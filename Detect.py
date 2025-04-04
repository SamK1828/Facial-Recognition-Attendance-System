import cv2
import os
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import numpy as np

# Load the face detection cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Load the known faces
known_faces = []
known_face_names = []
face_labels = {}
label_count = 0
for file in os.listdir('known_faces'):
    img = cv2.imread(os.path.join('known_faces', file))
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
    for (x, y, w, h) in faces:
        face = gray[y:y+h, x:x+w]
        face = cv2.resize(face, (100, 100))
        known_faces.append(face)
        name = file.split('.')[0]
        if name not in face_labels:
            face_labels[name] = label_count
            label_count += 1
        known_face_names.append(face_labels[name])

# Create a face recognizer
recognizer = cv2.face.LBPHFaceRecognizer()
recognizer.train(known_faces, np.array(known_face_names))

# Define a function to recognize faces
def recognize_faces(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
    for (x, y, w, h) in faces:
        face = gray[y:y+h, x:x+w]
        face = cv2.resize(face, (100, 100))
        label, confidence = recognizer.predict(face)
        for name, label_id in face_labels.items():
            if label == label_id:
                name = name
        print(f"Found {name} in the image!")
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(image, name, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36, 255, 12), 2)
    return image

# Function to upload image from storage
def upload_image():
    Tk().withdraw()
    image_path = askopenfilename()
    return image_path

# Upload image from storage
image_path = upload_image()

# Load the image
image = cv2.imread(image_path)

# Recognize faces in the image
image = recognize_faces(image)

# Display the output
cv2.imshow('Face Recognition', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Mark attendance
attendance_file = "attendance.txt"
with open(attendance_file, "a") as f:
    for name in known_face_names:
        for key, value in face_labels.items():
            if value == name:
                f.write(f"{key}\n")
# Module facevector_generator.py
import cv2
import face_recognition


def generate_vector(image_file):
    image = cv2.imread(image_file)
    rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    boxes = face_recognition.face_locations(rgb, model="hog")
    encodings = face_recognition.face_encodings(rgb, boxes)
    return encodings

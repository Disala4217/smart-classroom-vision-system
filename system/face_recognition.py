import cv2
import os
from train_model import train
# Load the pre-trained face detection model
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

def save_face(student_id):
    cap = cv2.VideoCapture(0)  # Initialize video capture from the webcam
    count = 0
    person_dir = os.path.join("system/DataSet", str(student_id))  # Create a directory for the student ID
    os.makedirs(person_dir, exist_ok=True)  # Create directory if it doesn't exist

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame")
            break


        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Convert the frame to grayscale
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)  # Detect faces

        for (x, y, w, h) in faces:
            face = frame[y:y+h, x:x+w]  # Extract the face from the frame
            filepath = os.path.join(person_dir, f"img{count}.jpg")  # Define the file path
            cv2.imwrite(filepath, face)  # Save the captured face image
            count += 1
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)  # Draw rectangle around the face

        # Display the frame with the detected face(s)
        cv2.imshow("Face Capture", frame)

        # Exit if 'q' is pressed or if 100 images have been captured
        if cv2.waitKey(1) & 0xFF == ord('q') or count >= 500:
            break

    cap.release()
    cv2.destroyAllWindows()
    train

# Example usage


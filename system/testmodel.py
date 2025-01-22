import cv2
import numpy as np
import tensorflow as tf
from database import gtIdName
from attendence import setStudent


def recognize():
    
    # Load the pre-trained face recognition model
    model = tf.keras.models.load_model("face_recognition_model.keras")

    # Define class labels (manually or load from a separate file)
    class_labels = gtIdName()

    # Real-time face recognition
    cap = cv2.VideoCapture(0)  # Capture from webcam

    # Load OpenCV's Haar cascade for face detection
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    ID=0
    count=0
    while True:
        ret, frame = cap.read()

        # Convert frame to grayscale for face detection
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # Detect faces in the frame
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)

        for (x, y, w, h) in faces:
            face = frame[y:y+h, x:x+w]  # Extract the face from the frame
            resized_face = cv2.resize(face, (128, 128)) / 255.0  # Normalize the image
            prediction = model.predict(np.expand_dims(resized_face, axis=0))  # Get model prediction

            # Get predicted class index
            predicted_index = np.argmax(prediction)

            # Get the label of the predicted class
            label = class_labels.get(predicted_index, "Unknown")  # Handle invalid indices

            # Debug: Print prediction and predicted index
            print(f"Predicted index: {predicted_index}, Label: {label}")
            ID+=predicted_index
            count+=1
            attendenceApprovingTime=10000
            x=attendenceApprovingTime
            if count<=x:
                idx=((ID+x)/x)-1
                if predicted_index==idx:
                    print("Student Detected")
                    setStudent(predicted_index)
                    ID=0
                    count=0
            

            # Draw rectangle around the face
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

            # Display name and index on the face rectangle
            label_text = f"{label} ({predicted_index})"
            cv2.putText(frame, label_text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

        # Show the frame with face detection and recognition
        cv2.imshow("Face Recognition", frame)

        # Exit when 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

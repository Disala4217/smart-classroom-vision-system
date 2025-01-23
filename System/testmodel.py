import cv2
import numpy as np
import tensorflow as tf
from database import gtIdName
from attendence import setStudent

ID = 0
count = 0

def recognize():
    global ID, count
    
    # Load the pre-trained face recognition model
    model = tf.keras.models.load_model("face_recognition_model.keras")

    # Define class labels (manually or load from a separate file)
    class_labels = gtIdName()

    # Real-time face recognition
    cap = cv2.VideoCapture(0)  # Capture from webcam

    # Load OpenCV's Haar cascade for face detection
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    
    while True:
        ret, frame = cap.read()

        # Check if the frame was captured correctly
        if not ret or frame is None:
            recognize()
        
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
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

            # Display name and index on the face rectangle
            label_text = f"{label} ({predicted_index})"
            cv2.putText(frame, label_text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

            # Debug: Print prediction and predicted index
            print(f"Predicted index: {predicted_index}, Label: {label}")
            ID += predicted_index
            count += 1
            attendence_approving_time = 1000000  # Rename the variable to avoid conflict with `x`
            if count <= attendence_approving_time:
                idx = ((ID + attendence_approving_time) / attendence_approving_time) - 1
                if predicted_index == idx:
                    print("Student Detected \nClosing frame")
                    cap.release()
                    cv2.destroyAllWindows()
                    
                    setStudent(predicted_index)
                    break  # Exit after handling attendance

        # Show the frame with face detection and recognition
        cv2.imshow("Face Recognition", frame)

        # Exit when 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()  # Release the webcam
    cv2.destroyAllWindows()  # Close the window



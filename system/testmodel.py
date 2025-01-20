import numpy as np
import cv2
import tensorflow as tf  # Import TensorFlow

# Load the trained model
model = tf.keras.models.load_model("face_recognition_model.h5")

# Define class labels (manually or load from a separate file)
class_labels = {0: 'Disala', 1: 'christ', 2: 'mark rufflo',3: 'thor',4: 'ironman',5: 'black widow',6:"ashoka",7:"ashoka"}  # Update with your actual class labels

# Real-time face recognition
cap = cv2.VideoCapture(0)  # Capture from webcam
while True:
    ret, frame = cap.read()
    
    # Preprocess the frame to match model input size
    resized_frame = cv2.resize(frame, (128, 128)) / 255.0  # Normalize the image
    prediction = model.predict(np.expand_dims(resized_frame, axis=0))  # Get model prediction
    
    # Get label of the predicted class
    label = class_labels[np.argmax(prediction)]
    
    # Display the label on the frame
    cv2.putText(frame, label, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    
    # Show the frame with the label
    cv2.imshow("Face Recognition", frame)

    # Exit when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

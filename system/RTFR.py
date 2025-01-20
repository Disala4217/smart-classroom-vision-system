import numpy as np

# Load the trained model
model = tf.keras.models.load_model("face_recognition_model.h5")

# Load the class labels
class_labels = train_data.class_indices
class_labels = {v: k for k, v in class_labels.items()}  # Reverse mapping

# Real-time recognition
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    resized_frame = cv2.resize(frame, (128, 128)) / 255.0
    prediction = model.predict(np.expand_dims(resized_frame, axis=0))
    label = class_labels[np.argmax(prediction)]
    cv2.putText(frame, label, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.imshow("Face Recognition", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

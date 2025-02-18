import cv2
import numpy as np
import tensorflow as tf
from database import gtIdName
from attendence import setStudent
Grade=0
def recognize(grade):
    global Grade
    ID = 0
    count = 0   
    Grade=grade
    model = tf.keras.models.load_model("face_recognition_model.keras")
    class_labels = gtIdName(Grade)
    cap = cv2.VideoCapture(0)  
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    while True:
        ret, frame = cap.read()
        if not ret or frame is None:
            recognize(Grade)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)
        for (x, y, w, h) in faces:
            face = frame[y:y+h, x:x+w] 
            resized_face = cv2.resize(face, (128, 128)) / 255.0 
            prediction = model.predict(np.expand_dims(resized_face, axis=0))  
            predicted_index = np.argmax(prediction)
            label = class_labels.get(predicted_index, "Unknown")  
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
            label_text = f"{label} ({predicted_index})"
            cv2.putText(frame, label_text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
            print(f"Predicted index: {predicted_index}, Label: {label}")
            ID += predicted_index
            count += 1
            attendence_approving_time = 1000000 
            if count <= attendence_approving_time and label!="Unknown":
                idx = ((ID + attendence_approving_time) / attendence_approving_time) - 1
                if predicted_index == idx:
                    print("Student Detected \nClosing frame")
                    cap.release()
                    cv2.destroyAllWindows()
                    setStudent(predicted_index)
                    ID = 0
                    count = 0 
                    break  
        cv2.imshow("Face Recognition", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()  
    cv2.destroyAllWindows() 



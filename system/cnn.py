import os
import cv2
import numpy as np
from sklearn.model_selection import train_test_split
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from tensorflow.keras.preprocessing.image import img_to_array

# Load Dataset
def load_dataset(dataset_path, img_size=(100, 100)):
    images = []
    labels = []
    label_dict = {}

    for idx, person in enumerate(os.listdir(dataset_path)):
        label_dict[idx] = person
        person_path = os.path.join(dataset_path, person)
        for img_name in os.listdir(person_path):
            img_path = os.path.join(person_path, img_name)
            img = cv2.imread(img_path, cv2.IMREAD_COLOR)
            if img is not None:
                img = cv2.resize(img, img_size)
                img = img_to_array(img)
                images.append(img)
                labels.append(idx)

    return np.array(images), np.array(labels), label_dict

# Define the CNN Model
def create_cnn_model(input_shape, num_classes):
    model = Sequential([
        Conv2D(32, (3, 3), activation='relu', input_shape=input_shape),
        MaxPooling2D((2, 2)),
        Conv2D(64, (3, 3), activation='relu'),
        MaxPooling2D((2, 2)),
        Flatten(),
        Dense(128, activation='relu'),
        Dropout(0.5),
        Dense(num_classes, activation='softmax')
    ])
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
    return model

# Main Program
if __name__ == "__main__":
    # Parameters
    dataset_path = "dataset"  # Path to the dataset folder
    img_size = (100, 100)
    test_size = 0.2

    # Load dataset
    print("Loading dataset...")
    images, labels, label_dict = load_dataset(dataset_path, img_size)
    images = images / 255.0  # Normalize pixel values
    labels = to_categorical(labels, num_classes=len(label_dict))

    # Split dataset
    X_train, X_test, y_train, y_test = train_test_split(images, labels, test_size=test_size, random_state=42)

    # Create model
    print("Creating model...")
    model = create_cnn_model(input_shape=img_size + (3,), num_classes=len(label_dict))

    # Train model
    print("Training model...")
    model.fit(X_train, y_train, epochs=10, batch_size=32, validation_split=0.2)

    # Evaluate model
    print("Evaluating model...")
    test_loss, test_accuracy = model.evaluate(X_test, y_test)
    print(f"Test Accuracy: {test_accuracy * 100:.2f}%")

    # Save the model
    model.save("face_recognition_model.h5")
    print("Model saved as 'face_recognition_model.h5'.")

    # Test with an example image
    print("Testing with an example image...")
    test_img_path = os.path.join(dataset_path, "person1", "img1.jpg")  # Example path
    test_img = cv2.imread(test_img_path, cv2.IMREAD_COLOR)
    test_img = cv2.resize(test_img, img_size)
    test_img = np.expand_dims(test_img / 255.0, axis=0)
    prediction = model.predict(test_img)
    predicted_label = label_dict[np.argmax(prediction)]
    print(f"Predicted Label: {predicted_label}")

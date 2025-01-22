import os
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Conv2D, MaxPooling2D, Flatten
from tensorflow.keras.optimizers import Adam

def train():
    # Set the directory for your dataset
    dataset_directory = 'system/dataset'  # Make sure your dataset is stored here

    # Data augmentation and preprocessing for training
    datagen = ImageDataGenerator(rescale=1.0/255.0, validation_split=0.2)

    # Load training and validation datasets
    train_generator = datagen.flow_from_directory(
        dataset_directory,
        target_size=(128, 128),
        batch_size=32,
        class_mode='categorical',
        subset='training')

    validation_generator = datagen.flow_from_directory(
        dataset_directory,
        target_size=(128, 128),
        batch_size=32,
        class_mode='categorical',
        subset='validation')

    # Build the model (a simple CNN)
    model = Sequential([
        Conv2D(32, (3, 3), activation='relu', input_shape=(128, 128, 3)),
        MaxPooling2D(pool_size=(2, 2)),
        Conv2D(64, (3, 3), activation='relu'),
        MaxPooling2D(pool_size=(2, 2)),
        Flatten(),
        Dense(128, activation='relu'),
        Dense(train_generator.num_classes, activation='softmax')  # The number of classes is the number of unique people
    ])

    # Compile the model
    model.compile(optimizer=Adam(), loss='categorical_crossentropy', metrics=['accuracy'])

    # Train the model
    model.fit(
        train_generator,
        steps_per_epoch=train_generator.samples // 32,
        epochs=10,
        validation_data=validation_generator,
        validation_steps=validation_generator.samples // 32
    )

    # Save the trained model
    model.save('face_recognition_model.keras')
    print("Model saved as face_recognition_model.keras")


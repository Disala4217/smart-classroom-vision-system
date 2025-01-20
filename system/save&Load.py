# Save the trained model
model.save("face_recognition_model.h5")

# Load the model later for inference
model = tf.keras.models.load_model("face_recognition_model.h5")

import cv2

def detect_faces(frame):
    """
    Detect faces in a video frame using Haar Cascade Classifier.

    Args:
        frame (numpy.ndarray): The video frame from OpenCV.

    Returns:
        list: A list of bounding box coordinates for detected faces [(x, y, w, h), ...].
        numpy.ndarray: The video frame with bounding boxes drawn around detected faces.
    """
    # Load Haar Cascade Classifier for face detection
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

    # Convert the frame to grayscale (required for Haar Cascade)
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(
        gray_frame,
        scaleFactor=1.1,  # Parameter specifying how much the image size is reduced at each image scale
        minNeighbors=5,   # Parameter specifying how many neighbors each candidate rectangle should have
        minSize=(30, 30)  # Minimum size of the face to detect
    )

    # Draw rectangles around detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    return faces, frame

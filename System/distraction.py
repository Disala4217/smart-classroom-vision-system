import cv2
import dlib
import numpy as np
import time

c1 = 0
c2 = 0
c3 = 0
c4 = 0
c5 = 0
c6 = 0
deduction_points = 0  # Global deduction_points

def engagement():
    global c1, c2, c3, c4, c5, c6, deduction_points
    # Load the facial landmark detector
    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

    # Camera matrix for head pose estimation
    camera_matrix = np.array([[640, 0, 320],
                            [0, 640, 240],
                            [0, 0, 1]], dtype="double")
    dist_coeffs = np.zeros((4, 1))

    # Define 3D model points for head pose estimation
    model_points = np.array([
        (0.0, 0.0, 0.0),        # Nose tip
        (0.0, -330.0, -65.0),   # Chin
        (-225.0, 170.0, -135.0), # Left eye corner
        (225.0, 170.0, -135.0), # Right eye corner
        (-150.0, -150.0, -125.0), # Left mouth corner
        (150.0, -150.0, -125.0)  # Right mouth corner
    ], dtype="double")

    def calculate_eye_aspect_ratio(eye):
        A = np.linalg.norm(eye[1] - eye[5])
        B = np.linalg.norm(eye[2] - eye[4])
        C = np.linalg.norm(eye[0] - eye[3])
        return (A + B) / (2.0 * C)

    def calculate_mouth_aspect_ratio(mouth):
        A = np.linalg.norm(mouth[2] - mouth[10])  # Vertical
        B = np.linalg.norm(mouth[4] - mouth[8])   # Vertical
        C = np.linalg.norm(mouth[0] - mouth[6])   # Horizontal
        return (A + B) / (2.0 * C)

    def detect_distraction(frame):
        global c1, c2, c3, c4, c5, c6, deduction_points  # Global declaration for deduction_points
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = detector(gray)

        for face in faces:
            landmarks = predictor(gray, face)
            landmarks = np.array([[p.x, p.y] for p in landmarks.parts()])

            # Eye coordinates
            left_eye = landmarks[36:42]
            right_eye = landmarks[42:48]
            mouth = landmarks[48:68]

            # Calculate EAR and MAR
            left_ear = calculate_eye_aspect_ratio(left_eye)
            right_ear = calculate_eye_aspect_ratio(right_eye)
            mar = calculate_mouth_aspect_ratio(mouth)

            # Detect yawning
            if mar > 0.7:
                cv2.putText(frame, "Yawning!", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
                x = 3
                if c1 <= x:
                    c1 += 1
                else:
                    print("yawning")
                    deduction_points += 1  # Modify global deduction_points
                    c1 = 0
                    break

            # Detect talking
            if 0.5 < mar <= 0.7:
                cv2.putText(frame, "Talking!", (10, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)
                x = 8
                if c2 <= x:
                    c2 += 1
                else:
                    print("talking")
                    deduction_points += 2  # Modify global deduction_points
                    c2 = 0
                    break

            # Detect smiling
            if mar < 0.5 and np.linalg.norm(mouth[0] - mouth[6]) > 80:
                cv2.putText(frame, "Smiling!", (10, 150), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                x = 1000
                if c3 <= x:
                    c3 += 1
                else:
                    print("Smiling")
                    deduction_points += 1  # Modify global deduction_points
                    c3 = 0
                    break

            # Head pose estimation
            image_points = np.array([
                landmarks[30],  # Nose tip
                landmarks[8],   # Chin
                landmarks[36],  # Left eye corner
                landmarks[45],  # Right eye corner
                landmarks[48],  # Left mouth corner
                landmarks[54]   # Right mouth corner
            ], dtype="double")

            success, rotation_vector, translation_vector = cv2.solvePnP(
                model_points, image_points, camera_matrix, dist_coeffs
            )

            rotation_matrix, _ = cv2.Rodrigues(rotation_vector)
            yaw_angle = np.arctan2(rotation_matrix[1, 0], rotation_matrix[0, 0]) * (180 / np.pi)
            pitch_angle = np.arctan2(-rotation_matrix[2, 0], np.sqrt(rotation_matrix[2, 1]**2 + rotation_matrix[2, 2]**2)) * (180 / np.pi)
            roll_angle = np.arctan2(rotation_matrix[2, 1], rotation_matrix[2, 2]) * (180 / np.pi)

            # Detect head direction changes
            if abs(yaw_angle) > 25:
                cv2.putText(frame, "Distracted (Head: Yaw)!", (10, 200), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
                x = 1
                if c4 <= x:
                    c4 += 1
                else:
                    print("head yaw")
                    deduction_points += 1  # Modify global deduction_points
                    c4 = 0
                    break

            if abs(pitch_angle) > 15:
                cv2.putText(frame, "Distracted (Head: Pitch)!", (10, 250), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
                x = 25
                if c5 <= x:
                    c5 += 1
                else:
                    print("Head pitch")
                    deduction_points += 1  # Modify global deduction_points
                    c5 = 0
                    break

            if abs(roll_angle) > 50:
                cv2.putText(frame, "Distracted (Head: Roll)!", (10, 300), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
                x = 1000
                if c6 <= x:
                    c6 += 1
                else:
                    print("Head Roll")
                    deduction_points += 1  # Modify global deduction_points
                    c6 = 0
                    break

            # Draw circles on the eyes and mouth landmarks
            for point in left_eye:
                cv2.circle(frame, tuple(point), 2, (0, 255, 0), -1)
            for point in right_eye:
                cv2.circle(frame, tuple(point), 2, (0, 255, 0), -1)
            for point in mouth:
                cv2.circle(frame, tuple(point), 2, (255, 0, 255), -1)

        return frame

    # Webcam feed
    cap = cv2.VideoCapture(0)

    start_time = time.time()  # Get the start time
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame = detect_distraction(frame)
        cv2.imshow("Distraction Detection", frame)

        # Check elapsed time (in seconds)
        elapsed_time = time.time() - start_time

        if elapsed_time > 30:  # Timer condition (30 seconds)
            print(f"Time elapsed: {elapsed_time} seconds")
            start_time = time.time()
            break  # Reset start time for the next interval

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    return deduction_points

# Run the engagement function

import cv2
from tkinter import messagebox
from PIL import Image
from utils import save_image
import time
from face_detection import detect_faces


def save_face(name, student_id):
    """Capture 500 images of a student's face when movement is detected and save them locally."""
    try:
        # Open webcam
        cam = cv2.VideoCapture(0)
        if not cam.isOpened():
            raise Exception("Cannot access webcam.")

        messagebox.showinfo("Info", "Move slightly, and images will be captured automatically.")

        base_dir = "faces"
        image_count = 0
        previous_frame = None

        while image_count < 100:
            ret, frame = cam.read()
            if not ret:
                raise Exception("Failed to capture image.")

            # Convert to grayscale for motion detection
            gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            gray_frame = cv2.GaussianBlur(gray_frame, (21, 21), 0)

            if previous_frame is None:
                previous_frame = gray_frame
                continue

            # Calculate the absolute difference between the current and previous frames
            frame_delta = cv2.absdiff(previous_frame, gray_frame)
            threshold = cv2.threshold(frame_delta, 25, 255, cv2.THRESH_BINARY)[1]
            threshold = cv2.dilate(threshold, None, iterations=2)

            # Find contours to detect movement
            contours, _ = cv2.findContours(threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            movement_detected = any(cv2.contourArea(contour) > 5000 for contour in contours)

            if movement_detected or detect_faces(frame):
                # Save the image when movement is detected
                pil_image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
                image_path = save_image(pil_image, student_id, base_dir)
                if not image_path:
                    raise Exception("Failed to save image.")

                image_count += 1
                print(f"Captured image {image_count}/100")

                # Wait briefly before capturing the next image
                time.sleep(0.5)

            # Update the previous frame for the next iteration
            previous_frame = gray_frame

            # Display the frame (for debugging purposes)
            cv2.imshow("Capture Face - Move to capture", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cam.release()
        cv2.destroyAllWindows()

        messagebox.showinfo("Success", f"Captured {image_count} images for {name} successfully.")

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")
    finally:
        if 'cam' in locals() and cam.isOpened():
            cam.release()
        cv2.destroyAllWindows()

import cv2
import time

# Detect object in video stream using Haarcascade Frontal Face
face_cascade = cv2.CascadeClassifier('models/haarcascade_frontalface_default.xml')
time.sleep(1)

# For each person, one face id
ID = input('Enter your ID: ')

# Wait for 2 seconds to be able to switch to the Webcam Window.
print("Please get your face ready!")
time.sleep(2)

# Initialize the camera
camera = cv2.VideoCapture(0)
camera.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)

# Display window
display_window = cv2.namedWindow("Dataset Generating...")

# Initialize sample face image
start_time = time.time()
interval = 500  # Capture an image every 500 milliseconds
current_time = start_time
image_count = 0  # Total number of images captured

# Start looping
while True:
    ret, image = camera.read()
    if not ret:
        break

    # Convert frame to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 5)

    # Loop through faces
    for (x, y, w, h) in faces:
        # Draw rectangle around the face
        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)

        # Check if enough time has passed to capture an image and if image count is less than 100
        if (time.time() - current_time) * 1000 >= interval and image_count < 100:
            # Save the captured image into the datasets folder
            cv2.imwrite(f"dataset/data.{ID}.{int(time.time() * 1000)}.jpg", gray[y:y + h, x:x + w])
            current_time = time.time()
            image_count += 1

    # Display the video frame with rectangle
    cv2.imshow("Dataset Generating...", image)

    # To stop taking video, press 'q' key or if image count reaches 100
    if cv2.waitKey(1) & 0xFF == ord('q') or image_count >= 100:
        break

# Release the camera and close all windows
camera.release()
cv2.destroyAllWindows()
import cv2

# Load pre-trained face recognition model
faceRecognizer = cv2.face.LBPHFaceRecognizer_create()
faceRecognizer.read("models/trained_lbph_face_recognizer_model.yml")

# Load Haarcascade for face detection
faceCascade = cv2.CascadeClassifier("models/haarcascade_frontalface_default.xml")

fontFace = cv2.FONT_HERSHEY_SIMPLEX
fontScale = 0.6
fontColor = (255, 255, 255)
fontWeight = 2
fontBottomMargin = 30

nametagColor = (255, 0, 0)
nametagHeight = 50

faceRectangleBorderColor = nametagColor
faceRectangleBorderSize = 2

# Open a connection to the first webcam
camera = cv2.VideoCapture(0)

# Start looping
while True:
    # Capture frame-by-frame
    ret, frame = camera.read()
    if not ret:
        break

    # Convert frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = faceCascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # For each face found
    for (x, y, w, h) in faces:

        # Recognize the face
        ID, Confidence = faceRecognizer.predict(gray[y:y + h, x:x + w])

        if ID == 0:
            Person = "pseudo"
        if ID == 1:
            Person = "Gabriel"
        elif ID == 2:
            Person = "Dalyoung"
        elif ID == 3:
            Person = "Godwill"
        elif ID == 4:
            Person = "Bright"
        elif ID == 5:
            Person = "Bena"  
        elif ID == 6:
            Person = "Sugira"                       
        # Confidence normalization to a 0-100 scale
        Confidence = 100 - Confidence

       
        if Confidence>45:
            # Create rectangle around the face
            cv2.rectangle(frame, (x - 20, y - 20), (x + w + 20, y + h + 20), faceRectangleBorderColor, faceRectangleBorderSize)

             # Display name tag
            cv2.rectangle(frame, (x - 22, y - nametagHeight), (x + w + 22, y - 22), nametagColor, -1)
            cv2.putText(frame, str(Person) + ": " + str(round(Confidence, 2)) + "%", (x, y-fontBottomMargin), fontFace, fontScale, fontColor, fontWeight)

    # Display the resulting frame
    cv2.imshow('Detecting Faces...', frame)

    # Exit loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close all OpenCV windows
camera.release()
cv2.destroyAllWindows()

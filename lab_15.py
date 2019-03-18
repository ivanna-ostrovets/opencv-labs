import cv2


def lab_15(filename):
    face_cascade = cv2.CascadeClassifier("filename")
    video_capture = cv2.VideoCapture(filename)

    while True:
        frame = video_capture.read()[1]
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30))

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        cv2.namedWindow("", cv2.WINDOW_NORMAL)
        cv2.imshow("Video", cv2.resize(frame, (960, 540)))

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    video_capture.release()
    cv2.destroyAllWindows()

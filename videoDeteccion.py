import cv2
import time

import imutils


video_path = "video huevos.mp4"

window_name = f"Detectando huevos en {video_path}"
cascade_Huevos_Normales = cv2.CascadeClassifier("huevosNormales.xml")

video = cv2.VideoCapture(video_path)
while True:
    ret, frame = video.read()
    if not ret:
        break
    imageGray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    detected_objects = cascade_Huevos_Normales.detectMultiScale(
        imageGray, scaleFactor=1.3, minNeighbors=610,  minSize=(60, 60),  # 5  # 3500
    )
    # Draw rectangles

    if len(detected_objects) != 0:

        for (x, y, w, h) in detected_objects:

            cv2.rectangle(
                img=frame,
                pt1=(x, y),
                pt2=(x + w, y + h),
                color=(0, 255, 0),
                thickness=5,
            )

            cv2.putText(
                frame, "Huevo", (x, y - 10), 2, 6.0, (0, 255, 0), 2, cv2.LINE_AA
            )

    # Resize window to fit screen, since it's vertical and long

    cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)

    cv2.imshow(window_name, frame)

    if cv2.waitKey(1) == 27:

        break

    # Sleep for 1/30 seconds to get 30 frames per second in the output

    # time.sleep(1 / 60)

video.release()

cv2.destroyAllWindows()

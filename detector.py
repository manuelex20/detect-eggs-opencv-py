import cv2


cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)  # 0 = cámara por default. Si

modeloHuevos = cv2.CascadeClassifier("imagenes/queresa/queresa.xml")

while True:

    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    toy = modeloHuevos.detectMultiScale(
        gray, scaleFactor=4, 
        minNeighbors=630,
        minSize=(80,80)  # 5  # 3500
    )

    for (x, y, w, h) in toy:

        cv2.rectangle(
            img=frame, pt1=(x, y), pt2=(x + w, y + h), color=(0, 255, 0), thickness=1
        )

        cv2.putText(frame, "arania", (x, y - 10), 2, 0.7, (0, 255, 0), 2, cv2.LINE_AA)

    cv2.imshow("frame", frame)

    if cv2.waitKey(1) == 27:
        break

cap.release()

cv2.destroyAllWindows()

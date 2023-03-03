import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(0)  # 内部摄像头为0 外部为1

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

pTime = 0
cTime = 0

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    # print(results.multi_hand_landmarks)
    if results.multi_hand_landmarks:  # 如果检测到手
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                # print(id, lm)
                h, w, c = img.shape
                cx, cy = int(lm.x*w), int(lm.y*h)
                print(id, ':', cx, cy)
                if id % 4 == 0:
                    cv2.circle(img, (cx, cy), 8, (255, 0, 255), cv2.FILLED)

            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

    # 帧率显示
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
    cv2.putText(img, 'fps:'+str(int(fps)), (10, 70), cv2.FONT_HERSHEY_DUPLEX, 0.8, (205, 90, 106), 2)

    cv2.imshow("Image", img)
    cv2.waitKey(1)

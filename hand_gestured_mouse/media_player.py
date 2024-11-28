import cv2
import mediapipe as mp

cap = cv2.VideoCapture(0)

drawing = mp.solutions.drawing_utils
hands = mp.solutions.hands
hand_obj = hands.Hands(max_num_hands=1)

while True:
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)

    res = hand_obj.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

    if res.multi_hand_landmarks:
        drawing.draw_landmarks(frame, res.multi_hand_landmarks[0], hands.HAND_CONNECTIONS)

    cv2.imshow("window", frame)

    if cv2.waitKey(1) == 27:
        cv2.destroyWindow()
        cap.release()
        break
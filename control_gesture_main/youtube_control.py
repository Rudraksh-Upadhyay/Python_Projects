import cv2
import mediapipe as mp

import time
import pyautogui
from popup import popupmsg


drawing = mp.solutions.drawing_utils
hands = mp.solutions.hands
hand_obj = hands.Hands(max_num_hands=1)

cap = cv2.VideoCapture(0)
popupmsg("YOUTUBE IS IN HANDS")

def count_fingers(lst):
    count = 0

    thresh = (lst.landmark[0].y * 100 - lst.landmark[9].y * 100)/2

    if (lst.landmark[5].y * 100 - lst.landmark[8].y * 100) > thresh:
        count += 1
    if (lst.landmark[9].y * 100 - lst.landmark[12].y * 100) > thresh:
        count += 1
    if (lst.landmark[13].y * 100 - lst.landmark[16].y * 100) > thresh:
        count += 1
    if (lst.landmark[17].y * 100 - lst.landmark[20].y * 100) > thresh:
        count += 1
    if (lst.landmark[5].x * 100 - lst.landmark[4].x * 100) < -5:
        count += 1

    if (lst.landmark[4].x * 100 - lst.landmark[20].x * 100) < 3:
        count = -1


    return count

start_init = False
prev = -1

while True:
    end_time = time.time()
    # t.sleep(0.2)
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)

    res = hand_obj.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))



    if res.multi_hand_landmarks:

        hand_keyPoints = res.multi_hand_landmarks[0]

        count = count_fingers(hand_keyPoints)
        # print(count)



        if not (prev == count):

            if not start_init:
                start_time = time.time()
                start_init = True

            elif end_time - start_time > 0.2:
                if count == 1:
                    pyautogui.press("right")
                elif count == 2:
                    pyautogui.press("left")
                elif count == 3:
                    pyautogui.press("up")
                elif count == 4:
                    pyautogui.press("down")
                elif count == 5:
                    pyautogui.press("space")

                elif count == -1:
                    popupmsg("GESTURE MODE OFF")
                    break

                prev = count
                start_init = False

        drawing.draw_landmarks(frame, hand_keyPoints, hands.HAND_CONNECTIONS)




    cv2.imshow("window", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
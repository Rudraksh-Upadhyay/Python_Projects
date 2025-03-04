import cv2
import mediapipe as mp
import pyautogui

cap = cv2.VideoCapture(0)
hand_detector = mp.solutions.hands.Hands()
drawing_utils = mp.solutions.drawing_utils
screen_width, screen_height = pyautogui.size()
index_y = 0

while True:
    _, frame = cap.read()
    mirrored_frame = cv2.flip(frame,1)
    frame_height, frame_width, _ = frame.shape
    # 1 ka matlab horizontal flip

    rgb_frame = cv2.cvtColor(mirrored_frame, cv2.COLOR_BGR2RGB)
    output = hand_detector.process(rgb_frame)
    hands = output.multi_hand_landmarks


    # print(hands)
    if hands:
        for hand in hands:
            drawing_utils.draw_landmarks(mirrored_frame, hand)

            landmarks = hand.landmark
            # print(landmarks)
            for id, landmark in enumerate(landmarks):
                x = int(landmark.x * frame_width)
                y = int(landmark.y * frame_height)
                # print(x,y)
                if id == 8:
                    cv2.circle(img=mirrored_frame, center=(x, y), radius=10, color=(0, 255, 255))
                    index_x = screen_width / frame_width * x
                    index_y = screen_height / frame_height * y
                    pyautogui.moveTo(index_x, index_y)

                if id == 4:
                    cv2.circle(img=mirrored_frame, center=(x, y), radius=10, color=(0, 255, 255))
                    thumb_x = screen_width / frame_width * x
                    thumb_y = screen_height / frame_height * y
                    if abs(index_y - thumb_y) < 50:
                        pyautogui.click()
                        print("clicked")
                        pyautogui.sleep(1)

    cv2.imshow('Virtual Mouse', mirrored_frame)
    # cv2.waitKey(1)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
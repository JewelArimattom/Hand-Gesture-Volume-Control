import cv2
import mediapipe as mp
import pyautogui

x1 ,y1, x2, y2 = 0, 0, 0, 0

webcam = cv2.VideoCapture(0)
my_hands = mp.solutions.hands.Hands()
drawing_units = mp.solutions.drawing_utils 



while True:
   _ , image = webcam.read()
   frame_height, frame_width, _ = image.shape
   rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
   output = my_hands.process(rgb_image)
   hands = output.multi_hand_landmarks

   if hands:
      for hand in hands:
         #drawing_units.draw_landmarks(image, hand) #line drawing
         landmarks = hand.landmark
         for id, landmark in enumerate(landmarks):
            x = int(landmark.x * frame_width)
            y = int(landmark.y * frame_height)

            if id == 8:
               cv2.circle(img=image,center=(x,y),radius=8 ,color=(0,255,255),thickness=1)
               x1, y1 = x, y

            if id == 4: #thumb
               cv2.circle(img=image,center=(x,y),radius=8 ,color=(0,0,255),thickness=1)
               x2, y2 = x, y

      distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5

      if distance < 50:
            pyautogui.press('volumedown')
      elif distance > 50:
            pyautogui.press('volumeup')
      elif distance == 50:
            pyautogui.press('volumemute')
      else:
            pass
              # cv2.line(image, (x1, y1), (x2, y2), (255, 0, 255), 3) #line drawing

               


   cv2.imshow("Volume Control", image)

   key = cv2.waitKey(10)

   if key == 27:
      break
   
webcam.release()
cv2.destroyAllWindows()
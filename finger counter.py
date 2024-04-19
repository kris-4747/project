import mediapipe
import cv2


medhands=mediapipe.solutions.hands
draw=mediapipe.solutions.drawing_utils


hand=medhands.Hands(max_num_hands=2)
video=cv2.VideoCapture(0)
while True:
    suc,img=video.read()
    img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    res=hand.process(img)
    img=cv2.cvtColor(img,cv2.COLOR_RGB2BGR)
    tip_ids=[4,8,12,16,20]
    lm_lst=[]    
    cv2.rectangle(img, (20, 350), (150, 450), (255, 0, 0), cv2.FILLED)
    
    if res.multi_hand_landmarks:
        # print(res.multi_hand_landmarks)
        for handlm in res.multi_hand_landmarks:
            for id,lm in enumerate(handlm.landmark):
                # print(id,lm)
                cx=lm.x
                cy=lm.y
                lm_lst.append([id,cx,cy])
                # print(lm_lst)
                if len(lm_lst)!=0 and len(lm_lst)==21:
                    finger_lst=[]
                    
                    
                    
                # thumb
                    if lm_lst[0][1]<lm_lst[1][1]:
                        if lm_lst[4][1]<lm_lst[3][1]:
                            finger_lst.append(0)
                        else:
                            finger_lst.append(1)
                    else:
                        if lm_lst[4][1]>lm_lst[3][1]:
                            finger_lst.append(0)
                        else:
                            finger_lst.append(1)

                    
                #other finger
                    for i in range(1,5):
                        if lm_lst[tip_ids[i]][2]>lm_lst[tip_ids[i]-2][2]:                #0-  lm_lst[4] [2]-y value     1-lm_lst[8][2]
                            finger_lst.append(0)
                        else:
                            finger_lst.append(1) 
                        # print(count)                 
                    # print(finger_lst)
                    if len(finger_lst)!=0:
                        fing_count=finger_lst.count(1)
                        # print(fing_count)
            
            cv2.putText(img,str(fing_count),(50,400),cv2.FONT_HERSHEY_COMPLEX,2,(255,255,255),2)
                                                                             #2-font scale next 2-thickness
            draw.draw_landmarks(img,handlm,medhands.HAND_CONNECTIONS,draw.DrawingSpec(color=(0,0,0),thickness=1,circle_radius=5),draw.DrawingSpec(color=(255,255,255),thickness=5))
                                                                      #landmark spec                                                  connection spec
    cv2.imshow('Hand',img)
    if cv2.waitKey(1) & 0XFF==ord('q'):
        break
video.release()
cv2.destroyAllWindows()
















# 1.Import necessary libraries: mediapipe for hand detection and landmark estimation, and cv2 for video capture and image processing.

# 2.Initialize MediaPipe Hands model for hand detection.

# 3.Start capturing video from the default webcam (index 0).

# 4.Enter a while loop to continuously process frames from the video feed.

# 5.Read a frame from the video capture.

# 6.Convert the color space of the frame from BGR to RGB (required by MediaPipe).

# 7.Process the frame using the MediaPipe Hands model to detect hands and landmarks.

# 8.Convert the color space of the frame back from RGB to BGR (for displaying with OpenCV).

# 9.Extract landmark positions from the detected hands and draw them on the frame using OpenCV.

# 10.Display the frame with the drawn landmarks.

# 11.Check for the 'q' keypress to exit the loop and release resources.

# 12.Release the video capture object and close all OpenCV windows.


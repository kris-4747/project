import cv2
import numpy as np
def sketch(image):
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    blur_gray = cv2.GaussianBlur(gray,(5,5),900)
    edges = cv2.Canny(blur_gray,45,90)
    ret,thre = cv2.threshold(edges,70,255,cv2.THRESH_BINARY_INV)
    return thre
cam = cv2.VideoCapture(0)
while 1:
    ret,frame = cam.read()
    cv2.imshow('Live Sketch', sketch(frame))
    if cv2.waitKey(1)==27:   #esc
        break
    if cv2.waitKey(1)==13:   #enter
        cv2.imwrite('sketch.jpg',sketch(frame))
        print('Image Saved!!!')
cam.release()
cv2.destroyAllWindows()




# Line 1-2 – Importing required libraries.
# Line 4-9 – Defining the sketch function. We will use this function to implement sketch using OpenCV.
# Line 5 – Convert the image from BGR to gray.
# Line 6 – Gaussian Blur the image, to remove Gaussian Noise.
# Line 7 – Find edges in the image using Canny Edge Detection.
# Line 8 – Threshold the image, to convert it to a binary image (just 0 and 255 pixels).
# Line 9 – Return the thresholded image.
# Line 11 – Instantiate the camera using cv2.VideoCapture(0). Here 0 means that it will use a webcam.
# Line 13 – Let’s start the loop.
# Line 14 – Read the image/frame from the camera.
# Line 15 – Show the sketch image returned by the sketch function when the current frame is passed into it.
# Line 16-17 – If someone hits the ESC key, break the code.
# Line 18-20 – If someone hits ENTER key, save the sketch.
# Line 22-23 – Close the webcam and destroy all open windows.
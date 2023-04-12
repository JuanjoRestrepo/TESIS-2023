# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 10:49:23 2018

@author: cap
"""

import cv2
import time
 
# Camera 0 is the integrated web cam on my netbook
camera_port = 0
 
#Number of frames to throw away while the camera adjusts to light levels
ramp_frames = 30
 
# Now we can initialize the camera capture object with the cv2.VideoCapture class.
# All it needs is the index to a camera port.

"""
cam.set(11,0) #Brillo
cam.set(12,1) #Contraste
cam.set(13,0) #Saturacion
cam.set(15,1) #Ganancia
cam.set(16,0.4) #Exposicion
"""
#capture from camera at location 0
cap = cv2.VideoCapture(0)

cap.set(cv2.cv2.CAP_PROP_FOURCC,1196444237) #('M','J','P','G')
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280.0)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720.0)
# Change the camera setting using the set() function
cap.set(cv2.cv2.CAP_PROP_EXPOSURE, 0.2)
cap.set(cv2.cv2.CAP_PROP_GAIN, 1)
cap.set(cv2.cv2.CAP_PROP_BRIGHTNESS, 0)
cap.set(cv2.cv2.CAP_PROP_CONTRAST, 1)
cap.set(cv2.cv2.CAP_PROP_SATURATION, 0)
#cap.set(cv2.cv2.CAP_PROP_FRAME_WIDTH,1280)
#cap.set(cv2.cv2.CAP_PROP_FRAME_HEIGHT,720)
 #1920 x 1080  1280 x 720 1920 x 1080    

time.sleep(2)

# Read the current setting from the camera
FOURCC = cap.get(cv2.cv2.CAP_PROP_FOURCC)
width = cap.get(cv2.cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.cv2.CAP_PROP_FRAME_HEIGHT)
brightness = cap.get(cv2.cv2.CAP_PROP_BRIGHTNESS)
contrast = cap.get(cv2.cv2.CAP_PROP_CONTRAST)
saturation = cap.get(cv2.cv2.CAP_PROP_SATURATION)
gain = cap.get(cv2.cv2.CAP_PROP_GAIN)
exposure = cap.get(cv2.cv2.CAP_PROP_EXPOSURE)
print("FOURCC: ", FOURCC)
print("Height: ", height)
print("Width: ", width)
print("Brightness: ", brightness)
print("Contrast: ", contrast)
print("Saturation: ", saturation)
print("Gain: ", gain)
print("Exposure: ", exposure)
# Captures a single image from the camera and returns it in PIL format
 
"""
0. CV_CAP_PROP_POS_MSEC Current position of the video file in milliseconds.
1. CV_CAP_PROP_POS_FRAMES 0-based index of the frame to be decoded/captured next.
3. CV_CAP_PROP_POS_AVI_RATIO Relative position of the video file
4. CV_CAP_PROP_FRAME_WIDTH Width of the frames in the video stream.
5. CV_CAP_PROP_FRAME_HEIGHT Height of the frames in the video stream.
6. CV_CAP_PROP_FPS Frame rate.
7. CV_CAP_PROP_FOURCC 4-character code of codec.
8. CV_CAP_PROP_FRAME_COUNT Number of frames in the video file.
9. CV_CAP_PROP_FORMAT Format of the Mat objects returned by retrieve() .
10. CV_CAP_PROP_MODE Backend-specific value indicating the current capture mode.
11. CV_CAP_PROP_BRIGHTNESS Brightness of the image (only for cameras).
12. CV_CAP_PROP_CONTRAST Contrast of the image (only for cameras).
13. CV_CAP_PROP_SATURATION Saturation of the image (only for cameras).
14. CV_CAP_PROP_HUE Hue of the image (only for cameras).
15. CV_CAP_PROP_GAIN Gain of the image (only for cameras).
16. CV_CAP_PROP_EXPOSURE Exposure (only for cameras).
17. CV_CAP_PROP_CONVERT_RGB Boolean flags indicating whether images should be converted to RGB.
18. CV_CAP_PROP_WHITE_BALANCE Currently unsupported
19. CV_CAP_PROP_RECTIFICATION Rectification flag for stereo cameras (note: only supported by DC1394 v 2.x backend currently)
"""
def get_image():
 # read is the easiest way to get a full image out of a VideoCapture object.
    retval, im = cap.read()
    return im
 


camera_capture = get_image()
cap.release()
cv2.imshow("Image", camera_capture)
cv2.waitKey(0)

#file = "/home/codeplasma/test_image.png"
# A nice feature of the imwrite method is that it will automatically choose the
# correct format based on the file extension you provide. Convenient!
#cv2.imwrite(file, camera_capture)
 
# You'll want to release the camera, otherwise you won't be able to create a new
# capture object until your script exits
del(cap)

# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 11:32:53 2018

@author: juandavid.contreras
"""

# import the necessary packages
from imutils import perspective
from imutils import contours
import numpy as np
import imutils
import cv2




"""
Cargar imagen, pikear color de fondo y obtener dimenciones
"""
image = cv2.imread("I1.jpg")
height, width, channels = image.shape
r=image[10][10][0]
g=image[10][10][1]
b=image[10][10][2]

"""
Pintar las lineas horizontales que separan los contornos
"""
HighP = height
WidthP = width
grosor = int(HighP*0.1)

al1 = HighP
al2 = int(HighP*0.7)
al3 = int(HighP*0.4)
al4 = int(HighP*0.1)
cv2.line(image,(0,al1),(WidthP,al1),(int(r),int(g),int(b)),grosor)
cv2.line(image,(0,al2),(WidthP,al2),(int(r),int(g),int(b)),grosor)
cv2.line(image,(0,al3),(WidthP,al3),(int(r),int(g),int(b)),grosor)
cv2.line(image,(0,al4),(WidthP,al4),(int(r),int(g),int(b)),grosor)
"""
Modificar imagen a escala de grises
"""
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (7, 7), 0)
cv2.imshow("Image", gray)
cv2.waitKey(0)

"""
Detectar bordes
"""
# perform edge detection, then perform a dilation + erosion to
# close gaps in between object edges
edged = cv2.Canny(gray, 50, 100)
edged = cv2.dilate(edged, None, iterations=1)
edged = cv2.erode(edged, None, iterations=1)
 
# find contours in the edge map
cnts = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL,
	cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if imutils.is_cv2() else cnts[1]

(cnts, _) = contours.sort_contours(cnts)
pixelsPerMetric = None
#205x260
#1704,2344
loc = np.array([[0],[0]])
p = 0

for c in cnts:
	# if the contour is not sufficiently large, ignore it
    if cv2.contourArea(c) < 150:
        continue
    # compute the rotated bounding box of the contour
    orig = image.copy()
    box = cv2.minAreaRect(c)
    box = cv2.cv.BoxPoints(box) if imutils.is_cv2() else cv2.boxPoints(box)
    box = np.array(box, dtype="int")

    box = perspective.order_points(box)
    cv2.drawContours(orig, [box.astype("int")], -1, (0, 255, 0), 2)

    #cv2.imshow("Image", orig)
    #cv2.waitKey(0)

    if p == 0:
        loc1 = box.astype("int")
        p = p+1
    elif p == 1:
        loc2 = box.astype("int")
        p = p+1
    elif p == 2:
        loc3 = box.astype("int")


"""
Calcular numero de prixeles entre lineas horizontales
"""
d1 = ((loc1[1][0]-loc1[0][0])+(loc1[2][0]-loc1[3][0]))/2
d2 = ((loc2[1][0]-loc2[0][0])+(loc2[2][0]-loc2[3][0]))/2
d3 = ((loc3[1][0]-loc3[0][0])+(loc3[2][0]-loc3[3][0]))/2

"""
Calcular dimencion en funcion de milimetros
"""
m1 = 22.0
m2 = round(1.002*d2*m1/d1,2)
m3 = round(0.986*d3*m1/d1,2)
print(m2)
print(m3)


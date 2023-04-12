# -*- coding: utf-8 -*-
"""
Created on Tue Apr  3 11:34:15 2018

@author: juandavid.contreras
"""
from imutils import perspective
from imutils import contours
import numpy as np
import imutils
import cv2

def contours_by_color(self,img,RGB1,RGB2):
    boundaries = [([RGB1[0], RGB1[1], RGB1[2]], [RGB2[0], RGB2[1], RGB2[2]])]  #limites del color permisible
    lower = np.array(boundaries[0][0], dtype=np.uint8)
    upper = np.array(boundaries[0][1], dtype=np.uint8)
    mask = cv2.inRange(img, lower, upper)  #activqr solo los pixeles que estan dentro del rango de color
    #Detectar bordes
    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
    	cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if imutils.is_cv2() else cnts[1]
    
    (cnts, _) = contours.sort_contours(cnts)
    return cnts
def pos():
    px= 640 #pixeles hotizontales
    #py= 480 #pixeles verticales
    a = 0 #referencia color 1
    b = 90 #referencia color 2
    image = cv2.imread('my.jpg', 1)  #improtar imagen, sacar de camara y reducir resolucion
    boundaries = [([a, b, 0], [a+20, b+50, 255])]  #limites del color permisible del guante
    lower = np.array(boundaries[0][0], dtype=np.uint8)
    upper = np.array(boundaries[0][1], dtype=np.uint8)
    mask = cv2.inRange(image, lower, upper)  #activqr solo los pixeles que estan dentro del rango de color
    #Detectar bordes
    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
    	cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if imutils.is_cv2() else cnts[1]
    
    (cnts, _) = contours.sort_contours(cnts)
    for c in cnts:
    	# tamaño minimo para ser tenido en cuenta
        if cv2.contourArea(c) < 400:
            continue
        # calcular el rectangulo que se ajuste al borde
        box = cv2.minAreaRect(c)
        box = cv2.cv.BoxPoints(box) if imutils.is_cv2() else cv2.boxPoints(box)
        box = np.array(box, dtype="int")    #convertir puntos a nunpy
        box = perspective.order_points(box) #ordenar puntos
        cv2.drawContours(image, [box.astype("int")], -1, (0, 255, 0), 2)
    #calcular punto medio del guante
    x1 = box[0][0]
    y1 = box[0][1]
    x2 = box[2][0]
    y2 = box[2][1]
    xp = int((x2+x1)/2)
    yp = int((y2+y1)/2)
    #calcular posiciones en mm
    LX=1000
    #LY=700
    mmp = LX/px
    x = xp*mmp
    y = yp*mmp
    x0 = 500
    y0 = 400
    X = x - x0
    Y = y - y0
    #dibujar lineas spbre punto medio
    #cv2.line(image,(0,y),(640,y),(255, 0, 0),2)
    #cv2.line(image,(x,0),(x,480),(255, 0, 0),2) 
    # show the images
    #cv2.imshow("images", image)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()
    return (X,Y)
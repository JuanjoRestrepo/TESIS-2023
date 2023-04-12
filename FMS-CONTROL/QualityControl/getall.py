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

class InspectionModule():
    """
    Modulo de inspeccion
    """
    def __init__(self,camera_port=0,):
        self.camera_port = camera_port
        self.camera = cv2.VideoCapture(camera_port)
        
    def get_image(self):
        #tomar una imagen con la camara
        retval, im = self.camera.read()
        return im 
    
    def picture(self):
        for i in range(6):
            pic = self.get_image()
        print("picture get it")
        return pic
    
    def background(self, image):
        r=image[10][10][0]
        g=image[10][10][1]
        b=image[10][10][2]
        return r,g,b
    
    def lines(self,image,h1,g1,h2,g2,h3,g3,h4,g4):
        r,b,g = self.background(image)
        height, width, channels = image.shape
        HighP = height
        WidthP = width
        al1 = int(HighP*h1)
        al2 = int(HighP*h2)
        al3 = int(HighP*h3)
        al4 = int(HighP*h4)
        cv2.line(image,(0,al1),(WidthP,al1),(int(r),int(g),int(b)),int(HighP*g1))
        cv2.line(image,(0,al2),(WidthP,al2),(int(r),int(g),int(b)),int(HighP*g2))
        cv2.line(image,(0,al3),(WidthP,al3),(int(r),int(g),int(b)),int(HighP*g3))
        cv2.line(image,(0,al4),(WidthP,al4),(int(r),int(g),int(b)),int(HighP*g4))
        return image
        
    def gray(self,image):
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) #convertir la iamgen a escala de grises
        #gray = cv2.GaussianBlur(gray, (5, 5), 0)
        return gray
        
    def contours(self,image):
        gray = image
        edged = cv2.Canny(gray, 50, 100)
        edged = cv2.dilate(edged, None, iterations=1)
        edged = cv2.erode(edged, None, iterations=1)
        cnts = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL,
        	cv2.CHAIN_APPROX_SIMPLE)
        cnts = cnts[0] if imutils.is_cv2() else cnts[1]
        (cnts, _) = contours.sort_contours(cnts)
        return cnts
        
    def measurePic(self,m1,fm2,fm3,h1,g1,h2,g2,h3,g3,h4,g4):
        img = self.picture()
        img = self.lines(img,h1,g1,h2,g2,h3,g3,h4,g4)
        img = self.gray(img)
        cnts = self.contours(img)
        p = 0
        for c in cnts:
        	 # if the contour is not sufficiently large, ignore it
            if cv2.contourArea(c) < 50:
                continue
            # compute the rotated bounding box of the contour
            orig = img.copy()
            box = cv2.minAreaRect(c)
            box = cv2.cv.BoxPoints(box) if imutils.is_cv2() else cv2.boxPoints(box)
            box = np.array(box, dtype="int")
            box = perspective.order_points(box)
            #cv2.drawContours(orig, [box.astype("int")], -1, (0, 255, 0), 2)
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
                
        #Calcular numero de pixeles entre lineas horizontales
        d1 = ((loc1[1][0]-loc1[0][0])+(loc1[2][0]-loc1[3][0]))/2
        d2 = ((loc2[1][0]-loc2[0][0])+(loc2[2][0]-loc2[3][0]))/2
        d3 = ((loc3[1][0]-loc3[0][0])+(loc3[2][0]-loc3[3][0]))/2
        #Calcular dimencion en funcion de milimetros
        m1 = m1
        m2 = round(fm2*d2*m1/d1,2)
        m3 = round(fm3*d3*m1/d1,2)
        return m2,m3, orig
    def endall(self):
        self.camera.release()
        cv2.destroyAllWindows()
      
cep = InspectionModule()
m2, m3, img = cep.measurePic(m1=22,fm2=1,fm3=1,h1=1,g1=0.5,h2=0.67,g2=0.07,h3=0.4,g3=0.07,h4=0.06,g4=0.07)
print(m2,m3)
#cv2.imshow("Image", img)
#cv2.waitKey(0)
cep.endall()


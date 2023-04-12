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
from numpy import interp

class InspectionModule():
    """
    Modulo de inspeccion
    """
    def __init__(self,camera_port=0,):
        self.camera_port = camera_port
        self.camera = cv2.VideoCapture(camera_port)
        self.camera.set(cv2.CAP_PROP_FOURCC,1196444237) #('M','J','P','G')
        self.camera.set(cv2.CAP_PROP_FRAME_WIDTH, 1280.0)
        self.camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 720.0)
        self.camera.set(cv2.CAP_PROP_EXPOSURE, 0.2)
        self.camera.set(cv2.CAP_PROP_GAIN, 1)
        self.camera.set(cv2.CAP_PROP_BRIGHTNESS, 0)
        self.camera.set(cv2.CAP_PROP_CONTRAST, 1)
        self.camera.set(cv2.CAP_PROP_SATURATION, 0)
    def get_image(self):
        #tomar una imagen con la camara
        retval, im = self.camera.read()
        return im 
    
    def picture(self):
        for i in range(20):
            pic = self.get_image()
        return pic
    
    def background(self, image):
        r=image[100][100][0]
        g=image[100][100][1]
        b=image[100][100][2]
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
        cv2.line(image,(100,0),(100,HighP),(int(r),int(g),int(b)),int(200))
        cv2.line(image,(150,0),(150,HighP),(int(r),int(g),int(b)),int(200))
        return image
        
    def gray(self,image):
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) #convertir la iamgen a escala de grises
        gray = cv2.GaussianBlur(gray, (5, 5), 0)
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
        #img = self.gray(img)
        cnts = self.contours(img)
        p = 0
        for c in cnts:
        	 # if the contour is not sufficiently large, ignore it
            if cv2.contourArea(c) < 100:
                continue
            # compute the rotated bounding box of the contour
            orig = img.copy()
            box = cv2.minAreaRect(c)
            box = cv2.cv.BoxPoints(box) if imutils.is_cv2() else cv2.boxPoints(box)
            box = np.array(box, dtype="int")
            box = perspective.order_points(box)
          
            cv2.drawContours(orig, [box.astype("int")], -1, (254, 254, 0), 1)
            cv2.imshow("Image", orig)
            cv2.waitKey(0)
          
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
        print("px1 = " + str(d1) +"-- px2 = " + str(d2) + "-- px3 = "+str(d3))
        #Calcular dimencion en funcion de milimetros
        #Para D2
        """
        mm21 = (0.992-0.990)/(181-164)
        mm22 = (0.990-0.992)/(203-181)
        bb21= 0.992-(mm21*181)
        bb22= 0.992-(mm22*181)
        #Para D3
        mm31 = (0.992-0.985)/(115-97)
        mm32 = (0.990-0.992)/(135-115)
        bb31= 0.992-(mm31*115)
        bb32= 0.992-(mm32*115)
        """
        """
        D2m1=0.978
        D2m2=
        D2m3=
        D3m1=0.97
        D3m2
        D3m3
        """
        if d2 >= 181:
            #fm2 = bb22+mm22*d2
            fm2 = interp(d2,[181,203],[0.975,0.978])
        else:
            #fm2 = bb21+mm22*d1
            fm2 = interp(d2,[163,181],[0.977,0.992])
            
        if d3 >= 115:
            #fm3 = bb32+mm32*d3
            fm3 = interp(d3,[116,135],[0.977,0.990])
        else:
            #fm3 = bb31+mm31*d3
            fm3 = interp(d3,[97,116],[0.967,0.992])
            
        m1 = m1
       
        print("F2:" + str(fm2) + "--- F3:" + str(fm3))
        m2 = fm2*d2*m1/d1
        m3 = fm3*d3*m1/d1
        
        print(m1,m2,m3)
        #self.endall() 
        return m2,m3
    def endall(self):
        self.camera.release()
        cv2.destroyAllWindows()
  

cep = InspectionModule()
m2,m3 = cep.measurePic(m1=22,fm2=0.990,fm3=0.990,h1=1,g1=0.25,h2=0.65,g2=0.40,h3=0.27,g3=0.32,h4=0.01,g4=0.17)
print("kjhkjhkjhkj")
print(m2,m3)
M3 = round(m3,1)
M2 = round(m2,1)
print(M2,M3)
cep.endall()

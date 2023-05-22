import cv2
import numpy as np

image=cv2.imread("Rubik cube\input\9774774ae7d9fbccc7927f4e6f9735c5.jpg")
image=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
R,G,B=cv2.split(image)

if B.all()==0 and (R==G).all()==255:       #yellow convert dark blue
    B=254
    R=0
    G=0

if R.all()==0 and (G==B).all()==255:       #cien convert Red
    B=0 
    R=254
    G=0

if G.all()==0 and R.all()==255 and B.all()==254:       #magenta convert Green
    B=1 
    R=255
    G=0
rubik=cv2.merge((R,G,B))

# cv2.imshow("",R)
cv2.imshow("rubik",rubik)
cv2.waitKey()
import cv2
import numpy as np

image=cv2.imread("Rubik cube\input\Rubik.jpg")
# image=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
R,G,B=cv2.split(image)

for i in range(image.shape[0]):
    for j in range(image.shape[1]):
        R,G,B=image[i,j]
        if B<50 and R>100 and G>100:       #yellow convert dark blue
            B=255
            R=0
            G=0

        if R<50 and G>100 and B>100:       #cien convert Red
            B=0 
            R=255
            G=0

        if B>100 and R>100 and G<50:       #magenta convert Green
            B=0
            R=0
            G=255


        image[i,j]=B,G,R
cv2.imwrite("Rubik cube/output/result.jpg",image)
cv2.waitKey()
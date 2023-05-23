import cv2
import numpy as np

image=cv2.imread("Watermelon/input/4acd2d1b192405fd3d44e64f73cd9f75.jpg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

R,G,B=cv2.split(image)

K=[]
K=R
R=G
G=K

image=cv2.merge((B,G,R))

cv2.imwrite("Watermelon/output/result.jpg",image)
cv2.waitKey()
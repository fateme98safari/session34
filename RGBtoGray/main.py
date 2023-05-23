import cv2
import numpy as np

color_image=cv2.imread("RGBtoGray\input\images.jpg")
color_image = cv2.cvtColor(color_image, cv2.COLOR_BGR2RGB)
R,G,B=cv2.split(color_image)


for i in range(color_image.shape[0]):
    for j in range(color_image.shape[1]):
        
        R,G,B=color_image[i,j]
        ave=int(R+G+B)//3
        color_image[i,j]=ave
       

   
# k=R[0,0]
# m=G[0,0]
# n=B[0,0]
# print(k)
# print(m)
# print(n)

# sum=R[0,0]+G[0,0]+B[0,0]
# print(sum)
# ave=sum//3
# print(ave)



cv2.imwrite("RGBtoGray/output/result.jpg",color_image)
cv2.waitKey()

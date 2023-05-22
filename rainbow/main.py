import cv2
import numpy as np

r=np.zeros((300 , 500) ,dtype=np.uint8)
g=np.zeros((300 , 500) ,dtype=np.uint8)
b=np.zeros((300 , 500) ,dtype=np.uint8)

r[:300,:500]=255
g[:300,:500]=255
b[:300,:500]=255

cv2.circle(b,(250,300), 230, 255, 25)
cv2.circle(g,(250,300), 230, 0, 25)
cv2.circle(r,(250,300), 230, 0,25)

cv2.circle(b,(250,300), 205, 255, 25)
cv2.circle(g,(250,300), 205, 110, 25)
cv2.circle(r,(250,300), 205,0 , 25)

cv2.circle(r,(250,300), 180, 20, 25)

cv2.circle(g,(250,300), 155, 100, 25)
cv2.circle(r,(250,300), 155, 20, 25)
cv2.circle(b,(250,300), 155, 0, 25)

cv2.circle(r,(250,300), 130, 255, 25)
cv2.circle(g,(250,300), 130, 165, 25)
cv2.circle(b,(250,300), 130, 0, 25)

cv2.circle(r,(250,300), 105, 130, 25)
cv2.circle(g,(250,300), 105, 0, 25)
cv2.circle(b,(250,300), 105, 0, 25)

cv2.circle(b,(250,300), 80, 50, 25)
cv2.circle(g,(250,300), 80,25 , 25)
cv2.circle(r,(250,300), 80, 80, 25)

rainbow=cv2.merge((r,g,b))

cv2.imshow("rainbow",rainbow)

cv2.waitKey()
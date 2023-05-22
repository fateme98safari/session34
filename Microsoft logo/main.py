import cv2
import numpy as np
import matplotlib.pyplot as plt


b=np.zeros((600 , 1400) ,dtype=np.uint8)
b[:600,:1400]=50
b[200:296,200:296]=250
b[304:400,304:400]=255

g=np.zeros((600,1400) , dtype=np.uint8)
g[:600,:1400]=50
g[200:296,304:400]=190
g[304:400,304:400]=180

r=np.zeros((600,1400),dtype=np.uint8)
r[:600,:1400]=50
r[304:400,200:296]=200
microsoft_logo=cv2.merge((r,g,b))

cv2.putText(microsoft_logo,'Microsoft', (450,350), cv2.FONT_HERSHEY_SIMPLEX, 5,(255,255,255), 7,2)
cv2.imshow("microsoft_logo",microsoft_logo)
cv2.waitKey()
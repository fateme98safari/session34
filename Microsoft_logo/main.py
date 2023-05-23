import cv2
import numpy as np
import matplotlib.pyplot as plt
from  PIL import ImageFont,ImageDraw, Image

b=np.zeros((600 , 1400) ,dtype=np.uint8)
b[:600,:1400]=50
b[200:296,200:296]=250
b[304:400,304:400]=255
b[304:400,200:296]=50
g=np.zeros((600,1400) , dtype=np.uint8)
g[:600,:1400]=50
g[200:296,304:400]=190
g[304:400,304:400]=180
g[304:400,200:296]=100


r=np.zeros((600,1400),dtype=np.uint8)
r[:600,:1400]=50
r[304:400,200:296]=250

microsoft_logo=cv2.merge((r,g,b))
microsoft_logo = cv2.cvtColor(microsoft_logo, cv2.COLOR_BGR2RGB)

microsoft_logo=Image.fromarray(microsoft_logo) 
   
draw = ImageDraw.Draw(microsoft_logo)  
   
 # use a truetype font  
font=ImageFont.truetype("C:\Windows\Fonts\micross.ttf",170)   
draw.text((450, 210), "Microsoft", font=font)  
   
microsoft_logo.save("Microsoft_logo/output/result.jpg") 
# cv2.putText(microsoft_logo,'Microsoft', (450,350), font=font, fontScale=5,color=(255,255,255), thickness=7)
# cv2.imshow("microsoft_logo",microsoft_logo)
cv2.waitKey()
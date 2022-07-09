import  cv2
import numpy as np

kernel = np.ones((5,54),np.uint8)
print(kernel)
img = cv2.imread("C:\\Users\\Daniel Samuel\\Desktop\\Robot car tools\\WhatsApp Image 2022-07-05 at 3.34.46 AM.jpeg")#load the image

img = cv2.resize(img, (200,200))
#CONVERT IMAGE TO GRAYSCALE
gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#blur image
blur_img = cv2.GaussianBlur(gray_img,(7,7),0)
# detect the edged
imgcanny = cv2.Canny(blur_img,100,200)
# enlarge the detected edge
imgdil = cv2.dilate(gray_img,kernel, iterations=1)
# make the detected edge small
imgerrod = cv2.erode(imgdil,kernel,iterations=1)


#display  images
cv2.imshow("Gray image", gray_img)
cv2.imshow("image canny", imgcanny)
cv2.imshow("image dilate", imgdil)
cv2.imshow("image dilate", imgerrod)
cv2.waitKey(0)

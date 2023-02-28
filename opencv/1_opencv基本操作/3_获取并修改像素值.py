import numpy as np
import cv2 as cv

img = cv.imread("../image/sunrise.png", 1)
px = img[100, 100]
px_B = px[0]
print(px)
print(px_B)

image1 = np.zeros((100, 100, 3), np.uint8)
px1 = image1[20, 20]
image1[50, 50] = (255, 255, 255)
cv.imshow("demo1", image1)
cv.waitKey(0)

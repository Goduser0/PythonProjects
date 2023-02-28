import cv2
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread("../../image/l_c.jpg")
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
pre_img = cv.medianBlur(gray, 7)
# cv.imshow("pre_img", pre_img)
# cv.waitKey(0)

circles = cv.HoughCircles(pre_img, cv2.HOUGH_GRADIENT, 1, 200, param1=100, param2=50, minRadius=0, maxRadius=100)
print(circles)

for circle in circles[0, :]:
    cv.circle(img, (int(circle[0]), int(circle[1])),  int(circle[2]), (0, 0, 255), 2)
    cv.circle(img, (int(circle[0]), int(circle[1])), 2, (0, 255, 0), -1)

plt.imshow(img[:, :, ::-1])
plt.show()

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('../image/cctv.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
corners = cv.goodFeaturesToTrack(gray, 1000, 0.01, 10)
for i in corners:
    x, y = i.ravel()
    cv.circle(img, (int(x), int(y)), 2, (0, 0, 255), -1)

cv.imshow('Shi-Tomas', img)
cv.waitKey(0)

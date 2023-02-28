import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread("../../image/blur.jpg", 0)
medianBlur = cv.medianBlur(img, 5)
cv.imshow("orign", img)
cv.imshow("median", medianBlur)
cv.waitKey(0)

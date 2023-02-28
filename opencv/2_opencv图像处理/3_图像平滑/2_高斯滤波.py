import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread("../../image/blur.jpg", 0)
GaussianBlur = cv.GaussianBlur(img, (3, 3), 1)
cv.imshow("orign", img)
cv.imshow("blur", GaussianBlur)
cv.waitKey(0)

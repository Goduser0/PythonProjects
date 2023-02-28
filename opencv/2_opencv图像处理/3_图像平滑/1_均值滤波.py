import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread("../../image/blur.jpg", 0)
blur = cv.blur(img, (5, 5))
cv.imshow("orign", img)
cv.imshow("blur", blur)
cv.waitKey(0)

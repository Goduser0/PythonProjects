import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


img = cv.imread("../../image/sunrise.png", 0)

dst = cv.equalizeHist(img)

cv.imshow("origin", img)
cv.imshow("result", dst)
cv.waitKey(0)

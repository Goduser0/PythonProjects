import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread("../../image/self.jpg", 0)

x = cv.Sobel(img, cv.CV_16S, 1, 0, ksize=-1)
y = cv.Sobel(img, cv.CV_16S, 0, 1, ksize=-1)

Scale_absX = cv.convertScaleAbs(x)
Scale_absY = cv.convertScaleAbs(y)

result = cv.addWeighted(Scale_absX, 0.5, Scale_absY, 0.5, 0)

cv.imshow("result_Schaar", result)
cv.waitKey(0)
cv.destroyAllWindows()

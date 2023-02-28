import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread("../../image/qin.jpg")

min = 25
max = 50

canny = cv.Canny(img, min, max)
cv.imshow("result_Canny", canny)
cv.waitKey(0)
cv.destroyAllWindows()

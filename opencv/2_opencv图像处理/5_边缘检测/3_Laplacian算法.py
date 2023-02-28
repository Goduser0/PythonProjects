import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread("../../image/self.jpg", 0)
result = cv.Laplacian(img, cv.CV_16S)
Scale_abs = cv.convertScaleAbs(result)

cv.imshow("result_Laplacian", Scale_abs)
cv.waitKey(0)
cv.destroyAllWindows()

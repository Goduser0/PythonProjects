import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

vango = cv.imread("../../image/vango1.jpg")
img_up1, img_down1 = vango, vango
for i in range(1, 3):
    img_up1 = cv.pyrUp(img_up1)
    img_down1 = cv.pyrDown(img_down1)
    cv.imshow("up"+str(i), img_up1)
    cv.waitKey(0)
    cv.imshow("down"+str(i), img_down1)
    cv.waitKey(0)

cv.destroyAllWindows()

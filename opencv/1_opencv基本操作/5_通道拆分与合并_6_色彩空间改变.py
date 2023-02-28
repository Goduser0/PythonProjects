import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread("../image/sunrise.png", 1)
b, g, r = cv.split(img)
plt.imshow(b, cmap=plt.cm.gray)
# plt.show()

img1 = cv.merge((r, g, b))
plt.imshow(img1)
# plt.show()

img2 = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
plt.imshow(img2, cmap=plt.cm.gray)
plt.show()

img3 = cv.cvtColor(img, cv.COLOR_BGR2HSV)
plt.imshow(img3, cmap=plt.cm.gray)
plt.show()

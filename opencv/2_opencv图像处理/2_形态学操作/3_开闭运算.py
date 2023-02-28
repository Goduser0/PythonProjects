import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

vango = cv.imread("../../image/girl.jpg", 1)

img2 = np.ones((10, 10), np.uint8)

img_open = cv.morphologyEx(vango, cv.MORPH_OPEN, img2)
img_close = cv.morphologyEx(vango, cv.MORPH_CLOSE, img2)

plt.imshow(img_open[:, :, ::-1])
plt.show()
plt.imshow(img_close[:, :, ::-1])
plt.show()

import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

img1 = cv.imread("../image/vango.jpg", 1)
img2 = cv.imread("../image/vango1.jpg", 1)

img3 = cv.addWeighted(img1, 0.3, img2, 0.7, 0)

plt.figure(figsize=(8, 8))
plt.imshow(img3[:, :, ::-1])
plt.show()

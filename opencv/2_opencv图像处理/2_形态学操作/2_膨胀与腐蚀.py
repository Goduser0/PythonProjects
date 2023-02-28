import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

img1 = np.ones((5, 5), np.uint8)
M = np.float32([[0, 0, 1, 0, 0], [0, 1, 1, 0, 0], [1, 1, 1, 1, 0], [0, 1, 1, 1, 0], [0, 1, 1, 1, 0]])
img1 = M*img1

vango = cv.imread("../../image/girl.jpg", 1)

img2 = np.ones((10, 10), np.uint8)

final1 = cv.erode(vango, img2)
final2 = cv.dilate(vango, img2)

plt.imshow(final1[:, :, ::-1])
plt.show()
plt.imshow(final2[:, :, ::-1])
plt.show()

import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

vango = cv.imread("../../image/vango1.jpg")
rows, cols = vango.shape[:2]

M = np.float32([[1, 0, 100], [0, 1, 50]])
res1 = cv.warpAffine(vango, M, (cols, rows))
plt.imshow(res1[:, :, ::-1])
plt.show()

M_rot = cv.getRotationMatrix2D((cols/2, rows/2), 45, 1)
res2 = cv.warpAffine(vango, M_rot, (cols, rows))
plt.imshow(res2[:, :, ::-1])
plt.show()

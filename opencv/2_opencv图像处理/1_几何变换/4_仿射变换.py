import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

vango = cv.imread("../../image/vango1.jpg")
rows, cols = vango.shape[:2]
plt.imshow(vango[:, :, ::-1])
plt.show()
# 不共线三点
pts1 = np.float32([[50, 50], [200, 50], [50, 200]])
pts2 = np.float32([[100, 100], [200, 50], [100, 250]])
# 获取仿射变换矩阵
M = cv.getAffineTransform(pts1, pts2)
# 仿射变换
img = cv.warpAffine(vango, M, [cols, rows])

plt.imshow(img[:, :, ::-1])
plt.show()

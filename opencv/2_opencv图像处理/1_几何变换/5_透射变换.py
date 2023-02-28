import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

vango = cv.imread("../../image/vango1.jpg")
rows, cols = vango.shape[:2]

# 任意3点不共线的四点
pts1 = np.float32([[56, 65], [368, 52], [28, 387], [389, 390]])
pts2 = np.float32([[100, 145], [300, 100], [80, 290], [310, 300]])
# 创建透射矩阵
T = cv.getPerspectiveTransform(pts1, pts2)
# 透射变换
img = cv.warpPerspective(vango, T, (cols, rows))
plt.imshow(img[:, :, ::-1])
plt.show()

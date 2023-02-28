import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


img = cv.imread("../../image/vango1.jpg", 0)
# 创建自适应均衡化对象
clahe = cv.createCLAHE(clipLimit=10.0, tileGridSize=(8, 8))
# 应用于图像
dst = clahe.apply(img)

cv.imshow("origin", img)
cv.imshow("result", dst)
cv.waitKey(0)

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

from pylab import *
mpl.rcParams['font.sans-serif'] = ['SimHei']

img = cv.imread('../../image/xyy.jpg', 0)
# 创建mask
mask = np.zeros(img.shape[:2], np.uint8)
mask[400:650, 200:500] = 255
# 用mask处理图像
masked_img = cv.bitwise_and(img, img, mask=mask)
# 处理后图像直方图
mask_hist = cv.calcHist([img], [0],  mask, [256], [1, 256])

fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(10, 8))
axes[0, 0].imshow(img, cmap=plt.cm.gray)
axes[0, 0].set_title("原图")
axes[0, 1].imshow(mask, cmap=plt.cm.gray)
axes[0, 1].set_title("mask")
axes[1, 0].imshow(masked_img, cmap=plt.cm.gray)
axes[1, 0].set_title("masked_img")
axes[1, 1].plot(mask_hist)
axes[1, 1].grid()
axes[1, 1].set_title("灰度直方图")
plt.show()


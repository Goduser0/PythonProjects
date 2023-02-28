import numpy as np
import cv2 as cv

img = cv.imread("../image/mnls.jpg", 0)
# 获取行、列、通道数
a = img.shape
b = img.size
c = img.dtype
d = img[100, 100]
print(a, '\n', b, '\n', c, '\n', d)

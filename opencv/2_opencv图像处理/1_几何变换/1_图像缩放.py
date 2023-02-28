import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

vango = cv.imread("../../image/vango1.jpg")
row, cols = vango.shape[:2]

res1 = cv.resize(vango, [2*row, 2*cols], interpolation=cv.INTER_CUBIC)
res2 = cv.resize(vango, None, fx=0.7, fy=0.5)

plt.imshow(res2[:, :, ::-1])
plt.show()

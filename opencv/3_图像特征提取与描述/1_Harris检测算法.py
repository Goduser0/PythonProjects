# Noel Stallworth
# TIME: 2022/1/10 23:55
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('../image/chessboard.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

gray = np.float32(gray)
dst = cv.cornerHarris(gray, 2, 3, 0.04)
print(dst)
img[dst > 0.001*dst.max()] = [0, 0, 255]
cv.imshow('Harris', img)
cv.waitKey(0)

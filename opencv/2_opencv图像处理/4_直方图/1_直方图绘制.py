import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img1 = cv.imread("../../image/sunrise.png", 0)
cv.imshow("img1", img1)
cv.waitKey(2)
hist = cv.calcHist([img1], [0], None, [256], [0, 255])

plt.figure(figsize=(6, 4), dpi=100)
plt.title('Hist')
plt.plot(hist)
plt.grid()
plt.show()

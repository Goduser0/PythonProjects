import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

img1 = cv.imread("chat record 1.png")
img2 = cv.imread("chat record 2.png")
img3 = cv.imread("chat record 3.png")
img4 = cv.imread("chat record 4.png")
img5 = cv.imread("chat record 5.png")
img6 = cv.imread("chat record 6.png")
img7 = cv.imread("chat record 7.png")
img8 = cv.imread("chat record 8.png")

height1, width1 = img1.shape[:2]
height2, width2 = img2.shape[:2]
height3, width3 = img3.shape[:2]
height4, width4 = img4.shape[:2]
height5, width5 = img5.shape[:2]
height6, width6 = img6.shape[:2]
height7, width7 = img7.shape[:2]
height8, width8 = img8.shape[:2]

height = height1 + height2 + height3 + height4 + height5 + height6 + height7 + height8
width = width1 + width2 + width3 + width4 + width5 + width6 + width7 + width8
result = np.ones((height, 1000, 3), np.uint8)

for a in range(height1):
    for b in range(width1):
        result[a, b] = img1[a, b]
for a in range(height2):
    for b in range(width2):
        result[height1+a, b] = img2[a, b]
for a in range(height3):
    for b in range(width3):
        result[height1+height2+a, b] = img3[a, b]
for a in range(height4):
    for b in range(width4):
        result[height1+height2+height3+a, b] = img4[a, b]
for a in range(height5):
    for b in range(width5):
        result[height1+height2+height3+height4+a, b] = img5[a, b]
for a in range(height6):
    for b in range(width6):
        result[height1+height2+height3+height4+height5+a, b] = img6[a, b]
for a in range(height7):
    for b in range(width7):
        result[height1+height2+height3+height4+height5+height6+a, b] = img7[a, b]
for a in range(height8):
    for b in range(width8):
        result[height1+height2+height3+height4+height5+height6+height7+a, b] = img8[a, b]

cv.imwrite("final1.png", result)
print("Done!!!")

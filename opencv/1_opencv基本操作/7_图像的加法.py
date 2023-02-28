import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

img1 = cv.imread("../image/vango.jpg", 1)
img2 = cv.imread("../image/vango1.jpg", 1)

img3 = cv.add(img1, img2)
img4 = img1+img2

fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(10, 8), dpi=100)
axes[0].imshow(img3[:, :, ::-1])
axes[0].set_title("cv")
axes[1].imshow(img4[:, :, ::-1])
axes[1].set_title("numpy")

plt.show()

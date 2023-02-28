import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
# 创建空白图像
img = np.zeros((512, 512, 3), np.uint8)
# 绘制图像
cv.line(img, (0, 0), (512, 512), (255, 0, 0), 8)
cv.rectangle(img, (256, 256), (512, 0), (0, 0, 255), -1)
cv.circle(img, (128+256, 128), 100, (0, 255, 0), 10)
font = cv.FONT_HERSHEY_DUPLEX
cv.putText(img, "Are you OK?", (10, 500), font, 1.2, (50, 200, 7), 1, cv.LINE_AA)

plt.imshow(img[:, :, ::-1])
plt.show()

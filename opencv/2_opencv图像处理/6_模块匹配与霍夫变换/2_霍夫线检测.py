import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread("../../image/l_c.jpg", 0)
img1 = cv.imread("../../image/l_c.jpg")
edges = cv.Canny(img, 100, 200)
# cv.imshow("edges", edges)
# cv.waitKey(0)

lines = cv.HoughLines(edges, 0.8, np.pi/180, 110)
print(lines)

for line in lines:
    rho, theta = line[0]
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = rho*a
    y0 = rho*b
    x1 = int(x0 + 1000 * (-b))
    y1 = int(y0 + 1000 * a)
    x2 = int(x0 - 1000 * (-b))
    y2 = int(y0 - 1000 * a)
    cv.line(img1, (x1, y1), (x2, y2), (0, 255, 0))

cv.imshow("result", img1)
cv.waitKey(0)

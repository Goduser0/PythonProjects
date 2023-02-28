import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

rab_I = cv.imread("../../image/num_I.jpg")
rab_T = cv.imread("../../image/num_T.jpg")

h, w, l = rab_T.shape
res = cv.matchTemplate(rab_I, rab_T, cv.TM_SQDIFF)
min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
print(min_val, max_val, min_loc, max_loc)

top_left = min_loc
bottom_right = (top_left[0] + w, top_left[1]+h)
cv.rectangle(rab_I, top_left, bottom_right, (0, 0, 255), 1)

cv.imshow("result", rab_I)
cv.waitKey(0)
cv.destroyAllWindows()

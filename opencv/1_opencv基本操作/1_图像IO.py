import cv2
# 图片读取并显示
from matplotlib import pyplot as plt

img = cv2.imread("../image/mnls.jpg", 1)
print(img.shape)
# cv2.imshow("Mona lisa", img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
#
# plt.imshow(img[:, :, ::-1])
# plt.title("Mona lisa"), plt.xticks(), plt.yticks()
# plt.show()
#
# # 灰度图
# img1 = cv2.imread("../image/mnls.jpg", 0)
# plt.imshow(img1, cmap=plt.cm.gray)
# plt.show()

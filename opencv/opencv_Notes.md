# 1. OpenCV简介



## 1.1 图像处理简介

### 1.1.1 基础概念

图：是物体反射或透射光的分布

像：是人的视觉系统所接受的图在人脑中所形版的印象或认识

模拟图像：连续图像

数字图像：离散图像

### 1.1.2 数字图像的表示

- 位数

  ```
  二进制编码，图像一般是8位数图像（一个像素点），灰度：0~255，0黑255白
  ```

- 图像分类

  ```
  二值图像、灰度图、彩色图
  ```



## 1.2 python 安装

package:

```python
numpy
matplotlib
opencv-python
opencv-contrib-python
```



## 1.3 OpenCV模块



# 2. OpenCV基本操作



## 2.1 图像的IO操作

### 2.1.1 读取图像

```python
img = cv.imread("1.jpg", 0)
```

- 读取方式：

  ```python
  cv.IMREAD*COLOR:彩色模式,不加载透明度（默认参数，1）
  cv.IMREAD*GRAYSCALE:灰度模式（0）
  cv.IMREAG_UNCHANGED:包括alpha通道，即透明度加载（-1）
  ```

- 路径不存在则返回None

### 2.1.2 显示图像

```python
cv.imshow('image', img)
# 为图像绘制留下时间，人为退出
cv.waitKey(0)
```

- 参数：

  ```python
  1.显示图像窗口名称，字符串类型
  2.要加载的图像
  ```

```python
# 在matplotlib中显示，需要通道翻转
from matplotlib import pyplot as plt
# imshow 负责处理图像
plt.imshow(img[:,:,::-1])
# show 负责显示图像
plt.show()
```

### 2.1.3 保存图像

```python
# 将img保存为1.png
cv.imwrite('1.png', img)
```



## 2.2 绘制几何图形

### 2.2.1 绘制直线

```python
cv.line(img, start, end, color, thickness)
```

### 2.2.2 绘制圆形

```python
cv.circle(img, centerpoint, r, color, thickness)
```

- thickness 为-1时，生成闭合图案并填充颜色

### 2.2.3 绘制矩形

```python
cv.rectangle(img, leftupper, rightdown, color, thickness)
```

### 2.2.4 添加文字

```python
cv.putText(img, text, station, font, fontsize, color, thickness, cv.LINE_AA)
```

- station：文本的放置位置



## 2.3 获取并修改指定像素点

对于BGR图像，返回像素点数组，对于灰度图像，仅返回强度值。

```python
import numpy as np
import cv2 as cv

img = cv.imread("image/sunrise.png", 1)
px = img[100, 100]
px_B = px[0]

image1 = np.zeros((100, 100, 3), np.uint8)
image1[50, 50] = (255, 255, 255)
```



## 2.4 获取图像的属性

行数列数通道数，图像数据类型，像素数等

```python
# 形状
img.shape
# 图像大小(像素数)
img.size
# 数据类型（像素编码类型）
img.dtype
```



## 2.5 图像通道拆分与合并

```python
# 拆分
b, g, r = cv.split(img)
# 合并
img = cv.merge((b, g, r))
```



## 2.6 色彩空间的改变

最常见的是：

BGR <-> Gray 

BGR <-> HSV

```python
cv.cvtColor(input_image, flag)
# flag: cv.COLOR_BGR2GARY: BGR -> Gary
# flag: cv.COLOR_BGR2HSV: BGR -> HSV
```



## 2.7 加法运算

- 要求两图像有相同的大小类型，或者第二个图像为标量值

```python
# OpenCV法：（饱和操作：250+10=260 -> 255）
cv.add(image1, image2)
# numpy法：（模运算：250+10=260 -> 260%256 -> 4）
```



## 2.8 图像的混合

- 实际为不同全重的相加

```python
# final = img1*a1 + img2*a2 + b
cv2.addWeighted(img1, a1, img2, a2, b)
```



# 3. OpenCV图像处理



## 3.1 几何变换

### 3.1.1 图像缩放

```python
cv2.resize(src, dsize, fx=0, fy=0, interpolation=cv2.INTER_LINEAR)
# dsize:绝对尺寸
# fx,fy:相对尺寸，设置比例因子，同时将dsize设为None
# interpolation:选择插值方法 
#				cv2.INTER_LINEAR - 双线性插值
#   			cv2.INTER_NEAREST - 最近邻插值
#        		cv2.INTER_AREA - 像素区域重采样（默认）
#            	cv2.INTER_CUBIC - 双三次插值
```

### 3.1.2 图像平移

```python
M = np.float32([1, 0, x],[0, 1, y])
img = cv.warpAffine(img, M, dsize)
# img:输入图像
# M:2*3移动矩阵
# dsize:输出图像大小，形式为（width， height）
```

对于M矩阵：
$$
(x,y) -> (x+t_{x}, y+t_{x})\\
M = \begin{bmatrix}
1 & 0 & t_{x} \\	
0 & 1 & t_{y}
\end{bmatrix}
$$

### 3.1.3 图像旋转

- 获取旋转矩阵

  ```python
  M_rot = cv2.getRotation2D(center, angle, scale)
  # center: 旋转中心
  # angle: 旋转角度(°)
  # scale: 缩放比例
  ```

- 变换

  ```
  img = cv.warpAffine(img, M_rot, dsize)
  ```

### 3.1.4 仿射变换

- 仿射矩阵
  $$
  M = \begin{bmatrix}
  A & B
  \end{bmatrix}
  =
  \begin{bmatrix}
  A_{00} & A_{01} & B_{0} \\	
  A_{10} & A_{11} & B_{1}
  \end{bmatrix}
  $$
  其中A为线性变换矩阵，B为平移矩阵
  $$
  A = \begin{bmatrix}
  A_{00} & A_{01}\\	
  A_{10} & A_{11}
  \end{bmatrix}
  ,
  B = \begin{bmatrix}
  B_{0}\\	
  B_{1}
  \end{bmatrix}
  $$

  
  
  ```python
  # 不共线三点
  pts1 = np.float32([[50, 50], [200, 50], [50, 200]])
  pts2 = np.float32([[100, 100], [200, 50], [100, 250]])
  # 获取仿射变换矩阵
  M = cv.getAffineTransform(pts1, pts2)
  # 仿射变换
  img = cv.warpAffine(vango, M, [cols, rows])
  ```

### 3.1.5 透射变换

- 透射矩阵
  $$
  T = \begin{bmatrix}
  a_{00}&a_{01}&a_{02}\\
  a_{10}&a_{11}&a_{12}\\
  a_{20}&a_{21}&a_{22}
  \end{bmatrix}
  =
  \begin{bmatrix}
  T_{1}&T_{2}\\
  T_{3}&a_{22}
  \end{bmatrix}\\
  其中:\\
  T_{1}:线性变换\\T_{2}:平移变换\\T_{3}:透射变换\\a_{22}:一般设为1
  $$

- 透射变换

  ```python
  # 任意3点不共线的四点
  pts1 = np.float32([[56, 65], [368, 52], [28, 387], [389, 390]])
  pts2 = np.float32([[100, 145], [300, 100], [80, 290], [310, 300]])
  # 创建透射矩阵
  T = cv.getPerspectiveTransform(pts1, pts2)
  # 透射变换
  img = cv.warpPerspective(vango, T, (cols, rows))
  ```

### 3.1.6 图像金字塔

```python
#上采样
cv.pyrUp(img)
#下采样
cv.pyrDown(img)
```



## 3.2 形态学操作

### 3.2.1 连通性

- 图像最小单位：像素

- 每个像素的周围有8个邻接像素，常见邻接关系：
  - 4邻接
  - D邻接
  - 8邻接

![image-20211215135713732](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20211215135713732.png)
$$
4邻接:N_{4}(p)\\
D邻接:N_{D}(p)\\
8邻接:N_{8}(p)
$$

- 连通性：

  - 两个像素连通的必要条件：

    1. 两个像素的位置是否相邻
    2. 两个像素的灰度值是否满足特定的相似性准则

  - 连通性分类：

    - 4连通

    - 8连通

    - m连通：
      $$
      对于具有值V的像素p和q,如果:\\
      1.q在集合N_{4}(p)中，或者\\
      2.q在集合N_{D}(p)中，并且N_{4}(p)和N_{4}(p)的交集为空（没有值V的像素）\\
      则称两个像素m连通，即4连通和D连通的混合连通
      $$

### 3.2.2 腐蚀与膨胀

腐蚀和膨胀都是针对白色部分（高亮部分）而言的。

膨胀就是使图像中高亮部分扩张；腐蚀是原图中的高亮区域被蚕食。膨胀是求局部最大值的操作，腐蚀是求局部最小值的操作。

- 腐蚀：用一个结构元素扫描图像中的每一个像素，用结构元素中的每一个像素与其覆盖的像素做“与"操作，如果都为1，则该像素为1，否则为0。腐蚀的作用是消除物体边界点，使目标缩小，可以消除小于结构元素的噪声点。

  ```python
  cv.erode(img, kernel, iterations)
  # img:要处理的图像
  # kernel:核结构
  # iterations:腐蚀的次数，默认为1
  ```

- 膨胀：用一个结构元素扫描图像中的每一个像素，用结构元素中的每一个像素与其覆盖的像素做”与"操作，如果都为0，则该像素为0，否则为1。作用是将与物体接触的所有背景点合并到物体中，使目标增大，可添补目标中的孔洞。

  ```python
  cv.dilate(img, kernel, iterations)
  # img:要处理的图像
  # kernel:核结构
  # iterations:腐蚀的次数，默认为1
  ```

  

### 3.2.3 开闭运算

开闭运算不可逆

开运算：先腐蚀后膨胀，作用：分离物体，消除小区域，特点：消除噪声，去除小的干扰块，而不影响原来的图像

闭运算：先膨胀后腐蚀，作用：消除闭合物体里面的孔洞，特点：可以填充闭合区域

```python
cv.morphologyEx(img, op, kernel)
# img:要处理的图像
# op:处理方式 开运算：cv.MORPH_OPEN 闭运算：cv.MORPH_CLOSE
# kernel:核结构
```

### 3.2.4 礼帽与黑帽

- 礼帽运算

  原图像与“开运算”的结果图之差
  礼帽运算用来分离比邻近点亮一些的斑块

- 黑帽运算

  “闭运算”的结果图与原图像之差

  黑帽运算用来分离比邻近点暗一些的斑块

```python
cv.morphologyEx(img, op, kernel)
# img:要处理的图像
# op:处理方式 礼帽运算：cv.MORPH_TOPHAT 黑帽运算：cv.MORPH_BLACKHAT
# kernel:核结构
```



## 3.3 图像平滑

### 3.3.1 图像噪声

- 椒盐噪声：也称脉冲噪声，图像中随机出现的白点或者黑点

- 高斯噪声：灰度值符合高斯分布的噪声

  高斯分布：二维正态分布

### 3.3.2 图像平滑

图像平滑：去除高频信息、保留低频信息

低通滤波：去除噪声（高频），实现图像平滑

常见滤波器：均值滤波、高斯滤波、中值滤波、双边滤波

#### 3.3.2.1均值滤波

特点：算法简单，计算快；去噪的同时去除很多细节的部分，使得图像变模糊

```python
cv.blur(src, ksize, anchor, borderType)
# src:输入图像
# ksize:卷积核的大小
# anchor:默认值为(-1, -1)，表示核中心
# borderType:边界类型
```

#### 3.3.2.2高斯滤波

特点：去除高斯噪声十分有效

- 处理流程：
  1. 确定权重矩阵，以像素中心为高斯分布中心，确定领域权重
  2. 高斯模糊：权重矩阵与各对应像素相乘再相加，得到像素中心的高斯模糊值
  3. 对每个像素点进行高斯模糊，如果为RGB三通道，则各分量分别进行高斯平滑

```python
cv2.GaussianBlur(src, ksize, sigmaX, sigmaY, borderType)
# src:输入图像
# ksize:卷积核大小，宽度和高度应都为奇数且可以不同
# sigmaX：水平方向的标准差
# sigmaY：垂直方向的标准差，默认为0，表示与sigmaX相等
# borderType：填充边界类型
```

#### 3.3.2.3中值滤波

典型的非线性滤波技术，基本思想是用像素点邻域灰度值的中值来代替该像素点的灰度值

特点：中值滤波对椒盐噪声来说尤其有用，因为它不依赖于邻域内那些与典型值差别很大的值

```python
cv.medianBlur(src, ksize)
# src:输入图像
# ksize:卷积核大小
```



## 3.4 直方图

### 3.4.1 灰度直方图

图像直方图（Image Histogram）：表示数字图像中亮度分布的直方图，左侧为较暗的区域，右侧为较亮的区域

直方图术语：

```
dims：需要统计的特征数目（维度）
bins：每个特征空间子区段的数目
range：需要统计的特征取值范围
```

直方图意义：

- 直方图是图像中像素强度分布的图形表达方式
- 它统计了每一个强度值所具有的像素个数
- 不同的图像的直方图可能是相同的

### 3.4.2 直方图的计算与绘制

```python
cv2.calcHist(images, channels, mask, histSize, ranges[, hist[, accumulate]])
# images:原图像，传入时用[]括起来
# channels:如果输入灰度图，则为[0]；输入彩色图，[0]，[1]，[2]分别代表B，G，R
# mask:掩模图像。统计整幅图像则为None，如果只统计部分区域，则制作掩模图像并输入
# histSize:bins的数目，也要用[]，例如：[256]
# ranges:像素值的范围，通常为[0, 256]
```

### 3.4.3 掩膜的应用

掩膜：用选定的图像、图形或物体，对要处理的图像进行遮挡，用来控制图像处理的区域

掩膜选用二维二进制矩阵，1值的区域被处理，0值的区域被屏蔽

主要用途：

- 提取感兴趣区域
- 屏蔽作用
- 结构特征提取
- 特殊形状图像制作

```python
img = cv.imread('../../image/xyy.jpg', 0)
# 创建mask
mask = np.zeros(img.shape[:2], np.uint8)
mask[400:650, 200:500] = 255
# 用mask处理图像
masked_img = cv.bitwise_and(img, img, mask=mask)
# 处理后图像直方图
mask_hist = cv.calcHist([img], [0],  mask, [256], [1, 256])
```

### 3.4.4 直方图均衡化

“直方图均衡化”：把原始图像的灰度直方图从比较集中的某个灰度区间变成在更广泛灰度范围内的分布；对图像进行非线性拉伸，重新分

配图像像素值，使一定灰度范围内的像素数量大致相同。

目的：提高整体对比度，在曝光过度或不足的图像中可以更好的突出细节

```python
dst = cv.equalizeHist(img)
# dst:均衡化后的图像
# img:灰度图像
```

### 3.4.5 自适应的直方图均衡化

全局均衡易丢失部分特征

方法：

- 将图像分块，分为许多“tiles”，默认大小8*8，对每小块均衡化
- 限幅

```python
cv.createCLAHE(clipLimit, tileGridSize)
# clipLimit:对比度限制，默认40
# tileGridSize:分块大小，默认8*8
```

```python
# example:
img = cv.imread("../../image/vango1.jpg", 0)
# 创建自适应均衡化对象
cl = cv.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
# 应用于图像
dst = cl.apply(img)
```



## 3.5 边缘检测

### 3.5.1 边缘检测简介

目的：标识数字图像中亮度变化明显的点

分类：绝大部分可分为：

- 基于搜索：通过寻找图像一阶导数中的最大值来检测边界，然后利用计算结果估计边缘的局部方向，通常采用梯度的方向，并利用此方向找到局部梯度模的最大值，代表算法是Sobel算子和Scharr算子。

![image-20211220161716601](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20211220161716601.png)

- 基于零穿越：通过寻找图像二阶导数零点穿越来寻找边界，代表算法是Laplacian算子。

![image-20211220161826968](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20211220161826968.png)

### 3.5.2 Sobel检测算法及Scharr算法

Sobel算子是高斯平滑与微分操作的结合体，所以其抗噪声能力很强，用途较多

特点：效率较高，对边缘的检测性以及细纹理处理能力一般

像素求导：
$$
f'(x)=f(x+1)-f(x)\\
f'(x)=f(x)-f(x-1)\\
f'(x)=\frac{f(x+1)-f(x-1)}{2}
$$
对与待处理的图像I，在两个方向上求导：

- 水平变化：I与奇数大小的的模板进行卷积，若模板大小为3：
  $$
  G_{x}=\begin{bmatrix}-1&0&+1\\-2&0&+2\\-1&0&+1\end{bmatrix}*I
  $$

- 垂直变化：I与奇数大小的的模板进行卷积，若模板大小为3：

$$
G_{y}=\begin{bmatrix}-1&-2&-1\\0&0&0\\+1&+2&+1\end{bmatrix}*I
$$

对于图像上每一点：
$$
G=\sqrt{G_x^2+G_y^2}
$$
统计极大值所在的位置，则为图像的边缘

此时，内核大小为3的Sobel算子可能误差较大，故用Scharr函数改进，但仅作用于大小为3的内核，计算速度不变，但结果却更加准确:
$$
G_{x}=\begin{bmatrix}-3&0&+3\\-10&0&+10\\-3&0&+3\end{bmatrix}*I\\\\
G_{y}=\begin{bmatrix}-3&-10&-3\\0&0&0\\+3&+10&+3\end{bmatrix}*I
$$

- sobel边缘检测：

  ```python
  Sobel_x_or_y = cv2.Sobel(src, ddepth, dx, dy, dst, ksize, scale, delta, borderType)
  # src:传入图像
  # ddepth:图像的深度
  # dx,dy:求导阶数，取0（不求导）/1（1阶导数）
  # ksize:sobel算子大小，必须为奇数，默认为3
  # scale:缩放导数的比例系数，默认没有
  # borderType:边界类型，默认为cv2.BORDER_DEFAULT
  #!!! 算子求导之后会有负值，大于255的数，而原图像是uint8，故会产生截断。因此，需使用16位有符号数据类型，即cv2.CV_16S。处理完之后，需用cv2.convertScaleAbs()函数转回值uint8来显示图像。
  #!!! Sobel算子是在两个方向计算的，最后需要调用cv2.addWeighted()函数将其结合
  # example:
  x = cv.Sobel(img, cv.CV_16S, 1, 0)
  y = cv.Sobel(img, cv.CV_16S, 0, 1)
  Scale_absX = cv.convertScaleAbs(x)
  Scale_absY = cv.convertScaleAbs(y)
  result = cv.addWeighted(Scale_absX, 0.5, Scale_absY, 0.5, 0)
  ```

  

- Scharr算法

  ```
  将Sobel算子中的ksize设为-1即可
  ```

### 3.5.3 Laplacian算法

利用二阶导数：
$$
\varDelta src = \frac{\part ^2src}{\part x^2}+ \frac{\part ^2src}{\part y^2}
$$
对于不连续函数的二阶导数：
$$
f''(x)=f'(x+1)-f'(x)=f(x+1)-f(x)-[f(x)-f(x-1)]=f(x+1)+f(x-1)-2f(x)
$$
则卷积核为：
$$
kernel = \begin{bmatrix}0&1&0\\1&-4&1\\0&1&0\end{bmatrix}
$$


```python
laplacian = cv2.Laplacian(src, ddpth, dst, ksize, scale, delta, borderType)
# src:传入图像
# ddepth:图像的深度，-1代表与原图像相同的深度，目标图像的深度必须大于等于原图像的深度
# ksize:算子大小，必须为1，3，5，7
# scale:缩放导数的比例系数，默认没有
# borderType:边界类型，默认为cv2.BORDER_DEFAULT
#!!! 算子求导之后会有负值，大于255的数，而原图像是uint8，故会产生截断。因此，需使用16位有符号数据类型，即cv2.CV_16S。处理完之后，需用cv2.convertScaleAbs()函数转回值uint8来显示图像。
# example 
img = cv.imread("../../image/self.jpg", 0)
result = cv.Laplacian(img, cv.CV_16S)
Scale_abs = cv.convertScaleAbs(result)
```



### 3.5.4 Canny边缘检测算法

算法步骤：

1. 噪声去除

   ```
   边缘检测易受噪声影响，先使用5*5高斯滤波器去除噪声
   ```

2. 计算图像梯度

   ```
   应用Sobel算法计算水平和竖直方向的一阶导数，并以此得到边界的梯度和方向
   ```

   $$
   Edge\_Gradient(G) = \sqrt{ G_x^2+G_y^2}\\
   Angle(\theta) = tan^{-1}\bigg(\frac{G_y}{G_x}\bigg)
   $$

   ```
   如果某个像素点是边缘，则其梯度方向总是垂直于边缘。梯度方向（对与一个像素点）被归为四类：垂直，水平，两个对角线方向
   ```

3. 非极大值抑制

   ```
   在获得梯度的方向和大小之后，对整幅图像进行扫描，去除那些非边界上的点。对每一个像素进行检查，看这个点的梯度是不是周围具有相同梯度方向的点中最大的
   ```

   ![image-20211221105026047](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20211221105026047.png)

   ```
   A点位于图像的边缘，在其梯度变化方向，选择像素点B和c，用来检验A点的梯度是否为极大值，若为极大值，则进行保留，否则A点被抑制,最终的结果是具有“细边”的二进制图像。
   ```

4. 滞后阈值

   ```
   现在要确定真正的边界。我们设置两个阈值: minVal和 maxVal。当图像的灰度梯度高于maxVal时被认为是真的边界，低于minVal 的边界会被抛弃。如果介于两者之间的话，就要看这个点是否与某个被确定为真正的边界点相连，如果是就认为它也是边界点，如果不是就抛弃。
   ```

Canny边缘检测：

```python
canny = cv2.Canny(image, threshold1, threshold2)
# image:灰度图
# threshold1:minval，较小的阈值将间断的边缘连接起来
# threshold2:maxval，较大的阈值检测图像中明显的边缘
```



## 3.6 模板匹配&霍夫变换

### 3.6.1 模板匹配

- 原理：在给定的图像中查找和模板最相似的区域，输入包括模板（T）和图片（I）；任务思路就是按滑窗的思路不断的移动模板图片，计算其与图像中对应区域的匹配度，最总将匹配度最高的区域输出
- 如果输入图像的大小（W×H），模板大小（w×h)，将相似结果保存在结果矩阵（R）中，则R的大小为（W - w + 1, H - h + 1）

```python
# 获取匹配结果矩阵（T）
res = cv.matchTemplate(img, template, method)
# method:模板匹配方法：
# 1.平方差匹配（CV_TM_SQDIFF）：最好的匹配是0，相差越大，匹配的值越大
# 2.相关匹配（CV_TM_CCORR）：数值越大表示越匹配
# 3.相关系数匹配（CV_TM_CCOEFF）：1表示完美匹配，-1表示最差的匹配

# 利用结果矩阵查找最大最小值所在的位置
min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
# min_val:最小匹配值
# max_val:最大匹配值
# min_loc:最小匹配值所在位置
# max_loc:最大匹配值所在位置
```

模板匹配不适用于尺度变换，视角变换后的图像，这时需要使用关键点匹配算法，例如SIFT算法和SURF等。主要的思路是首先通过关键点检测算法获取模板和测试图片中的关键点﹔然后使用关键点匹配算法处理即可。

### 3.6.2 霍夫变换

常用来提取图像中的直线和圆等几何图形

#### 3.6.2.1 原理

平面中的一条直线在霍夫变换之后为**霍夫空间**中的一点，两者一一对应<img src="C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20211221145118334.png" alt="image-20211221145118334" style="zoom:80%;" />

​		同样，笛卡尔坐标系中两点对应两直线的交点

<img src="C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20211221145417900.png" alt="image-20211221145417900" style="zoom:80%;" />	

​		如果在笛卡尔坐标系中的点共线，则这些点在霍夫空间中所对应的直线交于一点

​	<img src="C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20211221145713787.png" alt="image-20211221145713787" style="zoom:80%;" />

​		我们选择尽可能多的直线汇成的点，即笛卡尔坐标系中的直线。

​		为了避免斜率不存在的直线，选用极坐标表示：

​	<img src="C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20211221150054912.png" alt="image-20211221150054912" style="zoom:80%;" />

#### 3.6.2.2 实现流程

- 创建一个累加器，即二维数组：

  <img src="C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20211221150538667.png" alt="image-20211221150538667" style="zoom:80%;" />

  该数组的大小决定了结果的准确性，若希望角度的精度为1度，那θ就需要180列。对于ρ，最大值为图片对角线的距离，如果希望精度达到像素级别，行数应该与图像的对角线的距离相等。
  1. 取直线上的第一个点(x, y)，将其带入直线在极坐标中的公式中，然后遍历θ的取值:0，1，2，..180，分别求出对应的ρ值，如果这个数值在上述累加器中存在相应的位置，则在该位置上加1
  2. 取直线上的第二个点，重复上述步骤，更新累加器中的值。对图像中的直线上的每个点都执行以上步骤，每次更新累加器中的值。
  3. 搜索累加器中的最大值，并找到其对应的(ρ,θ)，就可将图像中的直线表示出来。

#### 3.6.2.3 霍夫线检测

```python
cv.HoughLines(img, rho, theta, threshold)
# img: 二值化图像
# rho,theta:ρ和θ的精确度
# thres:阈值，只有累加器中的值高于该阈值时才被认为是直线
```

#### 3.6.2.4 霍夫圆检测

霍夫梯度法：第一阶段检测圆心，第二阶段利用圆心推导出圆半径。

- 圆心检测：圆心是圆周法线的交汇处，设置一个阈值，在某点的相交的直线的条数大于这个阈值就认为该交汇点为圆心
- 圆半径检测：圆心到圆周上的距离（半径）是相同的，确定一个阈值，只要相同距离的数量大于该阈值,就认为该距离是该圆心的半径

```python
circles = cv.HoughCircles(image, method, dp, minDist, param1=100, param2=100, minRadius=0, maxRadius=1)
# image:输入灰度图像
# method:检测算法，CV_HOUGH_GRADIENT（霍夫梯度法）
# dp:霍夫空间的分辨率，dp=1表示霍夫空间与输入图像空间大小一致，dp=2表示霍夫空间为输入图像空间的一半，以此类推
# minDist:圆心间最小的距离
# param1:边缘检测时使用Canny算子的高阈值，低阈值为高阈值的一半
# param2:检测圆心和确定半径时所共有的阈值
# minRadius,maxRadius:所检测圆的半径最小值和最大值
# 返回圆向量，圆心横坐标，圆心纵坐标，圆半径
# 霍夫圆检测对噪声比较敏感，所以首先对图像进行中值滤波
```



# 4. 图像特征提取与描述



## 4.1 角点特征

适于被追踪、容易被比较---->角点，斑点

特征检测：找到图像中的特征

特征描述：对特征及其周围的区域进行描述



## 4.2 Harris&Shi-Tomas算法

### 4.2.1 Harris角点检测

#### 4.2.1.1 Harris角点检测原理：

![image-20220110150845660](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20220110150845660.png)

数学形式：
$$
E(u,v)=\sum_{x,y}(x,y)[I(x+u,y+v)-I(x,y)]^2\\
=\sum_{x,y}[I(x,y)+I_xu+I_yv-I(x,y)]^2\\
=\sum_{x,y}[I_x^2u^2+2I_xI_yuv+I_y^2v^2]\\
=\sum_{x,y}w(x,y)\begin{bmatrix}u&v\end{bmatrix}\begin{bmatrix}I_x^2&I_xI_y\\I_xI_y&I_y^2\end{bmatrix}\begin{bmatrix}u\\v\end{bmatrix}\\
=\begin{bmatrix}u&v\end{bmatrix}\sum_{x,y}w(x,y)\begin{bmatrix}I_x^2&I_xI_y\\I_xI_y&I_y^2\end{bmatrix}\begin{bmatrix}u\\v\end{bmatrix}\\
=\begin{bmatrix}u&v\end{bmatrix}M\begin{bmatrix}u\\v\end{bmatrix}\\
I(x,y):局部窗口图像灰度\\
I(x+u,y+v):平移后的图像灰度\\
w(x,y):窗口函数
$$
窗口函数：矩形函数与高斯函数

![image-20220110151553022](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20220110151553022.png)
$$
M是I_x和I_y的二次项系数，可以表示为椭圆的形状，椭圆的长短半轴由M的特征值\lambda_1和\lambda_2决定，方向由特征矢量决定
$$
![image-20220110153448172](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20220110153448172.png)



![image-20220110153529633](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20220110153529633.png)

Harris计算角点响应值R来判断：
$$
R=detM-\alpha(traceM)^2
\\detM=\lambda_1\lambda_2
\\traceM=\lambda_1+\lambda_2
$$
![image-20220110153931453](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20220110153931453.png)



#### 4.2.1.2 Harris角点检测代码实现

```python
dst = cv.cornerHarris(src, blockSize, ksize, k)
# img:数据类型为float32的输入图像
# blockSize:考虑的邻域大小
# ksize:sobel求导所用的核大小
# k:角点检测方程的自由参数，为[0.04, 0.06]
```

### 4.2.2 Shi-Tomas角点检测

#### 4.2.2.1 Shi-Tomas角点检测原理

角点响应值R：
$$
R=min(\lambda_1,\lambda_2)\\
\lambda_1和\lambda_2都大于阈值时才被认为是角点
$$
![image-20220110161648174](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20220110161648174.png)



#### 4.2.2.2 Shi-Tomas角点检测代码实现

```python
corners = cv2.goodFeaturesToTrack(image, maxcorners, qualityLevel, minDistance)
# 参数
# image:输入灰度图像
# maxCorners:获取的角点数
# qualityLevel:此参数指出最低可接受的角点质量水平，在[0,1]之间
# minDistance:角点间最小的欧式距离，避免得到相邻的特征点
# 返回
# corners:搜索到的角点
```





## 4.3 SIFT/SURF算法

### 4.3.1 简介

Harris&Tomas角点检测算法具有旋转不变性，但不具有尺度不变性

SIFT:  尺度不变特征变换

SIFT算法：在不同的尺度空间上查找关键点（特征点），并计算出关键点的方向

步骤：

1. 尺度空间检测
2. 关键点定位
3. 关键点方向确定
4. 关键点描述

### 4.3.2 尺度空间机制检测

使用尺度空间滤波器

高斯核是唯一可以产生多尺度空间的核函数
$$
一个图像的尺度空间L(x,y,\sigma),定义为原始图像I(x,y)与一个可变尺度的二维高斯函数G(x,y,\sigma)的卷积运算即：
\\L(x,y,\sigma)=G(x,y,\sigma)*I(x,y)
\\其中:
\\G(x,y,\sigma)=\frac{1}{2\pi\sigma^2}e^\frac{x^2+y^2}{2\sigma^2}
\\\sigma为尺度空间因子
\\实际应用中只计算(6\sigma+1)*(6\sigma+1)的高斯卷积核即可
$$

### 4.3.3 SURF算法

是SIFT算法的改进

### 4.3.4 代码实现

1. 实例化sift

   ```python
   sift = cv.xfeature2d.SIFT_create()
   ```

2. 检测关键点并计算

   ```python
   kp, des = sift.detectAndCompute(gray, None)
   # gray:进行关键点检测的灰度图像
   # kp:关键点信息，包括位置、尺度、方向信息
   # des:关键点描述符，每个关键点对应128个梯度信息的特征向量
   ```

3. 关键点检测结果绘制

   ```python
   cv.drawKeypoints(image, keypoints, outputimage, color, flags)
   # image:原始图像
   # ketpoints:关键点信息
   # outputimage:输出图片
   # color:画笔颜色设置
   # flags:绘图功能标识符
   #	1.cv2.DRAW_MATCHES_FLAGS_DEFAULT:
   # 	2.cv2.DRAW_MATCHES_FLAGS_DRAW_OVER_OUTMG:
   # 	3.cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS:
   # 	4.cv2.DRAW_MATCHES_FLAGS_NOT_DRAW_SINGLE_POINTS:
   ```

4. 

   ```python
   
   ```



## 4.4 Fast和ORB算法

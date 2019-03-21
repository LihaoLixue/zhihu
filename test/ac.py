import cv2
img = cv2.imread("D:\\WorkerCode\\zhihu\\test\\test.png")
# 转灰度图片
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

ret, binary = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)

# 轮廓检测
_ ,contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

# 新打开一个图片，我这里这张图片是一张纯白图片
newImg = cv2.imread("E:\\fort.bmp")
newImg = cv2.resize(newImg, (300,300))

# 画图
cv2.drawContours(newImg, contours, -1, (0,0,0), 3)

# 展示
cv2.imshow("img", newImg)
cv2.waitKey(0)
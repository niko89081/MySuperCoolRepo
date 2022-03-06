import cv2 as cv
import numpy as np

img = cv.imread("test.jpg")

height, width, uselessvalue = img.shape

pts1 = np.float32([[525,200], [1150, 75], [1150, 450], [525, 525]])
pts2 = np.float32([[2025, 1500], [2500, 1775], [2025, 2250], [1750, 1775]])

matrix = cv.getPerspectiveTransform(pts1, pts2)
result = cv.warpPerspective(img, matrix, (width+ 2000, height + 2750))

gray = cv.cvtColor(result, cv.COLOR_BGR2GRAY)
blur = cv.blur(gray, (3, 3))

circles = cv.HoughCircles(blur, cv.HOUGH_GRADIENT, 1, 100101, minRadius=230, maxRadius=250)

if circles is not None:
    circles = np.round(circles[0, :]).astype("int")
    for (x, y, r) in circles:
        cv.circle(result, (x, y), r, (0, 255, 0), 10)
        cv.circle(result, (x, y), 5, (0, 255, 0), -1)
uselessValueNeverUsedAnywhere, matrix = cv.invert(matrix)
result = cv.warpPerspective(result, matrix, (width, height))

cv.imshow('yoyoyoyoyoyo', result)

cv.waitKey(0)

cv.destroyAllWindows()

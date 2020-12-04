import cv2
import numpy as np
import math

def translate(image, x, y):
    M = np.float32([[1, 0, x], [0, 1, y]])
    shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
    return shifted
def rotate(image, angle, center = None, scale = 1.0):
    (h, w) = image.shape[:2]
    if center is None:
        center = (w / 2, h / 2)
    M = cv2.getRotationMatrix2D(center, angle, scale)
    rotated = cv2.warpAffine(image, M, (w, h))
    return rotated
def resize(image, width = None, height = None, inter = cv2.INTER_AREA):
    dim = None
    (h, w) = image.shape[:2]
    if width is None and height is None:
        return image
    if width is None:
        r = height / float(h)
        dim = (int(w * r), height)
    if height is None:
        r = width / float(w)
        dim = (width, int(h * r))
    if width and height:
        dim = (width, height)
    resized = cv2.resize(image, dim, interpolation = inter)
    return resized
def flip(image, direction):
    if direction == "h":
        flipped = cv2.flip(image, 1)
    elif direction == "v":
        flipped = cv2.flip(image, 0)
    else:
        # both horizontally and vertically
        flipped = cv2.flip(image, -1)
    return flipped
img = cv2.imread('cat.jpg')
#shifted = rotate(img, 30, center = None, scale = 1.0)
#旋转（图片，角度，中心，规格）
shifted = translate(img, 1, 1)
#平移（图片，x，y）
#shifted = resize(img,500,500);
#cv2.INTER_NEAREST;cv2.INTER_LINEAR;cv2.INTER_AREA;cv2.INTER_CUBIC;cv2.INTER_LANCZOS4
#缩放（图片，长，宽，方法）
#shifted = flip(img,"h")
#翻转（图片，方法）"h"水平翻转"v"垂直翻转
cv2.imwrite('cat1.jpg', shifted)
img1 = cv2.imread('cat1.jpg')
cv2.imshow('cat', img)
cv2.imshow('new_cat', img1)
cv2.waitKey(0)

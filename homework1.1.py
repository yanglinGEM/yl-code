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
def isometric(image, x, y, theta, center = None):
    theta = math.radians(-1 * theta)
    (h, w) = image.shape[:2]
    if center is None:
        cx = int(w/2)
        cy = int(h/2)
    else:
        cx = 0
        cy = 0
    M = np.float32([
        [math.cos(theta), -math.sin(theta), (1-math.cos(theta))*cx + math.sin(theta)*cy+x],
        [math.sin(theta), math.cos(theta), -math.sin(theta)*cx + (1-math.cos(theta))*cy+y]])
    isometric = cv2.warpAffine(image, M, (w, h))
    return isometric
def similar(image, x, y, theta, center = None, scale = 1.0):
    theta = math.radians(-1 * theta)
    (h, w) = image.shape[:2]
    if center is None:
        cx = int(w/2)
        cy = int(h/2)
    else:
        cx = 0
        cy = 0
    M = np.float32([
        [scale*math.cos(theta), -1*scale*math.sin(theta), scale*(1-math.cos(theta))*cx + scale*math.sin(theta)*cy+x],
        [scale*math.sin(theta), scale*math.cos(theta), -scale*math.sin(theta)*cx + scale*(1-math.cos(theta))*cy+y]])
    similar = cv2.warpAffine(image, M, (w, h))
    return similar
def affine(image, x, y, a11, a12, a21, a22):
    (h, w) = image.shape[:2]
    M = np.float32([
        [a11, a21, x],
        [a12, a22, y]])
    affine = cv2.warpAffine(image, M, (w, h))
    return affine
def projection(image, a11, a12, a13, a21, a22, a23, a31, a32, a33):
    (h, w) = image.shape[:2]
    M = np.float32([
        [a11, a21, a31],
        [a12, a22, a32],
        [a13, a23, a33]])
    projection = cv2.warpAffine(image, M, (w, h))
    return projection
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
#shifted = translate(img, 30, 50)
#平移（图片，x，y）
#shifted = rotate(img, 90, center = None, scale = 1.0)
#旋转（图片，角度，中心，规格）
#shifted = isometric(img, 30, 50, 30, center = None)
#欧式（图片，x，y，角度，中心）
#shifted = similar(img, 30, 50, 30, center = None, scale = 0.5)
#相似（图片，x，y，角度，中心，规格）
shifted = affine(img, 30, 50, 0.5, 0.5, 0, 0.5)
#仿射（图片，x，y，a11,a12,a21,a22）
#shifted = projection(img, 1, 0, 0, 0, 1, 0, 0, 0, 0)
#投影（图片，x，y，a11,a12,a21,a22）
#shifted = resize(img,500,500);
#cv2.INTER_NEAREST;cv2.INTER_LINEAR;cv2.INTER_AREA;cv2.INTER_CUBIC;cv2.INTER_LANCZOS4
#缩放（图片，长，宽，方法）
#shifted = flip(img,"h")
#翻转（图片，方法）"h"水平翻转"v"垂直翻转
cv2.imwrite('cat1.jpg', shifted)
img1 = cv2.imread('cat1.jpg')
#cv2.imshow('cat', img)
cv2.imshow('new_cat', img1)
cv2.waitKey(0)

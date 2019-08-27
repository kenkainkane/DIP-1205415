import cv2
import numpy as np

im1 = cv2.imread('img/bright.jpg',0)
im2 = cv2.imread('img/darkAndBright.jpg',0)
im3 = cv2.imread('img/dark.jpg',0)

cv2.imshow('im1', im1)
cv2.imshow('im2', im2)
cv2.imshow('im3', im3)

cv2.waitKey(0)
cv2.destroyAllWindows()

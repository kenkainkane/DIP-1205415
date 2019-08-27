import cv2
import numpy as np

# Load image and convert to grayscale
im1 = cv2.imread('bright.jpg', 0)
im2 = cv2.imread('darkAndbright.jpg', 0)
im3 = cv2.imread('dark.jpg', 0)

# Adjust gamma = 0.5
lowGammaIm1 = np.power(im1/255, 0.5)
lowGammaIm2 = np.power(im2/255, 0.5)
lowGammaIm3 = np.power(im3/255, 0.5)

# Adjust gamme = 1.5
highGammaIm1 = np.power(im1/255, 1.5)
highGammaIm2 = np.power(im2/255, 1.5)
highGammaIm3 = np.power(im3/255, 1.5)

cv2.imshow('lowGammaIm1', lowGammaIm1)
cv2.imshow('lowGammaIm2', lowGammaIm2)
cv2.imshow('lowGammaIm3', lowGammaIm3)

cv2.imshow('highGammaIm1', highGammaIm1)
cv2.imshow('highGammaIm2', highGammaIm2)
cv2.imshow('highGammaIm3', highGammaIm3)

cv2.waitKey(0)
cv2.destroyAllWindows()

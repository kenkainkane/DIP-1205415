import cv2
import numpy as np

img = cv2.imread('../img/lenna.png', 0)

# create laplacian filter
laplacian4 = np.array((
    [0, 1, 0],
    [1, -4, 1],
    [0, 1, 0]), dtype="int")

laplacian8 = np.array((
    [1, 1, 1],
    [1, -4, 1],
    [1, 1, 1]), dtype="int")

lap4 = cv2.filter2D(img, -1, laplacian4)
lap8 = cv2.filter2D(img, -1, laplacian8)

# output = img + c * laplacian (Using negative c if center of filter is negative. And vice versa.)
cv2.imshow('laplacian4', img-lap4)
cv2.imshow('laplacian8', img-lap8)

cv2.waitKey(0)
cv2.destroyAllWindows()
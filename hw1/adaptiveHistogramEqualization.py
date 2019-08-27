import cv2
import numpy as np
from matplotlib import pyplot as plt

# Load image and convert to gray scale
im = cv2.imread('img/bright.jpg', 0)

# create CLAHE windows and apply
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(7,7))
res = clahe.apply(im)

imHis = cv2.calcHist([im], [0], None, [256], [0, 256])
plt.subplot(211)
plt.plot(imHis)

claheHis = cv2.calcHist([res], [0], None, [256], [0, 256])
plt.subplot(212)
plt.plot(claheHis)

plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()

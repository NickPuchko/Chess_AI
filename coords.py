from PIL import Image
from pylab import *
import numpy as np
import cv2
from scipy.ndimage import filters

sigma = 6
im = np.array(Image.open('chess1.jpg').convert('L'))
im = cv2.resize(im, (1280, 720))
imx = np.zeros(im.shape)
filters.gaussian_filter(im, (sigma, sigma), (0, 1), imx)

imy = np.zeros(im.shape)
filters.gaussian_filter(im, (sigma, sigma), (1, 0), imy)

magn = np.sqrt(imx**2 + imy**2)
magn = np.uint8(magn)
im = magn
gray = im
corners = cv2.goodFeaturesToTrack(gray, 49, 0.01, 10)
corners = np.int0(corners)
a = 0
xa = np.zeros(49, int)
ya = np.zeros(49, int)
for i in corners:
    x, y = i.ravel()
    cv2.circle(im, (x, y), 2, 255, -4)

    xa[a] = int(x)
    ya[a] = int(y)
    a += 1

xa.sort()
cv2.imshow('img', im)
cv2.waitKey(3000)
cv2.destroyAllWindows()

xPiece = int(input())
columns = 0
xCoordinates = np.zeros(7)
for i in range(7):
    xCoordinates[columns] = np.mean(xa[7*i:7*i+6])
    columns += 1
print(f"Mean X of every column: \n{xCoordinates}")
for i in range(6):
    if xCoordinates[i] < xPiece < xCoordinates[i+1]:
        xPieceCoordinate = "B"
        break
    if xCoordinates[i] > xPiece:
        xPieceCoordinate = "A"
        break
print(f"Letter is {xPieceCoordinate}")

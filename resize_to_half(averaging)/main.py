import cv2
import numpy as np

img1024 = cv2.imread("1024.jpg")

def resize_average(x):
	'''
	Resizes given image to half the size by averaging pixels
	'''
	(h,w,c) = x.shape
	result = np.zeros((h/2,w/2,c))
	for i in range(h/2):
		for j in range(w/2):
			result[i][j] = x[2*i][2*j]//4 + x[2*i +1][2*j]//4 + x[2*i][2*j +1]//4 + x[2*i +1][2*j +1]//4

	return result


img512 = resize_average(img1024)
cv2.imwrite("512.jpg",img512)


img256 = resize_average(img512)
cv2.imwrite("256.jpg",img256)


img128 = resize_average(img256)
cv2.imwrite("128.jpg",img128)
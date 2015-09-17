import cv2
import numpy as np

img128 = cv2.imread("128.jpg")

def resize_replicate(x):
	'''
	Resizes given image to double the size by replicating pixels
	'''
	(h,w,c) = x.shape
	result = np.zeros((2*h,2*w,c))
	for i in range(h):
		for j in range(w):
			result[2*i][2*j] = result[2*i +1][2*j] = result[2*i][2*j +1] = result[2*i +1][2*j +1] = x[i][j]

	return result



img256 = resize_replicate(img128)
cv2.imwrite("256.jpg",img256)


img512 = resize_replicate(img256)
cv2.imwrite("512.jpg",img512)


img1024 = resize_replicate(img512)
cv2.imwrite("1024.jpg",img1024)
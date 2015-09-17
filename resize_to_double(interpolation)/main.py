import cv2
import numpy as np

img128 = cv2.imread("128.jpg")

def resize_replicate(x):
	'''
	Resizes given image to double the size by replicating pixels
	'''
	(h,w,c) = x.shape
	result = np.zeros((2*h -1,2*w -1,c))
	for i in range(h):
		for j in range(w):
			result[2*i][2*j] = x[i][j]	
			if (i!=h-1 and j!=w-1):
				result[2*i][2*j +1] = x[i][j]//2 + x[i][j+1]//2
				result[2*i +1][2*j] = x[i][j]//2 + x[i+1][j]//2
				result[2*i +1][2*j +1] = x[i][j]//4 + x[i+1][j]//4 + x[i][j+1]//4 + x[i+1][j+1]//4
			elif (i!=h-1):
				result[2*i +1][2*j] = x[i][j]//2 + x[i+1][j]//2
			elif (j!=w-1):
				result[2*i][2*j +1] = x[i][j]//2 + x[i][j+1]//2

	return result



img256 = resize_replicate(img128)
cv2.imwrite("256.jpg",img256)


img512 = resize_replicate(img256)
cv2.imwrite("512.jpg",img512)


img1024 = resize_replicate(img512)
cv2.imwrite("1024.jpg",img1024)
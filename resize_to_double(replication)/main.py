import cv2
import numpy as np

img = cv2.imread("../lena.jpg")

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


img_doubled_replicate = resize_replicate(img)
cv2.imwrite("img_doubled_replicate.jpg",img_doubled_replicate)
import cv2
import numpy as np

img = cv2.imread("../lena.jpg")

def resize_skip(x):
	'''
	Resizes given image to half the size by skiping pixels
	'''
	(h,w,c) = x.shape
	result = np.zeros((h/2,w/2,c))
	for i in range(h/2):
		for j in range(w/2):
			result[i][j] = x[2*i][2*j]

	return result



img_half_skip = resize_skip(img)
cv2.imwrite("img_half_skip.jpg",img_half_skip)
import cv2
import numpy as np

img = cv2.imread("../lena.jpg")

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


img_half_average = resize_average(img)
cv2.imwrite("img_half_average.jpg",img_half_average)
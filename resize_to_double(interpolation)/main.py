import cv2
import numpy as np

img = cv2.imread("../lena.jpg")

def resize_interpolate(x):
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



img_doubled_interpolate = resize_interpolate(img)
cv2.imwrite("img_doubled_interpolate.jpg",img_doubled_interpolate)
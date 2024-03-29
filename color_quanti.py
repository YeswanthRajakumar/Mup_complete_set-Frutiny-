import numpy as np
import cv2

img = cv2.imread('defects2.jpeg')
img = cv2.resize(img, (300, 450)) 
Z = img.reshape((-1,3))

# convert to np.float32
Z = np.float32(Z)

# define criteria, number of clusters(K) and apply kmeans()
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
K = 10
cv2.imshow('original',img)
for  i in range(1,K):
	frame_string = "k="
	counter =str(i)
	ret,label,center=cv2.kmeans(Z,i,None,criteria,10,cv2.KMEANS_RANDOM_CENTERS)

	# Now convert back into uint8, and make original image
	center = np.uint8(center)
	res = center[label.flatten()]
	res2 = res.reshape((img.shape))
	cv2.imshow(frame_string+counter,res2)
	
cv2.waitKey(0)
cv2.destroyAllWindows()


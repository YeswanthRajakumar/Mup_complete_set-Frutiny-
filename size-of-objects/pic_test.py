import cv2 

imagepath = 'img.jpg'
gray = cv2.imread(imagepath,0)
cv2.imwrite('Converted_img.jpg',gray)
print("Converted")


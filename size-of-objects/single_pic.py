import cv2
import os 
import time

cap = cv2.VideoCapture(0)
result = True
while(result):
    
    ret,frame = cap.read()
    cv2.imwrite("img.jpg",frame)
    cv2.imwrite('backup_pics/img1.jpg',frame)
    result =False
cap.release()
cv2.destroyAllWindows()
        
 

print("call second file ")

command = "python3 object_size.py"
os.system(command)

print("second file executed ")


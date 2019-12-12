import cv2 as cv
import  numpy as np

#upper and lower bound for green color
#params(Hue,saturation,unknown)

lowerBound =np.array([10, 100, 20])
upperBound = np.array([25, 255, 255])


cap = cv.VideoCapture(0)

#Open and Close for Noise Removal

kernelOpen = np.ones((5,5))
kernelClose = np.ones((5,5))

font = cv.FONT_HERSHEY_SIMPLEX
conts=[]
while True:
    ret,frame = cap.read()
    frame = cv.resize(frame,(600,600))

    #convert BGR to HSV

    frameHSV = cv.cvtColor(frame,cv.COLOR_BGR2HSV)
    mask = cv.inRange(frameHSV,lowerBound,upperBound,)

    #Morphology(Noise-Removal)
    maskOpen = cv.morphologyEx(mask,cv.MORPH_OPEN,kernelOpen)
    maskClose = cv.morphologyEx(maskOpen,cv.MORPH_CLOSE,kernelClose)

    maskFinal = maskClose
    conts,h = cv.findContours(maskFinal.copy(),cv.RETR_EXTERNAL,cv.CHAIN_APPROX_NONE)
    cv.drawContours(frame,conts,-1,(255,0,0),2)
    
    
    # Draw rectangle in original image
    '''
    for i in range(len(conts)):
        x,y,w,h = cv.boundingRect(conts[i])
        cv.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
    '''
    
    #Display Frames
    #cv.imshow("MaskOpen",maskOpen)
    #cv.imshow("MaskClose",maskClose)
    cv.imshow("Mask",mask)
    cv.imshow("Original",frame)
    if cv.waitKey(1) & 0XFF == ord('q'):
        cap.release()
        cv.destroyAllWindows()
contours = (len(conts[0])+len(conts[1])+len(conts[2]))/3
print(contours)
        

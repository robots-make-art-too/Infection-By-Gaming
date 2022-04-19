import numpy as np
import cv2  as cv
from matplotlib import pyplot as plt

dnnnet=cv.dnn.readNetFromTensorflow("opencv_face_detector_uint8.pb","opencv_face_detector.pbtxt")
mou=cv.imread("Mouse3.jpg")
mou1=mou
mou2=cv.imread("Mouse1.jpg")
mou3=cv.imread("Mouse5.jpg")
n=0
def GTong(img):
 img=cv.medianBlur(img,7) 
 img=cv.GaussianBlur(img,(5,5),0)
 return img


def LogicAdd(mg1,mg2,x1,y1,x2,y2):
 
    rows,cols,channels=mg2.shape
    roi=mg1[y1-180:rows+y1-180,x1-5:cols+x1-5]
    rows2,cols2,channels=roi.shape
 
    if rows2!=cols2:
        return 
    img2gray=cv.cvtColor(mg2, cv.COLOR_BGR2GRAY)
    GTong(img2gray)
    ret,mask=cv.threshold(img2gray,20,255,cv.THRESH_BINARY)
    
    mask_inv=cv.bitwise_not(mask) 
    img1_bg=cv.bitwise_and(roi,roi,mask=mask_inv) 
    img2_fg=cv.bitwise_and(mg2,mg2,mask=mask)
    dst=cv.add(img1_bg,img2_fg)
    cv.imshow("img1_bg",img1_bg)
    cv.imshow("mg2",img2_fg)
    mg1[y1-180:rows+y1-180,x1-5:cols+x1-5]=dst

    return mg1
 
 
    
cap = cv.VideoCapture(0)
cap.set(cv.CAP_PROP_FRAME_WIDTH,640)
cap.set(cv.CAP_PROP_FRAME_HEIGHT,480)
while True:
    success,img = cap.read()
    cv.imshow('faces1',img)
    h,w=img.shape[:2]

    blobs=cv.dnn.blobFromImage(img,1.0,(300,300),[104.,117.,123.],False,False)
    dnnnet.setInput(blobs)                                                                                                                                                                                                                                                                                      
    detections=dnnnet.forward()
   
    faces=0
    for i in range(0,detections.shape[2]): 
        
        confidence=detections[0,0,i,2]  
        
        if confidence>0.6:
        
         faces+=1
         #print(faces)
         box=detections[0,0,i,3:7]*np.array([w,h,w,h]) 
        
         x1,y1,x2,y2=box.astype("int")
         y=y1-10 if y1-10>10 else y1+10            
         
         if y1-190<0 or x1-70<0: 
            
            confidence=0
            continue
         img=LogicAdd(img,mou,x1,y1,x2,y2)
        
   
    if img is None:
        continue
    cv.imshow('faces2',img)
    cv.waitKey(1)
cap.release()
cv.destroyAllWindows()

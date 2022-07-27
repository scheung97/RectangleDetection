# import argparse
import cv2
from cv2 import THRESH_BINARY
from cv2 import THRESH_OTSU
import numpy as np 

def Rect_Detection(): 
    WIDTH = 400
    HEIGHT = 400

    img_input = "CV\media\ez_shapes.jpg" #2d shapes
    # img_input = "CV\media\example_sign.jpg" #ctown image
  
    # 1) import camera/imge
    img = cv2.imread(img_input, cv2.IMREAD_COLOR)
    w,h,_ = img.shape
    if w > 1000 or h > 1000: 
        img = cv2.resize(img, (WIDTH, HEIGHT), interpolation = cv2.INTER_LINEAR)  # resize image
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # convert to grayscale
    blur = cv2.GaussianBlur(gray, (5,5),1)  # 5x5 kernel
    # cv2.imshow("blur", blur)


    # 2) filter image 
    # adpt_thresh_img = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
    # cv2.THRESH_BINARY,9,4)  # testing 9 nearest pixels, 
    #                         # 3 = constant subtracted from the mean or weighted mean

    thresh_img = cv2.threshold(blur, 0, 255, THRESH_BINARY+THRESH_OTSU)[1]
    edges = cv2.Canny(thresh_img, 150, 200, 1)

    # finds contours and gets number of corners
    # source: https://medium.com/analytics-vidhya/opencv-findcontours-detailed-guide-692ee19eeb18

    """
    contour shape detection: 
    https://www.youtube.com/watch?v=Fchzk1lDt7Q&ab_channel=Murtaza%27sWorkshop-RoboticsandAI (contour area + bounding box)
    https://www.delftstack.com/howto/python/opencv-shape-detection/#:~:text=Use%20the%20findContours()%20and,number%20of%20corners%20it%20has. (shape check)

    """
    # 3) contour detection 
    cnts = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]

    # 4) learn rectangles
    for cnt in cnts:
        approx = cv2.approxPolyDP(cnt,0.0125*cv2.arcLength(cnt,False),True)
        if len(approx)==4:
            area = cv2.contourArea(cnt)
            if area < (0.6*HEIGHT*WIDTH): #removes large detections that obscure the others
                # cv2.drawContours(img,[cnt],0,(0,0,255),-1)
                cv2.imshow("test", img)
                x, y, w, h = cv2.boundingRect(approx)
                cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 2)

      # 5) pull text from rectangles 
                #pull text here


    
    
    
    
    
  

    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__": 
    Rect_Detection()
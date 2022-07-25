import argparse
import cv2
from cv2 import THRESH_BINARY
from cv2 import THRESH_OTSU
from cv2 import THRESH_BINARY_INV
import numpy as np 

def main(): 
    # big enough just for viewing, can adjust size 
    # if building a model or needing a smaller size
    width = 400
    height = 400

    img_input = "CV\media\ez_shapes.jpg" #2d shapes
    # img_input = "CV\media\example_sign.jpg" #ctown image
  
    # 1) import camera/imge
    img = cv2.imread(img_input, cv2.IMREAD_COLOR)
    w,h,_ = img.shape
    if w > 1000 or h > 1000: 
        img = cv2.resize(img, (width, height), interpolation = cv2.INTER_LINEAR)  # resize image
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # convert to grayscale
    blur = cv2.GaussianBlur(gray, (5,5),1)  # 5x5 kernel

    # cv2.imshow("blur", blur)

    # 2) filter image 
    adpt_thresh_img = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
    cv2.THRESH_BINARY,9,4)  # testing 9 nearest pixels, 
                            # 3 = constant subtracted from the mean or weighted mean

    thresh_img = cv2.threshold(blur, 1000, 255, THRESH_BINARY_INV+THRESH_OTSU)[1]
    # cv2.imshow("thresh", thresh_img)
    # cv2.imshow("adpt_thresh", adpt_thresh_img)

    edges = cv2.Canny(thresh_img, 150, 200, 1)
    # cv2.imshow("edges", edges)

    # finds contours and draws them on the original image
    # https://medium.com/analytics-vidhya/opencv-findcontours-detailed-guide-692ee19eeb18
    cnts, _ = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    new_img = np.ones((gray.shape[0], gray.shape[1]))
    cv2.drawContours(new_img, cnts, -1, (0,255,75), 2)
    cv2.imshow("test", new_img)
        


    
    
    
    # 3) corner detection 
    # 4) learn rectangles
    # 5) pull text from rectangles 





    
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__": 
    main()
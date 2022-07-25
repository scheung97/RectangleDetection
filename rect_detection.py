import cv2
import numpy as np 

def main(): 
    # big enough just for viewing, can adjust size 
    # if building a model or needing a smaller size
    width = 400
    height = 400

    # img_input = "CV\ez_shapes.jpg" #2d shapes
    img_input = "CV\example_sign.jpg" #ctown image
    
    # 1) import camera/imge
    img = cv2.imread(img_input, cv2.IMREAD_COLOR)
    w,h,_ = img.shape
    if w > 1000 or h > 1000: 
        img = cv2.resize(img, (width, height), interpolation = cv2.INTER_LINEAR)  # resize image
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # convert to grayscale
    blur = cv2.GaussianBlur(gray, (5,5),1)
    # gray = gray/255  # normalize 
    # cv2.imshow("blur", blur)

    # 2) filter image 
    thresh_img = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
    cv2.THRESH_BINARY,9,3)
    cv2.imshow("thresh", thresh_img)

    
    
    
    # 3) corner detection 
    # 4) learn rectangles
    # 5) pull text from rectangles 





    
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__": 
    main()
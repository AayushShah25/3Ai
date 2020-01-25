import cv2


def Load():
    
    video = cv2.VideoCapture(r'../DATA/Loading.mov')
    
    if video.isOpened() == True:
        
        cv2.namedWindow("The Video")
        cv2.moveWindow("The Video", 500,200)
    
    elif video.isOpened() == False:
        
        print('No Data For Loading Video')
        return 0
        
    while video.isOpened():
        
        _, frame = video.read()
        
        if _ == True:
            frame = cv2.resize(frame,(1000,520))    
            
            cv2.imshow("The Video",frame)
        
            if cv2.waitKey(10) & 0xff == 27:
                break
        
        if _ == False :
            break
        
    cv2.destroyAllWindows()
    video.release()
    

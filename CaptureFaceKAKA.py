import cv2

import os
from datetime import datetime

class GetImageForReference:
    
    detector = cv2.CascadeClassifier(r'./DATA/face.xml')
    
    
    
    try:
        now = datetime.now()
        date = now.strftime("%d-%m-%y")
        os.mkdir('./Requests/'+str(date))
    except Exception:
        pass
    
    def CaptureKAKA(self):

        
        
        now = datetime.now()
        date = now.strftime("%d-%m-%y")
        time = now.strftime("%H%M%S")
            
        temp = cv2.VideoCapture(0)
        timetoclosewindow = 0
        
        while True:
            
            _, frame = temp.read()
            tosave = frame.copy()
            cv2.circle(frame, (320,160),150, (255,0,225), 2)
            frame = cv2.flip(frame,1)
            ableToCapture = False
            
            
#            cv2.putText(frame,"Keep your face inside the Circle",(80,400),  cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,255) , 2)
            
            detection = self.detector.detectMultiScale(cv2.cvtColor(frame.copy(), cv2.COLOR_BGR2GRAY), 1.3,5)
            
            if len(detection) > 0:
                x,y,w,h = detection[0]
                
                cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0), 2)
                
                if (x,y) > (200,70) and (x,y) < (250,100):
                    cv2.putText(frame,"Press A to Capture !",(130,400),  cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0) , 2)
                    ableToCapture = True
                
                else:
                    cv2.putText(frame,"Keep your face inside the Circle",(80,400),  cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,255) , 2)
                
            else:
               cv2.putText(frame,"Keep your face inside the Circle",(80,400),  cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,255) , 2) 
            
            cv2.namedWindow("Press A to Capture picture")
            cv2.moveWindow("Press A to Capture picture",120,300)
            cv2.imshow("Press A to Capture picture", frame)
            
            
            if cv2.waitKey(1) & 0xff == ord('a'):
                
                if ableToCapture:
                    
                    cv2.imwrite("./Requests/"+str(date)+"/"+str(time)+".png", tosave[y:y+h, x:x+w])
                    break
            print(timetoclosewindow)
            if timetoclosewindow == 200:
                break
        
            timetoclosewindow += 1
            
            
        cv2.destroyAllWindows()
        temp.release()
        
        if timetoclosewindow >= 200:
            return 0
        if timetoclosewindow < 200:
            print("In Less 200 : ",timetoclosewindow)
            print("The Time passed : ",time)
            
            return time

       
         
        
        

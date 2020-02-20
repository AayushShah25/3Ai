import cv2

import os
from datetime import datetime

class GetImageForReference:
    
    detector = cv2.CascadeClassifier(r'./DATA/face.xml')
    now = datetime.now()
    date = now.strftime("%d-%m-%y")
    time = now.strftime("%H%M%S")
    
    try:
        os.mkdir('./Requests/'+str(date))
    except Exception:
        pass
    
    def __init__(self):
        
        temp = cv2.VideoCapture(0)
        timetoclosewindow = 0
        
        while True:
            
            _, frame = temp.read()
            tosave = frame.copy()
            cv2.circle(frame, (320,160),150, (255,0,225), 2)
#            cv2.circle(frame, (200,70),50, (255,0,225), -1)
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
            
            
            cv2.imshow("Press A to Capture picture", frame)
            
            
            if cv2.waitKey(1) & 0xff == ord('a'):
                
                if ableToCapture:
                    
                    cv2.imwrite("./Requests/"+str(self.date)+"/"+str(self.time)+".png", tosave[y:y+h, x:x+w])
                    break
            
            if timetoclosewindow == 200:
                break
        
            timetoclosewindow += 1
            
            
        cv2.destroyAllWindows()
        temp.release()
        return None
        
        
        


        

import tkinter as tk
import mysql.connector as connector
import Names
from tkinter import messagebox
import os
import numpy as np
from numpy import float32,array
from keras.models import load_model
import EditEnter
import CaptureScreen
import webbrowser
import cv2
import MainPage
import shutil



class Show:
    def __init__(self, Details):
        
        global saved_
        saved_ = False  
        model=load_model('../DATA/facenet_keras.h5')
        print(Details)
        
        
        def on_closing():
            
            if messagebox.askokcancel("Quit", "Do you want to quit?\nThe Details will be deleted !!"):
                
                try:

                    shutil.rmtree(r'C:\Users\GIGABYTE\Desktop\Project\Faces\\'+str(Details[0]))
                except Exception:
                    print('Error in Deleting the File !!')
                
                
                
                top.destroy()
                MainPage.MAINCALL(Details[-1])
                
                
        def ExtractFeatures(img):
            
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                        
            img = cv2.resize(img, (160,160))
            img = img.reshape((1,160,160,3))
            img = img / 255.0
            
            return model.predict(img)[0]
            
            
            
            
            
            
        def CheckPhotos():
            
            try:

                if (webbrowser.open(r'C:\Users\GIGABYTE\Desktop\Project\Faces\\'+ str(Details[0]))):
                    pass
                else:
                    print (' No File Found Error ')
                    
            except Exception:

                print('Error in opening the Folder ')
        def Re():
            print('Here in Re Take Images')
            top.destroy()
            CaptureScreen.Capture(Details)


        def Edit():
            
            
            print('HERE ! In Edit Info')
            top.destroy()
            print(Details)
            EditEnter.Editorial(Details)
            
            
            
        def Another():
            global saved_

            if saved_ == False:

                faces = []
                
                
                if len(os.listdir("../Faces/"+str(Details[0]))) > 6 or len(os.listdir("../Faces/"+str(Details[0]))) < 3 :
                    
                    messagebox.showinfo('Images are not sufficient ','Please keep images between 3 and 6')
                    return 0
                
                for face in os.listdir("../Faces/"+str(Details[0])):
                    
                    img = cv2.imread("../Faces/"+str(Details[0])+"/"+face)
                    faces.append(ExtractFeatures(img))
                    

                faces = np.array(faces)
                String_Code = faces.__repr__()
                
                
                mydb= connector.connect(host = "localhost", user= "root", passwd = "aayush123", database="testdb")
                cursor = mydb.cursor()
                
                q = "insert into userse (name,age,gender,post,contact,address, encodings, ref_id) values ( %s , %s , %s , %s , %s , %s , %s, %s )"

                data = [(Details[1], int(Details[2]), Details[3], Details[4], Details[5], Details[6], String_Code, Details[-1] ) ]
                print(data)
                cursor.executemany(q,data)
                mydb.commit()
                saved_ = True


            mydb= connector.connect(host = "localhost", user= "root", passwd = "aayush123", database="testdb")
            cursor = mydb.cursor()

            cursor.execute("Select count(ID) from userse")
            result = cursor.fetchall()
            incrementedID = int(result[0][0]) + 1
            top.destroy()

            Names.EnterData(incrementedID,Details[-1])



        def Train():

            global saved_
            if saved_ == False:
                
                faces = []
                
                
                if len(os.listdir("../Faces/"+str(Details[0]))) > 6 or len(os.listdir("../Faces/"+str(Details[0]))) < 3 :
                    
                    messagebox.showinfo('Images are not sufficient ','Please keep images between 3 and 6')
                    return 0
                
                for face in os.listdir("../Faces/"+str(Details[0])):
                    
                    img = cv2.imread("../Faces/"+str(Details[0])+"/"+face)
                    faces.append(ExtractFeatures(img))
                    

                faces = np.array(faces)
                String_Code = faces.__repr__()
                
                
                mydb= connector.connect(host = "localhost", user= "root", passwd = "aayush123", database="testdb")
                cursor = mydb.cursor()
                
                q = "insert into userse (name,age,gender,post,contact,address, encodings,ref_id) values ( %s , %s , %s , %s , %s , %s , %s , %s )"

                data = [(Details[1], int(Details[2]), Details[3], Details[4], Details[5], Details[6], String_Code, Details[-1] ) ]
                print(data)
                cursor.executemany(q,data)
                mydb.commit()
                saved_ = True
                
                print("The Person is added ")
                top.destroy()
                MainPage.MAINCALL(Details[-1])
            
            

           


                
            

        top = tk.Toplevel()

        top.geometry("600x1000")
        
        top.resizable(0, 0)
        top.title("Check The Info")
        top.configure(background="#d9d9d9")
        top.protocol("WM_DELETE_WINDOW", on_closing)
                      
        
        try:
            first = os.listdir(r'C:\Users\GIGABYTE\Desktop\Project\Faces\\'+str(Details[0]))[0]            
            photo = tk.PhotoImage(file=r"C:\Users\GIGABYTE\Desktop\Project\Faces\\"+str(Details[0])+"\\"+first)
            
        except Exception:
                    
            photo = tk.PhotoImage(file=r"C:\Users\GIGABYTE\Desktop\Project\Faces\noimage.png")
        #photo = tk.PhotoImage(file=r"C:\Users\GIGABYTE\Desktop\Project\Faces\\"+str(Details[0])+"\\1.png")

        self.ID = tk.Label(top,font="-family {Product Sans} -size 18 -weight normal")
        self.ID.place(relx=0.193, rely=0.288, height=71, width=124)
        self.ID.configure(activebackground="#f9f9f9")
        self.ID.configure(activeforeground="black")
        self.ID.configure(background="#d9d9d9")
        self.ID.configure(cursor="fleur")
        self.ID.configure(disabledforeground="#a3a3a3")
        self.ID.configure(foreground="#000000")
        self.ID.configure(highlightbackground="#d9d9d9")
        self.ID.configure(highlightcolor="black")
        self.ID.configure(text='''ID : ''')

        self.IMAGE = tk.Label(top,image=photo)
        self.IMAGE.place(relx=0.3, rely=0.038, height=201, width=224)
        self.IMAGE.configure(activebackground="#f9f9f9")
        self.IMAGE.configure(activeforeground="black")
        self.IMAGE.configure(background="#d9d9d9")
        self.IMAGE.configure(disabledforeground="#a3a3a3")
        self.IMAGE.configure(foreground="#000000")
        self.IMAGE.configure(highlightbackground="#d9d9d9")
        self.IMAGE.configure(highlightcolor="black")
        self.IMAGE.configure(text='''IMAGE''')

        self.CheckBt = tk.Button(top, text = "Check The Photos",font="-family {Product Sans} -size 12 -weight bold",fg="white",bg="#800040", command = CheckPhotos , wraplength="150")
        self.CheckBt.place(relx = 0.722, rely = 0.09, height =80 , width=150 )

        self.NAME = tk.Label(top,font="-family {Product Sans} -size 18 -weight normal")
        self.NAME.place(relx=0.2, rely=0.35, height=71, width=114)
        self.NAME.configure(activebackground="#f9f9f9")
        self.NAME.configure(activeforeground="black")
        self.NAME.configure(background="#d9d9d9")
        self.NAME.configure(disabledforeground="#a3a3a3")
        self.NAME.configure(foreground="#000000")
        self.NAME.configure(highlightbackground="#d9d9d9")
        self.NAME.configure(highlightcolor="black")
        self.NAME.configure(text='''Name : ''')

        self.AGE = tk.Label(top,font="-family {Product Sans} -size 18 -weight normal")
        self.AGE.place(relx=0.0, rely=0.463, height=61, width=144)
        self.AGE.configure(activebackground="#f9f9f9")
        self.AGE.configure(activeforeground="black")
        self.AGE.configure(background="#d9d9d9")
        self.AGE.configure(disabledforeground="#a3a3a3")
        self.AGE.configure(foreground="#000000")
        self.AGE.configure(highlightbackground="#d9d9d9")
        self.AGE.configure(highlightcolor="black")
        self.AGE.configure(text='''Age : ''')

        self.GENDER = tk.Label(top,font="-family {Product Sans} -size 18 -weight normal")
        self.GENDER.place(relx=0.017, rely=0.55, height=71, width=124)
        self.GENDER.configure(activebackground="#f9f9f9")
        self.GENDER.configure(activeforeground="black")
        self.GENDER.configure(background="#d9d9d9")
        self.GENDER.configure(cursor="fleur")
        self.GENDER.configure(disabledforeground="#a3a3a3")
        self.GENDER.configure(foreground="#000000")
        self.GENDER.configure(highlightbackground="#d9d9d9")
        self.GENDER.configure(highlightcolor="black")
        self.GENDER.configure(text='''Gender : ''')

        self.POST = tk.Label(top,font="-family {Product Sans} -size 18 -weight normal")
        self.POST.place(relx=0.012, rely=0.638, height=81, width=134)
        self.POST.configure(activebackground="#f9f9f9")
        self.POST.configure(activeforeground="black")
        self.POST.configure(background="#d9d9d9")
        self.POST.configure(disabledforeground="#a3a3a3")
        self.POST.configure(foreground="#000000")
        self.POST.configure(highlightbackground="#d9d9d9")
        self.POST.configure(highlightcolor="black")
        self.POST.configure(text='''Post : ''')

        self.CONTACT = tk.Label(top,font="-family {Product Sans} -size 18 -weight normal")
        self.CONTACT.place(relx=0.022, rely=0.75, height=71, width=124)
        self.CONTACT.configure(activebackground="#f9f9f9")
        self.CONTACT.configure(activeforeground="black")
        self.CONTACT.configure(background="#d9d9d9")
        self.CONTACT.configure(disabledforeground="#a3a3a3")
        self.CONTACT.configure(foreground="#000000")
        self.CONTACT.configure(highlightbackground="#d9d9d9")
        self.CONTACT.configure(highlightcolor="black")
        self.CONTACT.configure(text='''Contact : ''')

        self.ADDRESS = tk.Label(top,font="-family {Product Sans} -size 18 -weight normal")
        self.ADDRESS.place(relx=-0.057, rely=0.838, height=81, width=224)
        self.ADDRESS.configure(activebackground="#f9f9f9")
        self.ADDRESS.configure(activeforeground="black")
        self.ADDRESS.configure(background="#d9d9d9")
        self.ADDRESS.configure(disabledforeground="#a3a3a3")
        self.ADDRESS.configure(foreground="#000000")
        self.ADDRESS.configure(highlightbackground="#d9d9d9")
        self.ADDRESS.configure(highlightcolor="black")
        self.ADDRESS.configure(text='''Address :''')

        self.IDd = tk.Label(top,font="-family {Product Sans} -size 28 -weight normal")
        self.IDd.place(relx=0.383, rely=0.309, height=41, width=124)
        self.IDd.configure(activebackground="#f9f9f9")
        self.IDd.configure(activeforeground="black")
        self.IDd.configure(background="#d9d9d9")
        self.IDd.configure(disabledforeground="#a3a3a3")
        self.IDd.configure(foreground="#000000")
        self.IDd.configure(highlightbackground="#d9d9d9")
        self.IDd.configure(highlightcolor="black")
        self.IDd.configure(text=Details[0])

        self.NAMEd = tk.Label(top,font="-family {Product Sans} -size 28 -weight normal")
        self.NAMEd.place(relx=0.4, rely=0.36, height=50, width=300)
        self.NAMEd.configure(activebackground="#f9f9f9")
        self.NAMEd.configure(activeforeground="black")
        self.NAMEd.configure(background="#d9d9d9")
        self.NAMEd.configure(disabledforeground="#a3a3a3")
        self.NAMEd.configure(foreground="#000000")
        self.NAMEd.configure(highlightbackground="#d9d9d9")
        self.NAMEd.configure(highlightcolor="black")
        self.NAMEd.configure(text=Details[1])

        self.AGEd = tk.Label(top,font="-family {Product Sans} -size 28 -weight normal")
        self.AGEd.place(relx=0.2, rely=0.45, height=71, width=300)
        self.AGEd.configure(activebackground="#f9f9f9")
        self.AGEd.configure(activeforeground="black")
        self.AGEd.configure(background="#d9d9d9")
        self.AGEd.configure(disabledforeground="#a3a3a3")
        self.AGEd.configure(foreground="#000000")
        self.AGEd.configure(highlightbackground="#d9d9d9")
        self.AGEd.configure(highlightcolor="black")
        self.AGEd.configure(text=Details[2])

        self.GENDERd = tk.Label(top,font="-family {Product Sans} -size 28 -weight normal")
        self.GENDERd.place(relx=0.2, rely=0.55, height=71, width=300)
        self.GENDERd.configure(activebackground="#f9f9f9")
        self.GENDERd.configure(activeforeground="black")
        self.GENDERd.configure(background="#d9d9d9")
        self.GENDERd.configure(disabledforeground="#a3a3a3")
        self.GENDERd.configure(foreground="#000000")
        self.GENDERd.configure(highlightbackground="#d9d9d9")
        self.GENDERd.configure(highlightcolor="black")
        self.GENDERd.configure(text=Details[3])

        self.POSTd = tk.Label(top,font="-family {Product Sans} -size 28 -weight normal")
        self.POSTd.place(relx=0.2, rely=0.643, height=71, width=300)
        self.POSTd.configure(activebackground="#f9f9f9")
        self.POSTd.configure(activeforeground="black")
        self.POSTd.configure(background="#d9d9d9")
        self.POSTd.configure(disabledforeground="#a3a3a3")
        self.POSTd.configure(foreground="#000000")
        self.POSTd.configure(highlightbackground="#d9d9d9")
        self.POSTd.configure(highlightcolor="black")
        self.POSTd.configure(text=Details[4])

        self.CONTACTd = tk.Label(top,font="-family {Product Sans} -size 28 -weight normal")
        self.CONTACTd.place(relx=0.2, rely=0.715, height=60, width=300)
        self.CONTACTd.configure(activebackground="#f9f9f9")
        self.CONTACTd.configure(activeforeground="black")
        self.CONTACTd.configure(background="#d9d9d9")
        self.CONTACTd.configure(disabledforeground="#a3a3a3")
        self.CONTACTd.configure(foreground="#000000")
        self.CONTACTd.configure(highlightbackground="#d9d9d9")
        self.CONTACTd.configure(highlightcolor="black")
        self.CONTACTd.configure(text=Details[5])

        self.ADDRESSd = tk.Label(top,font="-family {Product Sans} -size 10 -weight normal")
        self.ADDRESSd.place(relx=0.2, rely=0.838, height=81, width=300)
        self.ADDRESSd.configure(activebackground="#f9f9f9")
        self.ADDRESSd.configure(activeforeground="black")
        self.ADDRESSd.configure(background="#d9d9d9")
        self.ADDRESSd.configure(disabledforeground="#a3a3a3")
        self.ADDRESSd.configure(foreground="#000000")
        self.ADDRESSd.configure(highlightbackground="#d9d9d9")
        self.ADDRESSd.configure(highlightcolor="black")
        self.ADDRESSd.configure(text=Details[6])

        self.ADDMOREbtn = tk.Button(top,text = "Save & Add More",font="-family {Product Sans} -size 12 -weight bold",fg="white",bg="#800040",command=Another)
        self.ADDMOREbtn.place(relx=0.05,rely=0.93,height=50,width=150)
        
        self.Editbtn = tk.Button(top,text = "Edit Info",font="-family {Product Sans} -size 12 -weight bold",fg="white",bg="#248396",command=Edit)
        self.Editbtn.place(relx=0.34,rely=0.93,height=50,width=80)

        self.Rebtn = tk.Button(top,text = "Retake Photos",font="-family {Product Sans} -size 12 -weight bold",fg="white",bg="#248396",wraplength="60",command=Re)
        self.Rebtn.place(relx=0.52,rely=0.93,height=50,width=80)

        self.TRAINbtn = tk.Button(top,text = "Save & Exit",font="-family {Product Sans} -size 12 -weight bold",fg="white",bg="#700100",command=Train)
        self.TRAINbtn.place(relx=0.70,rely=0.93,height=50,width=150)

        #Edit Button Baki chhe.
        top.mainloop()


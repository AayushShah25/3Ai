import tkinter as tk
from tkinter import messagebox
import mysql.connector as connector
import ast



class Notifications:


    
        
    def __init__(self):
        
        
        
        def create():
            
            self.mydb= connector.connect(host = "localhost", user= "root", passwd = "aayush123", database="testdb")
            self.cursor = self.mydb.cursor()
            
            q = "select * from  requests_for_attendance where refered = false"
            self.cursor.execute(q)
            self.result = self.cursor.fetchall()
            
#            self.temp = tk.Tk()
#            self.temp.withdraw()
            self.root = tk.Toplevel()
            self.root.title("Notification List")
            
#            self.root.protocol("WM_DELETE_WINDOW",self.temp.destroy)
            self.root.geometry("650x400")
            self.canvas = tk.Canvas(self.root, borderwidth=0, background="#d9d9d9")
            self.frame = tk.Frame(self.canvas, background="#d9d9d9")
            self.vsb = tk.Scrollbar(self.root, orient="vertical", command=self.canvas.yview)
            self.canvas.configure(yscrollcommand=self.vsb.set)
            
            self.vsb.pack(side="right", fill="y")
            self.canvas.pack(side="left", fill="both", expand=True)
            self.canvas.create_window((4,4), window=self.frame, anchor="nw")
            
            self.frame.bind("<Configure>", lambda event, canvas=self.canvas: onFrameConfigure(self.canvas))
            
            populate(self.frame)
            
            self.root.mainloop()

            
        
        def Decline(id):
            self.mydb= connector.connect(host = "localhost", user= "root", passwd = "aayush123", database="testdb")
            self.cursor = self.mydb.cursor()
            q= "update requests_for_attendance set refered = true where id= {}".format(str(id))
            
            
            self.cursor.execute(q)
            self.mydb.commit()
            self.root.destroy()
#            self.temp.destroy()
            create()
        
        def Accept(id,date,time,personID):
            
            self.mydb= connector.connect(host = "localhost", user= "root", passwd = "aayush123", database="testdb")
            self.cursor = self.mydb.cursor()
            q = "select summary_of_daily_attendance from great_attendance where date_of_attendance = {}".format(date)
            self.cursor.execute(q)
            self.r = self.cursor.fetchone()
            
            if self.r == None:
                messagebox.showerror("The Technical Error found", "There is a technical error, please contact the team directly...\nError code : Tmismsedcshdagndgserd")
            
            else:
                print("\n\n IN ELSE \n\n")
                r = self.r[0]
                
                
                r = ast.literal_eval(r)
                
                try:
                    
                    r[personID][0] = 1
                    r[personID][1] = str(time)
                    
                    self.cursor = self.mydb.cursor()
                    q = "update great_attendance set summary_of_daily_attendance = %s where date_of_attendance = %s "
                    val = [(str(r) , date)]
                    self.cursor.executemany(q,val)
                    
                    self.cursor = self.mydb.cursor()
                    
                    self.cursor.execute("update requests_for_attendance set refered = true where id = {}".format(str(id)))
                    self.mydb.commit()
                
                except KeyError:
                    
                    messagebox.showerror("The Key is not Found", "There is an error please contact the developer\n Error code : Isdsndodtfidnfdatabase")
                
                
                
                
                
                messagebox.showinfo("Done","The Person has been attended successfully")
                self.root.destroy()
#                self.temp.destroy()
                create()
                
                
                

        def populate(frame):
            
            for i, row in enumerate(self.result):
                
                tk.Label(frame, text= str(i+1), width=3, borderwidth="1", 
                         relief="solid").grid(row=i, column=0)
                date = row[3][:2] + " / " + row[3][2:4] + " / " + "20"+row[3][4:]
                kaka = " Request ID : {} \n\n Person ID : {} \n\n Person Name : {} \n\n Date of Request : {} \n __________________________________".format(row[0], row[1], row[2], date)
                dateEntry = row[3]
                dateFormat = str(dateEntry[:2]) +"-"+ str(dateEntry[2:4]) +"-"+ str(dateEntry[4:])

                timeEntry = row[4]
                timeFormat = ''.join(str(timeEntry).split(":"))
                try:
                    print(r'C:\Users\GIGABYTE\Desktop\Project\Requests\\'+str(dateFormat)+'\\'+str(timeFormat)+'.png')
                    image = tk.PhotoImage(file = r'C:\Users\GIGABYTE\Desktop\Project\Requests\\'+str(dateFormat)+'\\'+str(timeFormat)+'.png')
                except Exception:
                    print(r'C:\Users\GIGABYTE\Desktop\Project\Faces\noimage.png')
                    image = tk.PhotoImage(file = r'C:\Users\GIGABYTE\Desktop\Project\Faces\noimage.png')
                
                try:
                    IMAGE = tk.Label(frame,image = image)
                    IMAGE.image = image
                    IMAGE.grid(row=i, column = 1)
                    
                except Exception:

                    tk.Label(frame, text = "Image Not Found").grid(row=i, column = 1)
                
                
                
                
                tk.Label(frame, text= kaka, bg = "#d9d9d9", font = "-size 10") .grid(row=i, column=2)
                         
                I = row[0]
                tk.Button(frame, text = "Decline", fg="white", bg="#800040", command = lambda I=I : Decline(I) ).grid(row=i, column = 3)
                personID = row[1]
                
                
                
                tk.Button(frame, text = "Accept", fg="white", bg="green", command = lambda I=I, dateEntry=dateEntry, timeEntry = timeEntry , personID = personID : Accept(I, dateEntry, timeEntry, personID) ) .grid(row=i, column =4)
                
                
        
        def onFrameConfigure(canvas):
            
            canvas.configure(scrollregion=canvas.bbox("all"))
        
        
        
        create()
        
        

import tkinter as tk
from tkcalendar import *
from tkinter import messagebox
import mysql.connector as connector
import Best
import MainPage
class GetDateforAttendance:
    def __init__(self,Admin_id):
        
        
    

        mydb= connector.connect(host = "localhost", user= "root", passwd = "aayush123", database="testdb")
        cursor = mydb.cursor()
        
        def on_close():
            top.destroy()
            MainPage.MAINCALL(Admin_id)
        def Show():
            
            
            string = self.cal.get_date()
            
            k = ""
            for i in string.split("/"):
                k += i
                
                        
            print(k)
            
            q = "select count(date_of_attendance) from great_attendance where date_of_attendance = "+str(k)
            cursor.execute(q)
            result = cursor.fetchone()
            
            if result[0] == 0:
                
                messagebox.showinfo("Select", "No record for the date :  "+self.cal.get_date())
                
            
            elif result[0] == 1:
                
                if messagebox.askyesno( "Select", "The Selected date is : " + self.cal.get_date() + "\n\n\nRecord Found ! \nWould you like to continue ? "):
                    Best.showAttendance(k)
                    
                
                
            
                
            
                    
        
        top = tk.Toplevel()

        top.geometry("664x559+578+266")
        top.minsize(124, 1)
        top.maxsize(1916, 1053)
        top.resizable(0, 0)
        top.title("Check Attendance")
        top.configure(background="#d9d9d9")
        top.protocol("WM_DELETE_WINDOW",on_close)

    
                      

        self.Label1 = tk.Label(top,background="#d9d9d9",disabledforeground="#a3a3a3",font="-family {Product Sans} -size 18 -weight normal"
                            ,foreground="#000000",text='''The Attendance''')
        self.Label1.place(relx=0.283, rely=0.034, height=31, width=184)
        

        self.Label1_4 = tk.Label(top,activebackground="#f9f9f9"
                                
                                ,background="#d9d9d9"
                                ,disabledforeground="#a3a3a3"
                                ,font="-family {Product Sans} -size 18 -weight normal"
                                ,highlightbackground="#d9d9d9"
                                ,foreground="#800040"
                                ,text='''Checker''')
        self.Label1_4.place(relx=0.554, rely=0.036, height=31, width=104)
        
        self.Select = tk.Label(top,activebackground="#f9f9f9"
                                
                                ,background="#d9d9d9"
                                ,disabledforeground="#a3a3a3"
                                ,font="-family {Product Sans} -size 18 -weight normal"
                                ,highlightbackground="#d9d9d9"
                                ,foreground="#800040"
                                ,text='''Select\n And Press the Button\n To Get the Date''')
        self.Select.place(relx=0.554, rely=0.236, height=300, width=250)
        
        ####
        
        
        self.cal = Calendar(top, date_pattern = 'dd/mm/yy')
        self.cal.place(relx=0.100, rely=0.300)
        
        
        
        ####

        self.Button1 = tk.Button(top, command = Show )
        self.Button1.place(relx=0.316, rely=0.877, height=54, width=227)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#800040")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(font="-family {Product Sans} -size 18 -weight normal")
        self.Button1.configure(foreground="#ffffff")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Check Attendance''')



        top.mainloop()
        mydb.close()








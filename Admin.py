import tkinter as tk
import mysql.connector as connector
from tkinter import messagebox
import MainPage
import KeyInputPage


class Admin:
    def __init__(self):
        
        
        
        mydb= connector.connect(host = "localhost", user= "root", passwd = "aayush123", database="testdb")
        cursor = mydb.cursor()
        
        def ChangeSettings():
            top.destroy()
            KeyInputPage.InputKey()
            
        
        def check(u,p):
            print(u,p)
            
            q = "select Id from admin where username = '{}' and BINARY password like '{}'".format(u,p)
            print(q)
            
            cursor.execute(q)
            result = cursor.fetchone()
            
            if result != None:
                
                Admin_id = result[0]
                
                messagebox.showinfo("Authentication Success", "You are now logged in ID : {}".format(Admin_id))
                
                top.destroy()
#                root.destroy()
                MainPage.MAINCALL(Admin_id)
                
                
                
                
                
                
            else:
                
                messagebox.showinfo("Authentication Failure", "No match found" )
                
                
            
            
            
            
        
        
        
        
#        root = tk.Tk()
#        root.withdraw()

        
        top = tk.Tk()
#        top.protocol("WM_DELETE_WINDOW", root.destroy)
        
        top.geometry("433x300+638+321")
        
        top.resizable(0, 0)
        top.title("Admin Page")
        top.configure(background="#d9d9d9")

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.3, rely=0.067, height=38, width=81)
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font="-family {Product Sans} -size 19 -weight bold")
        self.Label1.configure(foreground="#800040")
        self.Label1.configure(text='''Admin''')

        self.Label1_1 = tk.Label(top)
        self.Label1_1.place(relx=0.492, rely=0.067, height=38, width=71)
        self.Label1_1.configure(activebackground="#f9f9f9")
        self.Label1_1.configure(activeforeground="black")
        self.Label1_1.configure(background="#d9d9d9")
        self.Label1_1.configure(disabledforeground="#a3a3a3")
        self.Label1_1.configure(font="-family {Product Sans} -size 19 -weight bold")
        self.Label1_1.configure(foreground="#000000")
        self.Label1_1.configure(highlightbackground="#d9d9d9")
        self.Label1_1.configure(highlightcolor="black")
        self.Label1_1.configure(text='''Login''')

        self.Label2 = tk.Label(top)
        self.Label2.place(relx=0.069, rely=0.377, height=22, width=89)
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font="-family {Product Sans} -size 13 -weight normal ")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text='''Username''')

        self.Label2_5 = tk.Label(top)
        self.Label2_5.place(relx=0.069, rely=0.57, height=22, width=89)
        self.Label2_5.configure(activebackground="#f9f9f9")
        self.Label2_5.configure(activeforeground="black")
        self.Label2_5.configure(background="#d9d9d9")
        self.Label2_5.configure(disabledforeground="#a3a3a3")
        self.Label2_5.configure(font="-family {Product Sans} -size 13 -weight normal ")
        self.Label2_5.configure(foreground="#000000")
        self.Label2_5.configure(highlightbackground="#d9d9d9")
        self.Label2_5.configure(highlightcolor="black")
        self.Label2_5.configure(text='''Password''')

        self.Entry1 = tk.Entry(top)
        self.Entry1.place(relx=0.323, rely=0.363,height=30, relwidth=0.61)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(insertbackground="black")

        self.Entry1_11 = tk.Entry(top, show = "*")
        self.Entry1_11.place(relx=0.326, rely=0.557,height=30, relwidth=0.356)
        self.Entry1_11.configure(background="white")
        self.Entry1_11.configure(disabledforeground="#a3a3a3")
        self.Entry1_11.configure(font="TkFixedFont")
        self.Entry1_11.configure(foreground="#000000")
        self.Entry1_11.configure(highlightbackground="#d9d9d9")
        self.Entry1_11.configure(highlightcolor="black")
        self.Entry1_11.configure(insertbackground="black")
        self.Entry1_11.configure(selectbackground="#c4c4c4")
        self.Entry1_11.configure(selectforeground="black")

        self.Button1 = tk.Button(top, command = lambda : check(self.Entry1.get(), self.Entry1_11.get()))
        self.Button1.place(relx=0.393, rely=0.767, height=54, width=117)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#800040")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(font="-family {Product Sans} -size 17 -weight normal")
        self.Button1.configure(foreground="#ffffff")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Access''')
        
        self.Image1 = tk.PhotoImage(file = r"../DATA/setadmin.png")
        self.Image1 = self.Image1.subsample(10)
        self.SetAdminButton = tk.Button(top, image = self.Image1, command = ChangeSettings )
        self.SetAdminButton.place(relx = 0.02, rely = 0.9)
        

        
        top.mainloop()
    

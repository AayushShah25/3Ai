import tkinter as tk
from tkinter import messagebox

import mysql.connector as connector

class AdminADD:
    
    
    IsEnabled = False
    def __init__(self):
        
        
        def Add():
            
            if NameEntry.get().strip() == '' or PEntry.get() == '' or RePasswordEntry.get() == '':
                messagebox.showwarning("Add Details", "Please Fill all the fields")
                
                
            elif PEntry.get() != RePasswordEntry.get():
                messagebox.showwarning("Not Matched","Passwords are not matched - Kindly use the SHOW button for Clear the input.")
                
            
            
            elif NameEntry.get().strip().upper() == "TemproryProject with KAKA".upper():
                messagebox.showwarning("The Name Error", " You can't FOOL me ! \nDon't use the Key as a username")
                
            else:
                
                mydb= connector.connect(host = "localhost", user= "root", passwd = "aayush123", database="testdb")
                cursor = mydb.cursor()
        
                q= "select username from admin where isin = true"
                
        
                cursor.execute(q)
                
                re= cursor.fetchall()
                mydb.close()
                
                if NameEntry.get().upper() in [NAME[0].upper() for NAME in re]:
                    messagebox.showwarning("Already Taken Name", "Please take different Username")
                    
                    
                else:
                    
                    q="insert into admin(username,password) values ( '{}' , '{}' )".format(str(NameEntry.get().strip()) , str(PEntry.get()))
                    print (q)
                    mydb= connector.connect(host = "localhost", user= "root", passwd = "aayush123", database="testdb")
                
                    cursor = mydb.cursor()
                    cursor.execute(q)
                    
                    messagebox.showinfo("Entry Success", "The New Admin has successfully joined the Unit")
                    mydb.commit()
                    mydb.close()
                    root.destroy()
                
                
                
                
                
                
                
                
            
            
            
            
        def ShowHide():
            
            if self.IsEnabled == False:
                PEntry.configure(show = '')
                RePasswordEntry.configure(show = '')
                ShowHideButton.configure(text = 'H\nI\nD\nE')
                self.IsEnabled = True
                
            else:
                
                PEntry.configure(show = '*')
                RePasswordEntry.configure(show = '*')
                ShowHideButton.configure(text = 'S\nH\nO\nW')
                self.IsEnabled = False
                
                
        
        
        root = tk.Tk()
        root.title("Admin Entry Page")
        root.geometry("375x370+600+250")
        root.resizable(0,0)
        root.configure(background = "#d9d9d9")
                       
                       
        #Element Section
        
        AdminEntryLabel = tk.Label(root, text = "Admin Entry", fg = "#800040", font = "-family {Product Sans} -size 15 -weight bold", bg = "#d9d9d9").place(relx=0.17,rely=0.04)
        PageLabel = tk.Label(root, text = "Page", font = "-family {Product Sans} -size 15 -weight bold", bg = "#d9d9d9").place(relx=0.49,rely=0.04)
                             
        IDLabel = tk.Label(root, text ="Admin ID", font = "-family {Product Sans} -size 15", bg = "#d9d9d9").place(relx = 0.05,rely=0.15)
        IDEntry = tk.Entry(root,font = "-family {Product Sans} -size 15")
        IDEntry.place(relx=0.46,rely=0.15, width = 100)
        
        mydb= connector.connect(host = "localhost", user= "root", passwd = "aayush123", database="testdb")
        cursor = mydb.cursor()
        
        q= "select count(ID) from admin"
        
        cursor.execute(q)
        
        upcomindId = int(cursor.fetchone()[0]) + 1
        
        IDEntry.delete(0,"end")
        IDEntry.insert(0,upcomindId)
        IDEntry.configure(state = "disabled")
        
        mydb.close()
        
        
        AdminNameLabel = tk.Label(root, text ="Admin Name", font = "-family {Product Sans} -size 15", bg = "#d9d9d9").place(relx = 0.05,rely=0.3)
        NameEntry = tk.Entry(root,font = "-family {Product Sans} -size 15")
        NameEntry.place(relx=0.46,rely=0.3, width = 150)
        
        
        PLabel = tk.Label(root, text ="Password", font = "-family {Product Sans} -size 15", bg = "#d9d9d9").place(relx = 0.05,rely=0.47)
        PEntry = tk.Entry(root,font = "-family {Product Sans} -size 15", show = "*")
        PEntry.place(relx=0.46,rely=0.47, width = 150)
        
        RePasswordLabel = tk.Label(root, text ="Type Again", font = "-family {Product Sans} -size 15", bg = "#d9d9d9").place(relx = 0.05,rely=0.63)
        RePasswordEntry = tk.Entry(root,font = "-family {Product Sans} -size 15", show = "*")
        RePasswordEntry.place(relx=0.46,rely=0.63, width = 150)
        
        
        ShowHideButton = tk.Button(root,text ="S\nH\nO\nW", command = ShowHide , background = "#800040", foreground = "#ffffff", font ="-family {Product Sans} -size 12 -weight bold")
                                   
        ShowHideButton.place(relx = 0.9,rely = 0.46)
        
        
        AddButtonKAKA = tk.Button(root, text="Add", command = Add, background = "#800040", foreground = "#ffffff",font ="-family {Product Sans} -size 12 -weight bold" )
                                  
        AddButtonKAKA.place(relx = 0.34, rely = 0.87, width = 150)
        
        root.mainloop()
        
    
    
    
    
    
    

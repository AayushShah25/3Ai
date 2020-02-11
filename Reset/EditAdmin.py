import tkinter as tk
from tkinter import messagebox 

import mysql.connector as connector
import Selecttask

class EditAdmin:
    
    
    
    
    def __init__(self):
        
        
        def onmainpage():
            
            root.destroy()
            Selecttask.SelecttheTask()
        def EditPassword():
            
            name = UsernameEntry.get()
            newpassword = PasswordEntry.get()
            renewpassword = Password2Entry.get()
            
            if newpassword == '' or renewpassword == '' or name == '':
                messagebox.showwarning("Please Enter data", "Please Fill the fields with the appropriate data")
                
                
            else:
                
                mydb= connector.connect(host = "localhost", user= "root", passwd = "aayush123", database="testdb")
                cursor = mydb.cursor()
                
                q = "select Id from admin where username = '{}' and isin = true".format(name)
                
                 
                cursor.execute(q)
                result = cursor.fetchone()
                 
                if result == None:
                     messagebox.showerror("No User","No user for this username")
                     
                 
                     
                     
                
                elif newpassword != renewpassword:
                    messagebox.showinfo("Not Matched","The password are not matching")
                else:
                    mydb= connector.connect(host = "localhost", user= "root", passwd = "aayush123", database="testdb")
                    cursor = mydb.cursor()
                
                    q = "update admin set password = '{}' where id = '{}'".format(newpassword,result[0])
                    cursor.execute(q)
                    mydb.commit()
                    mydb.close()
                
                
                    messagebox.showinfo("DONE", "The password is changed for the person ")
                    
                     
                     
                     
                     
                     
                     
                     
                     
                     
                     
                     
                     
        root = tk.Tk()
        root.title("Admin Entry Page")
        root.geometry("430x290+600+250")
        root.resizable(0,0)
        root.configure(background = "#d9d9d9")
        root.protocol("WM_DELETE_WINDOW", onmainpage)
        
                       
        _ = tk.Label(root, text = " ",bg = "#d9d9d9").grid(row =0 , column = 0, padx = 2, columnspan = 1)
        TitleLabel = tk.Label(root, text = "Admin Removal", fg = "#800040", bg = "#d9d9d9",
                              font = "-family {Product Sans} -size 15 -weight bold").grid(row = 0, column = 1, columnspan = 2)
        
        PAgeLabel = tk.Label(root, text = "Page", bg = "#d9d9d9",
                              font = "-family {Product Sans} -size 15 -weight bold").grid(row = 0, column = 2, columnspan = 2)
                       
        
        UsernameLabel = tk.Label(root, text = "Username", bg = "#d9d9d9",font = "-family {Product Sans} -size 15 -weight normal")
        UsernameLabel.grid(row = 1, column = 1,padx = 1, pady = 15)
        
        UsernameEntry = tk.Entry(root, font = "-family {Product Sans} -size 12 -weight bold")
        UsernameEntry.grid(row = 1, column = 2, columnspan = 2, pady = 10 , padx  = 10)
        
        
        PasswordLabel = tk.Label(root, text = "Password", bg = "#d9d9d9",font = "-family {Product Sans} -size 15 -weight normal")
        PasswordLabel.grid(row = 2, column = 1)
                                 
        PasswordEntry = tk.Entry(root, font = "-family {Product Sans} -size 12 -weight bold")
        PasswordEntry.grid(row = 2, column = 2, columnspan = 2, pady = 10)
        
        Password2Label = tk.Label(root, text = "Again Password", bg = "#d9d9d9",font = "-family {Product Sans} -size 15 -weight normal")
        Password2Label.grid(row = 3, column = 1)
                                 
        Password2Entry = tk.Entry(root, font = "-family {Product Sans} -size 12 -weight bold")
        Password2Entry.grid(row = 3, column = 2, columnspan = 2, pady = 15)
                       
                
        
        
        
        
        
        RemoveButton = tk.Button(root, text = "Change password in one Click", background =  "#800040", foreground = "#d9d9d9"
                                 ,font = "-family {Product Sans} -size 15 -weight bold"
                                 ,command = EditPassword)
        RemoveButton.grid(row = 4, column = 0,columnspan = 4, pady = 40, padx = 50, sticky = "n")
        root.mainloop()
    
        root.mainloop()

import tkinter as tk
from tkinter import messagebox

import mysql.connector as connector
import Selecttask
class RemoveAdmin:
    
    def __init__(self):
        
        def onmainpage():
            
            root.destroy()
            Selecttask.SelecttheTask()
        root = tk.Tk()
        root.title("Admin Entry Page")
        root.geometry("375x290+600+250")
        root.resizable(0,0)
        root.configure(background = "#d9d9d9")
        root.protocol("WM_DELETE_WINDOW", onmainpage)
        
        def Remove():
            name = UsernameEntry.get().strip()
            password = PasswordEntry.get()
            
            if name == '' or password == '':
                messagebox.showwarning("Please Enter data", "Please Fill the fields with the appropriate data")
                
            else:
                
                 mydb= connector.connect(host = "localhost", user= "root", passwd = "aayush123", database="testdb")
                 cursor = mydb.cursor()
                 
                 
                 q = "select Id from admin where username = '{}' and BINARY password like '{}' and isin = true".format(name,password)
                 
                 cursor.execute(q)
                 result = cursor.fetchone()
                 print(result)
                 
                 if result == None:
                     messagebox.showerror("Not Found","The Username and password are not matched")
                     
                 elif messagebox.askyesno("Delete or Not" ,"Do you really want to delete an Admin {} of id {} ?".format(name, result[0])):
                     
                     cursor = mydb.cursor()
                     q = "update admin set isin = false where id = {} and isin = true".format(result[0])
                     cursor.execute(q)
                     mydb.commit()
                     mydb.close()
                     messagebox.showinfo("Done", "The Admin is removed successfully")
                    
                 
                       
        _ = tk.Label(root, text = " ",bg = "#d9d9d9").grid(row =0 , column = 0, padx = 2, columnspan = 1)
        TitleLabel = tk.Label(root, text = "Admin Removal", fg = "#800040", bg = "#d9d9d9",
                              font = "-family {Product Sans} -size 15 -weight bold").grid(row = 0, column = 1, columnspan = 2)
        
        PAgeLabel = tk.Label(root, text = "Page", bg = "#d9d9d9",
                              font = "-family {Product Sans} -size 15 -weight bold").grid(row = 0, column = 2, columnspan = 2)
                       
        
        UsernameLabel = tk.Label(root, text = "Username", bg = "#d9d9d9",font = "-family {Product Sans} -size 15 -weight normal").grid(row = 1, column = 1,padx = 1, pady = 30)
                                 
        UsernameEntry = tk.Entry(root, font = "-family {Product Sans} -size 12 -weight bold")
        UsernameEntry.grid(row = 1, column = 2, columnspan = 2, pady = 20 , padx  = 10)
        
        
        PasswordLabel = tk.Label(root, text = "Password", bg = "#d9d9d9",font = "-family {Product Sans} -size 15 -weight normal").grid(row = 2, column = 1)
                                 
                                 
        PasswordEntry = tk.Entry(root, font = "-family {Product Sans} -size 12 -weight bold")
        PasswordEntry.grid(row = 2, column = 2, columnspan = 2, pady = 10)
                       
                
        
        
        RemoveButton = tk.Button(root, text = "Remove", background =  "#800040", foreground = "#d9d9d9"
                                 ,font = "-family {Product Sans} -size 15 -weight bold",
                                 command = Remove).grid(row = 3, column = 0,columnspan = 5, pady = 60, padx = 70)
        root.mainloop()
    
    
    


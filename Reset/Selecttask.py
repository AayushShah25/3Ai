import tkinter as tk
from tkinter import messagebox
import adminadd
import EditAdmin 
import removeAdmin
import Admin

class SelecttheTask:
    
    
    def __init__(self):
        
        
        def taskSelect(n):
            
            root.destroy()
            temp.destroy()
            if n == 1:
                adminadd.AdminADD()
            elif n == 2:
                EditAdmin.EditAdmin()
            elif n == 3:
                removeAdmin.RemoveAdmin()
                
                
                
                
        def opengood():
            
            temp.destroy()
            Admin.Admin()
            
        temp = tk.Tk()
        temp.withdraw()
        root = tk.Toplevel(temp)
        root.geometry("600x300+600+340")
        root.configure(background = "#d9d9d9")
        root.title("Select the Task")
        root.resizable(0,0)      
        root.protocol("WM_DELETE_WINDOW", opengood)
                       
                       
#Elements Area
        
        
        t = tk.Label(root, bg = "#d9d9d9").grid(row =0, column = 0 , padx = 25)
        image = tk.PhotoImage(file = r"../DATA/AddAdmin.png")               
        image = image.subsample(4)
        
        AddNewButton = tk.Button(root, image = image,command = lambda : taskSelect(1))               
        AddNewButton["bg"] = "#d9d9d9"
        AddNewButton["border"] = "0"
        AddNewButton.grid(row = 0, column = 1)
        
        image1 = tk.PhotoImage(file = r"../DATA/EditPassword.png")               
        image1 = image1.subsample(4)
        
        EditButton = tk.Button(root, image = image1,command = lambda : taskSelect(2))               
        EditButton["bg"] = "#d9d9d9"
        EditButton["border"] = "0"
        EditButton.grid(row = 0, column = 2)
        
        image2 = tk.PhotoImage(file = r"../DATA/RemoveAdmin.png")               
        image2 = image2.subsample(4)
        
        RemoveButton = tk.Button(root, image = image2,command = lambda : taskSelect(3))               
        RemoveButton["bg"] = "#d9d9d9"
        RemoveButton["border"] = "0"
        RemoveButton.grid(row = 0, column= 3, pady = 38)
        
        
        SelectTaskLabel = tk.Label(root, text = "Select the Task to proceed Ahead", font = "-family {Product Sans} -size 20 -weight bold", bg = "#d9d9d9" ).grid(row = 1, column= 1, columnspan = 4, padx = 50 )
        
        
        root.mainloop()
        
        

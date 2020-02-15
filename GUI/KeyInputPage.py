import tkinter as tk
from tkinter import messagebox
import Selecttask
import Admin
class InputKey:
    
    
    
    
            
        
        
    IsEnabled = False
     
    def __init__(self):
                
        
        def Showtext():
            
            if self.IsEnabled == False : EnteryField.configure(show = "") ; ShowTextButton.configure(text = "Hide Text") ; self.IsEnabled = True;
            else: EnteryField.configure(show = "*"); ShowTextButton.configure(text = "See Text") ; self.IsEnabled = False
            
        def KeyCheck():
            
            key = str(EnteryField.get())
            
            if key != "TemproryProject with KAKA":
                messagebox.showinfo("Error", "No key found related to your input !")
            
            else:
                root.destroy()
                Selecttask.SelecttheTask()
            
            
            
        def opengood():
            root.destroy()
            Admin.Admin()
            
        root = tk.Tk()
        root.title("Admin Reset Page")
        root.geometry("450x200+600+340")
        root.configure(background = "#d9d9d9")
        root.resizable(0,0)  
        root.protocol("WM_DELETE_WINDOW", opengood)
        
        
        TLabel = tk.Label(root, text = "", bg = "#d9d9d9").grid(row = 0 , column = 0, padx = 50)               
                          
        AdminLabel = tk.Label(root, text = "Admin", bg = "#d9d9d9",font="-family {Product Sans} -size 19 -weight bold", fg = "#800040").grid(row = 0 , column = 1, pady = 10)
        ResetLabel = tk.Label(root, text = "Reset Settings", bg = "#d9d9d9", font="-family {Product Sans} -size 19").grid(row = 0 , column = 2)                      
                              

                          
        KeyLabel = tk.Label(root, text = "Key", bg = "#d9d9d9", font="-family {Product Sans} -size 12 -weight bold").grid(row = 1 , column =0, pady = 30)
        EnteryField = tk.Entry(root, font = "-family {Product Sans} -size 15", show = "*")
        EnteryField.grid(row = 1, column = 1, columnspan = 2)

        
        ShowTextButton = tk.Button(root, text = "See Text", background = "#800040", foreground = "#ffffff", font = "-family {Product Sans} -size 12 -weight bold", command = Showtext)
        ShowTextButton.grid(row = 2, column = 0, pady = 5, sticky = "e")
        
        Temp2 = tk.Label(root, text = " ", bg = "#d9d9d9").grid(row = 2, column = 1, pady = 5, sticky= "e")
        Check = tk.Button(root, text = "Check", background = "#800040", foreground = "#ffffff", font = "-family {Product Sans} -size 12 -weight bold", command = KeyCheck, width = 15).grid(row = 2, column = 2, pady = 5, columnspan = 3, padx = 60, sticky= "e")
        
        
        
        
        
        
        root.mainloop()
        
        

        
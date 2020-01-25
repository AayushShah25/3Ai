import tkinter as tk
from tkinter import ttk
from tkinter import *
from datetime import datetime
from tkinter import messagebox
from WorkingForGoodReports import ShowGraph
import mysql.connector as connector
import MainPage

class Generate:
    def __init__(self, Admin_id):

        
        def on_close():
             
            top.destroy()
            MainPage.MAINCALL(Admin_id)
        
        top = tk.Tk()
        top.geometry("602x279+650+150")
        top.minsize(124, 1)
        top.maxsize(1916, 1053)
        top.resizable(0, 0)
        top.title("Generate Report")
        top.configure(background="#d9d9d9")
                      
        top.protocol("WM_DELETE_WINDOW",on_close)
                     
                      
                     
                             
    
                      


        months = ['January','February', 'March', 'April', 'May', 'June', 'July', 'August' , 'September', 'October', 'November', 'December']
        years = list(range(2020,2099))
        
        kaka = datetime.now()
        #m_selected = kaka.strftime("%B")
        #y_selected = kaka.strftime("%Y")
        def printing():
            
            
            if selected_m.get() == '' or selected_y.get() == '':
                
                messagebox.showerror("Selection Error", " Please Select all the required fields !! ")
                return 0
            
            
            print("Selected : ", selected_m.get(),selected_y.get())
            
            mydb= connector.connect(host = "localhost", user= "root", passwd = "aayush123", database="testdb")
            cursor = mydb.cursor()
            
            
            cursor.execute("select count(date_of_attendance) from great_attendance where date_of_attendance in (select date_of_attendance where month(str_to_date(date_of_attendance,'%d%m%y')) = {} and year(str_to_date(date_of_attendance,'%d%m%y')) = 20{} )".format(months.index(selected_m.get())+1,selected_y.get()[2:]))
            
            result = cursor.fetchone()
            
            if result[0] == 0:
                messagebox.showerror("No Records found " , "No Records found for the Selected month and year")
                return 0
            
            
            
            
            ShowGraph(months.index(selected_m.get())+1 , selected_y.get()[2:], selected_m.get(), Admin_id)
            
            
            
                
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
        selected_m = StringVar(top)
        self.TCombobox1 = ttk.Combobox(top, value = months)
        
        self.TCombobox1.configure(state = "readonly")
        self.TCombobox1.place(relx=0.133, rely=0.466, relheight=0.147
                , relwidth=0.304)
        self.TCombobox1.configure(textvariable=selected_m)
        self.TCombobox1.configure(takefocus="")



        selected_y = StringVar(top)
        self.TCombobox1_2 = ttk.Combobox(top, values = years)
        
        self.TCombobox1_2.configure(state = "readonly")
        self.TCombobox1_2.place(relx=0.615, rely=0.466, relheight=0.147
                , relwidth=0.171)
        self.TCombobox1_2.configure(textvariable=selected_y)
        self.TCombobox1_2.configure(takefocus="")
        
        
        
        

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.083, rely=0.072, height=31, width=284)
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font= "-family {Product Sans} -size 22 -weight normal " )
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''Select Month & Year''')

        self.Label2 = tk.Label(top)
        self.Label2.place(relx=0.453, rely=0.215, height=42, width=273)
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font= "-family {Product Sans} -size 22 -weight normal " )
        self.Label2.configure(foreground="#800040")
        self.Label2.configure(text='''To Generate A Report''')

        self.Button1 = tk.Button(top, command=printing)
        self.Button1.place(relx=0.432, rely=0.753, height=44, width=97)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#800040")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(font= "-family {Product Sans} -size 18 -weight normal " )
        self.Button1.configure(foreground="#ffffff")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Get it !''')

        top.mainloop()






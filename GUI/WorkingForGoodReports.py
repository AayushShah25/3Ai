import mysql.connector as connector
import ast


import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import matplotlib
matplotlib.use("TkAgg")
import tkinter as tk
import MainPage
from tkinter import ttk




def ShowGraph(month, year, name, Admin_id):
    
    
   
        
    mydb= connector.connect(host = "localhost", user= "root", passwd = "aayush123", database="testdb")
    cursor = mydb.cursor()
    
    
 
     
    
    q = "select * from great_attendance where date_of_attendance in (select date_of_attendance where month(str_to_date(date_of_attendance,'%d%m%y')) = {} and year(str_to_date(date_of_attendance,'%d%m%y')) = 20{} )".format(month,year)
    print(q)
    
    cursor.execute(q)
    
    recordsforreport = cursor.fetchall()
    
    
    
    master = {}
    
    
    for record in recordsforreport:
        
        date = record[0]
        info = record[1]
        master[date] = {}
        for k,v in ast.literal_eval(info).items():
            
            master[date][k]= v[0]
            
            
    info = {}
    
    for i in master.values():
        for k in i.keys():
            info[k] = 0
    
    for i in master.values():
        for k,v in i.items():
            
            info[k] += v
            
            
            
    root = tk.Tk()
    root.title("Graph")
    

    
    
    from matplotlib.pyplot import cm
    import numpy as np
    color=cm.rainbow(np.linspace(0,1,len(list(info.keys()))+1))
    
    f = Figure(figsize = (5,5), dpi = 100)
    a = f.add_subplot(111)
    
    a.bar(list(info.keys()), list(info.values()), color = color)
    
    a.set_title(name)
    a.set_xlabel('Employees')
    a.set_ylabel('Attendance')
    canvas = FigureCanvasTkAgg(f, master=root)
    canvas.draw()
    canvas.get_tk_widget().pack(side = tk.TOP, fill = tk.BOTH, expand = True)
    
    toolbar = NavigationToolbar2Tk(canvas, root)
    toolbar.update()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
    
    view = ttk.Treeview(root)
    view.pack(side = tk.LEFT, fill = tk.BOTH, expand = True)
    
    view.config(column = ('name', 'attend'))
    
    
    view.heading('#0', text = "ID" , anchor = 'center')
    view.heading('name', text = "Name" , anchor = 'center')
    view.heading('attend', text = "Attend" , anchor = 'center')
    
    
    name_id = tuple(info.keys())
    
    
    q = "select name from userse where id in"+str(name_id)
    cursor.execute(q)
    names = cursor.fetchall()
    names = sum(names , () )
    
    
    
    for i,kv in enumerate(info.items()):
        
        view.insert('', 'end', text = kv[0], values = (names[i],kv[1]))
    
    
    vscrollbar = ttk.Scrollbar(root, orient= "vertical", command = view.yview)
    vscrollbar.pack(side = tk.RIGHT, fill = 'y')
    
    
    
    view.configure(yscrollcommand= vscrollbar.set)
    
    root.mainloop()
    
    
    # Info is the Final Dict which has all the Data with the respective ID



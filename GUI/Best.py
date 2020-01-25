import tkinter as tk
import tkinter.ttk as ttk
import mysql.connector as connector
import ast

def showAttendance(date):
    
    mydb= connector.connect(host = "localhost", user= "root", passwd = "aayush123", database="testdb")
    cursor = mydb.cursor()
    
    q= "select * from great_attendance where date_of_attendance = "+str(date)
    cursor.execute(q)
    result = cursor.fetchone()
    id_and_attend = result[1]
    id_and_attend = ast.literal_eval(id_and_attend)
    
    name_id = tuple(id_and_attend.keys())
    
    
    q = "select name from userse where id in"+str(name_id)
    cursor.execute(q)
    names = cursor.fetchall()
    names = sum(names , () )
    
    final_dict = {}
    
    for i in zip(id_and_attend,zip(names, id_and_attend.values() ) ):
        final_dict[i[0]] = i[1]
    
    
    
    
    
    
    root = tk.Tk()
    root.title("The Attendance Sheet")
    root.resizable(0,0)
    
    view = ttk.Treeview(root)
    view.pack(side = tk.LEFT)
    
    vscrollbar = ttk.Scrollbar(root, orient= "vertical", command = view.yview)
    vscrollbar.pack(side = tk.RIGHT, fill = 'y')
    
    view.config(column = ('name', 'attend', 'attend_time'))
    
    view.configure(yscrollcommand= vscrollbar.set)
    view.heading('#0', text = "ID" , anchor = 'center')
    view.heading('name', text = "Name" , anchor = 'center')
    view.heading('attend', text = "Attend" , anchor = 'center')
    view.heading('attend_time', text = "Attend Time" , anchor = 'center')
    
    
    for i in final_dict.items():
        view.insert('','end' ,text = i[0], values = (i[1][0],i[1][1][0],i[1][1][1]))
    
    root.mainloop()
    mydb.close()

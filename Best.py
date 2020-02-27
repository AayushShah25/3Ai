import tkinter as tk
import tkinter.ttk as ttk
import mysql.connector as connector
import ast
from tkinter import messagebox
# from tkcalendar import *

def showAttendance(date):
        
    def OnDoubleClick(event):
        
        print(id_and_attend)
        
        try:
            item = view.selection()[0]
            root.withdraw()

        except Exception:
            item = view.selection()
            
        
        if str(type(item)) == "<class 'tuple'>":
            pass

        else:

            if messagebox.askyesno("Really Delete ?", "Do you really want to delete the attendance of ID {} \n for the date {} ?".format(view.item(item,"text"),date[:2] + " - "+ date[2:4] + " - 20"+ date[4:])):
                id_and_attend[ int(view.item(item,"text")) ] = [0,0]
                print(id_and_attend)
                
                
                cursor = mydb.cursor()
                q = "update great_attendance set summary_of_daily_attendance = %s where date_of_attendance = %s"
                val = [(str(id_and_attend), date)]
                
                cursor.executemany(q,val)
                mydb.commit()
                
                messagebox.showinfo("Done","The attendance has been updated")
                root.destroy()
            else:
                root.deiconify()
                
                
                
              
    def OnDoubleClickAdd(event):
        
            
        root.withdraw()
        def saveData():
            if HH.get() == '' or MM.get() == '' or SS.get() == '':
                messagebox.showerror("Select Value","Please select the value for the time")
            else:
                
                cursor = mydb.cursor()
                print(id_and_attend)
                Hformat = int(hh.get())
                Mformat = int(mm.get())
                Sformat = int(ss.get())
                
                if Hformat < 10:
                    Hformat = "0"+str(Hformat)
                
                if Mformat < 10:
                    Mformat = "0"+str(Mformat)
                    
                if Sformat < 10:
                    Sformat = "0"+str(Sformat)
                    
                id_and_attend[ int(view.item(item,"text")) ] = [1, str(Hformat) +":"+ str(Mformat) +":"+ str(Sformat) ]
                
                cursor = mydb.cursor()
                q = "update great_attendance set summary_of_daily_attendance = %s where date_of_attendance = %s"
                val = [(str(id_and_attend), date)]
                
                cursor.executemany(q,val)
                mydb.commit()
                print(id_and_attend)
                messagebox.showinfo("Done","The attendance has been updated")
                EditWindow.destroy()
                root.destroy()
                
                
                
                    
                
                
            
        try:
            item = view.selection()[0]
    
        except Exception:
            item = view.selection()
        
        if str(type(item)) == "<class 'tuple'>":
            pass
        
        else:
            
            def onclose():
                EditWindow.destroy()
                root.deiconify()
                
            EditWindow = tk.Toplevel()
            EditWindow.title("Edit the Attendance")
            EditWindow.geometry("500x500+300+120")
            
            EditWindow.protocol("WM_DELETE_WINDOW",onclose)
            EditWindow.resizable(0,0)
            
            tk.Label(EditWindow, text = "You are presenting" , font = "-family {product sans} -size 18").place(relx = 0.01, rely = 0.06)
            tk.Label(EditWindow, text = "ID : {} ".format(view.item(item,"text")),font = "-family {product sans} -size 18 -weight bold", fg = "#800040").place(relx = 0.46, rely = 0.06)
            
            
    # #        print("you clicked on", view.item(item,"text"))
            
            
            tk.Label(EditWindow, text = "On Date : {} ".format(date[:2] + " - "+ date[2:4] + " - 20"+ date[4:] ),font = "-family {product sans} -size 18", fg = "#800040").place(relx = 0.1, rely = 0.2)
    #        present = ["Present","Absent"]
    #        tk.Label(EditWindow, text = "Select the Attendance", font = "-family {product sans} -size 12").place(relx = 0.01, rely = 0.4)
    #        SelectAttendance = ttk.Combobox(EditWindow, value = present, state = "readonly")
            
    #        SelectAttendance.place(relx = 0.38, rely = 0.4)
            
            tk.Label(EditWindow, text ="Enter the time",font = "-family {product sans} -size 12").place(relx = 0.01, rely = 0.6)
            
            tk.Label(EditWindow, text ="HH",font = "-family {product sans} -size 12").place(relx = 0.3, rely = 0.6)
            hh = tk.StringVar(EditWindow)
            hValues = list(range(24))
            HH =ttk.Combobox(EditWindow, value = hValues, state = "readonly", textvariable = hh)
            HH.place(relx = 0.38, rely = 0.6, width = 50)
    
            tk.Label(EditWindow, text ="MM",font = "-family {product sans} -size 12").place(relx = 0.48, rely = 0.6)
            mm = tk.StringVar(EditWindow)
            mValues = list(range(60))
            MM = ttk.Combobox(EditWindow, value = mValues, state = "readonly", textvariable = mm)
            MM.place(relx = 0.55, rely = 0.6, width = 50)
    
            tk.Label(EditWindow, text ="SS",font = "-family {product sans} -size 12").place(relx = 0.65, rely = 0.6)
            ss = tk.StringVar(EditWindow)
            sValues = list(range(60))
            SS = ttk.Combobox(EditWindow, value = sValues, state = "readonly", textvariable = ss)
            SS.place(relx = 0.7, rely = 0.6, width = 50)
    
    #        cal = Calendar(EditWindow, date_pattern = 'dd/mm/yy').place(relx = 0.2, rely = 0.70)
    
            tk.Button(EditWindow, text = "Save Edited Values", background = "#800040", foreground = "white",
                font = "-family {product sans} -size 12 -weight bold", command = saveData).place(relx = 0.4, rely = 0.75)
    
    
    
    
    
    
    
    
    
            EditWindow.mainloop()
            
            
        
        
      
    mydb = connector.connect(host = "localhost", user= "root", passwd = "aayush123", database="testdb")
    cursor = mydb.cursor()
    
    q= "select * from great_attendance where date_of_attendance = "+str(date)
    cursor.execute(q)
    result = cursor.fetchone()
    
    id_and_attend = result[1]
    id_and_attend = ast.literal_eval(id_and_attend)
    
    name_id = tuple(id_and_attend.keys())
    if len(name_id) == 1:
        q = "select name from userse where id in ("+str(name_id[0])+")"
    
    else:
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
    tk.Label(root, text ="Double Left click - Add an Attendance                                    Double Right click - Remove an Attendance").pack()
    view = ttk.Treeview(root)
    view.pack(side = tk.LEFT)
    view.bind("<Double-3>",  OnDoubleClick)
    view.bind("<Double-1>",  OnDoubleClickAdd)

    
    
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



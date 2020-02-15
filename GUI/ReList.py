import tkinter as tk
import mysql.connector as connector
import os
from tkinter import messagebox

import MainPage




class ListKAKA:
    def __init__(self,Admin_id):

        mydb = connector.connect(host="localhost", user ="root", passwd="aayush123" , database="testdb")
        cursor = mydb.cursor()

        q = "select ID,name,age,gender,post,contact,address,isin,hold from userse where isin=1 and hold=1"
        print(q)
        cursor.execute(q)
        Data = cursor.fetchall()
        print(Data)



        def release(id):
            mydb = connector.connect(host="localhost", user ="root", passwd="aayush123" , database="testdb")
            cursor = mydb.cursor()
            
            q = "update userse set hold = false where id="+str(id)
            cursor.execute(q)
            mydb.commit()



            q = "select name from userse where id="+str(id)
            cursor.execute(q)
            

            result = cursor.fetchall()
            result=result[0][0]
            top.destroy()
            
            ## Updating the Attendance Data
            
            checkTable = "select count(ID) from attendance"
            
            cursor.execute(checkTable)
            isthere =  cursor.fetchone()[0]
            
            
            if isthere != 0:
                
                print ("Inside of the Attendance Update : " , id)
                q = "update attendance set hold = false where id="+str(id)
                print(" The  q : ", q)
                cursor.execute(q)
                mydb.commit()
                
                
            messagebox.showinfo("Hold ","The Person "+result+" of ID : "+str(id)+" Has been released from hold...")
            
            top.destroy()
            root.destroy()
            MainPage.MAINCALL(Admin_id)
            

        if (len(Data) == 0 or Data == None ):

            temp = tk.Tk()
            temp.withdraw()
            messagebox.showinfo("Not Found !","No one Found !!")
            temp.destroy()
            
            MainPage.MAINCALL(Admin_id)
        
        else: 





            def populate(top):
                
                NUMBERLab = []
                IMAGE = []
                IDLab = []
                NAMELab = []
                DEPARTMENLab = []
                REMOVEBut = []
                IDData = []
                NAMEData = []
                DEPARMENTData = []

                for i,D in enumerate(Data):
        
        
        
                        self.NUMLab = tk.Label(top)
                        
                        self.NUMLab.configure(background="#d9d9d9")
                        self.NUMLab.configure(disabledforeground="#a3a3a3")
                        self.NUMLab.configure(font="-family {Product Sans} -size 24 -weight normal ")
                        self.NUMLab.configure(foreground="#000000")
                        self.NUMLab.configure(text=str(i+1)+".")
        
                        NUMBERLab.append(self.NUMLab)
        
                        
                        try:
                            print("In try")
                            first = os.listdir(r'C:\Users\GIGABYTE\Desktop\Project\Faces\\'+str(D[0]))[0]       
                            print("The Image",first)
                            photo = tk.PhotoImage(file="C:\\Users\\GIGABYTE\\Desktop\\Project\\Faces\\"+str(D[0])+"\\"+first)
                        
                        except Exception:
                                
                            photo = tk.PhotoImage(file=r"C:\Users\GIGABYTE\Desktop\Project\Faces\noimage.png")
                            
                        print("C:\\Users\\GIGABYTE\\Desktop\\Project\\Faces\\"+str(D[0])+"\\"+first)
        
                        self.IMG = tk.Label(top,image=photo)
                        self.IMG.image = photo
                        self.IMG.place(relx=0.35, rely=0.083, height=141, width=164)
                        self.IMG.configure(background="#d9d9d9")
                        self.IMG.configure(disabledforeground="#a3a3a3")
                        self.IMG.configure(foreground="#000000")
                        self.IMG.configure(text='''Label''')
        
                        IMAGE.append(self.IMG)
        
        
                        self.IdLab = tk.Label(top)
                        self.IdLab.place(relx=0.21, rely=0.229, height=41, width=54)
                        self.IdLab.configure(background="#d9d9d9")
                        self.IdLab.configure(disabledforeground="#a3a3a3")
                        self.IdLab.configure(font="-family {Product Sans} -size 12 -weight normal")
                        self.IdLab.configure(foreground="#000000")
                        self.IdLab.configure(text='''ID''')
        
                        IDLab.append(self.IdLab)
        
        
                        self.NAMLab = tk.Label(top)
                        self.NAMLab.place(relx=0.19, rely=0.28, height=41, width=54)
                        self.NAMLab.configure(activebackground="#f9f9f9")
                        self.NAMLab.configure(activeforeground="black")
                        self.NAMLab.configure(background="#d9d9d9")
                        self.NAMLab.configure(disabledforeground="#a3a3a3")
                        self.NAMLab.configure(font="-family {Product Sans} -size 12 -weight normal")
                        self.NAMLab.configure(foreground="#000000")
                        self.NAMLab.configure(highlightbackground="#d9d9d9")
                        self.NAMLab.configure(highlightcolor="black")
                        self.NAMLab.configure(text='''Name''')
        
                        NAMELab.append(self.NAMLab)
        
        
                        self.DEPLab = tk.Label(top)
                        self.DEPLab.place(relx=0.12, rely=0.328, height=41, width=94)
                        self.DEPLab.configure(activebackground="#f9f9f9")
                        self.DEPLab.configure(activeforeground="black")
                        self.DEPLab.configure(background="#d9d9d9")
                        self.DEPLab.configure(disabledforeground="#a3a3a3")
                        self.DEPLab.configure(font="-family {Product Sans} -size 12 -weight normal")
                        self.DEPLab.configure(foreground="#000000")
                        self.DEPLab.configure(highlightbackground="#d9d9d9")
                        self.DEPLab.configure(highlightcolor="black")
                        self.DEPLab.configure(text='''Department''')
        
                        DEPARTMENLab.append(self.DEPLab)
                        
                        I = D[0]
                        self.RMVBut = tk.Button(top,command=lambda I=I : release(I))
                     
                        self.RMVBut.place(relx=0.725, rely=0.253, height=54, width=97)
                        self.RMVBut.configure(activebackground="#ececec")
                        self.RMVBut.configure(activeforeground="#000000")
                        self.RMVBut.configure(background="#800040")
                        self.RMVBut.configure(disabledforeground="#a3a3a3")
                        self.RMVBut.configure(font="-family {Product Sans} -size 14 -weight bold")
                        self.RMVBut.configure(foreground="#ffffff")
                        self.RMVBut.configure(highlightbackground="#d9d9d9")
                        self.RMVBut.configure(highlightcolor="black")
                        self.RMVBut.configure(pady="0")
                        self.RMVBut.configure(text='''Release''')
        
                        REMOVEBut.append(self.RMVBut)
        
                        self.IdData = tk.Label(top)
                        self.IdData.place(relx=0.317, rely=0.242, height=21, width=224)
                        self.IdData.configure(background="#d9d9d9")
                        self.IdData.configure(disabledforeground="#a3a3a3")
                        self.IdData.configure(font="-family {Product Sans} -size 12 -weight bold")
                        self.IdData.configure(foreground="#000000")
                        self.IdData.configure(text=D[0])
        
                        IDData.append(self.IdData)
        
                        self.NMEData = tk.Label(top)
                        self.NMEData.place(relx=0.317, rely=0.292, height=21, width=224)
                        self.NMEData.configure(activebackground="#f9f9f9")
                        self.NMEData.configure(activeforeground="black")
                        self.NMEData.configure(background="#d9d9d9")
                        self.NMEData.configure(disabledforeground="#a3a3a3")
                        self.NMEData.configure(font="-family {Product Sans} -size 12 -weight bold")
                        self.NMEData.configure(foreground="#000000")
                        self.NMEData.configure(highlightbackground="#d9d9d9")
                        self.NMEData.configure(highlightcolor="black")
                        self.NMEData.configure(text=D[1])
        
                        NAMEData.append(self.NMEData)
        
                        self.DEPData = tk.Label(top)
                        self.DEPData.place(relx=0.317, rely=0.339, height=21, width=224)
                        self.DEPData.configure(activebackground="#f9f9f9")
                        self.DEPData.configure(activeforeground="black")
                        self.DEPData.configure(background="#d9d9d9")
                        self.DEPData.configure(disabledforeground="#a3a3a3")
                        self.DEPData.configure(font="-family {Product Sans} -size 12 -weight bold")
                        self.DEPData.configure(foreground="#000000")
                        self.DEPData.configure(highlightbackground="#d9d9d9")
                        self.DEPData.configure(highlightcolor="black")
                        self.DEPData.configure(text=D[4])
        
                        DEPARMENTData.append(self.DEPData)
        
                        self.TitleLab = tk.Label(top)
                        #self.TitleLab.place(relx=0.133, rely=0.01, height=71, width=344)
                        self.TitleLab.grid(row = 0 , column = 0)
                        self.TitleLab.configure(background="#d9d9d9")
                        self.TitleLab.configure(disabledforeground="#a3a3a3")
                        self.TitleLab.configure(font= "-family {Product Sans} -size 17 -weight normal ")
                        self.TitleLab.configure(foreground="#000000")
                        self.TitleLab.configure(text='''Select The''')
        
                        self.TitleLab2 = tk.Label(top)
                        #self.TitleLab2.place(relx=0.517, rely=0.021, height=51, width=54)
                        self.TitleLab2.grid(row = 0 , column = 1)
                        self.TitleLab2.configure(background="#d9d9d9")
                        self.TitleLab2.configure(disabledforeground="#a3a3a3")
                        self.TitleLab2.configure(font= "-family {Product Sans} -size 17 -weight normal ")
                        self.TitleLab2.configure(foreground="#800040")
                        self.TitleLab2.configure(text='''One''')

                rely=-0.400
                row = 0
                        
        
        
                print(zip (NUMBERLab,IMAGE,IDLab,NAMELab,DEPARTMENLab,REMOVEBut,IDData,NAMEData,DEPARMENTData))
                    
                for (numl, im, idl, nml, depl, rmb, idd, nmd, depd) in zip (NUMBERLab,IMAGE,IDLab,NAMELab,DEPARTMENLab,REMOVEBut,IDData,NAMEData,DEPARMENTData):
                    rely += 0.400
                    
                    
        #                    numl.place()
                    numl.grid(row=1+row, column=0, pady = 0 )# height=71, width=74)
                    im.grid(row=1+row, column=1 , columnspan = 3, rowspan =3, padx = 50, pady=60)#, height=141, width=164)
                    rmb.grid(row=1+row, column=3, columnspan = 3,rowspan = 3,padx = 155, pady = 50)# height=54, width=97)
                    
                    idl.grid(row=4+row, column=0 , columnspan= 2, sticky = "e")
                    nml.grid(row=5+row, column=0, columnspan = 2,sticky = "e")
                    depl.grid(row=6+row, column=0, columnspan = 2,sticky = "e")
                    
                    idd.grid(row=4+row, column=2, padx = 50,sticky = "w")# height=21, width=224)
                    nmd.grid(row=5+row, column=2,padx = 50,sticky = "w")# height=21, width=224)
                    depd.grid(row=6+row, column=2,padx = 50,sticky = "w")# height=21, width=224)
                    
                    clean = tk.Label(top, text = "-----------------------------------------------------------------------------------------", background="#d9d9d9")
                    
                    clean.grid(row = 7+row, column = 0, columnspan = 5, pady = 30)
                    
                    row += 8
                    #top.grid_rowconfigure(row, minsize=500)
        #        
                    print("After For Loop")

            def onFrameConfigure(canvas):
                
                canvas.configure(scrollregion=canvas.bbox("all"))

            def onmainpage():
            
                print("THE DESTROY ?")
                top.destroy()
                root.destroy()
                MainPage.MAINCALL(Admin_id)  


            root = tk.Tk()
            root.withdraw()                 
            
            
            top = tk.Toplevel(root)
            canvas = tk.Canvas(top, borderwidth=0, background="#d9d9d9") # Canvas
            frame = tk.Frame(canvas, background="#d9d9d9") # Frame
                             
            vsb = tk.Scrollbar(top, orient="vertical", command=canvas.yview)
            vsb.pack(side="right", fill="y")
            
            
            
            canvas.configure(yscrollcommand=vsb.set)
            canvas.pack(side="left", fill="both", expand=True)
            canvas.create_window((4,4), window=frame, anchor="nw")
            
            frame.bind("<Configure>", lambda event, canvas=canvas: onFrameConfigure(canvas))
            top.geometry("600x963")
            
    #        top.resizable(0,0 )
            top.title("Relese people fom here")
            top.configure(background="#d9d9d9")
            top.protocol("WM_DELETE_WINDOW", onmainpage)
            


            
     
            populate(frame)
            top.mainloop()

                
                    

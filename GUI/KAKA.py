import tkinter as tk


top = tk.Tk()
top.geometry('600x600')
frame = tk.Frame(top, background="#e88413")

frame.pack(expand = True, side = "bottom", fill = 'both')

btn = tk.Button(frame, text = "HEY Click here " )
btn.grid(row = 0 , column = 0)

label = tk.lab
btn1 = tk.Button(frame, text = "HEY" )
btn1.grid(row = 1 , column = 0)

top.mainloop()
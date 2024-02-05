import tkinter as tk
from PIL import ImageTk, Image
import os
from tkinter import *
#custom functions
def draw():
    #adds user lines to graph
    x1 = int(txtX1.get())
    y1 = int(txtY1.get())
    x2 = int(txtX2.get())
    y2 = int(txtY2.get())
    x1 = (x1*20)+10
    y1 = (y1*20)+10
    x2*=20
    y2*=20
    canvas.create_line(x1,y1,x2,y2)
def clear():
    #clears made lines
    canvas.delete("all")
    graph()
def graph():
    #makes graph x&y lines
    canvas.create_line(10, 0, 10,800,fill="grey")
    canvas.create_line(0,10,800,10,fill="grey")
    #points of interest
    canvas.create_text((300,600),text="Fish School")
    canvas.create_text((600,700),text="Coral Reef")
    canvas.create_text((700,400),text="Fish School")
    canvas.create_text((200,350),text="Sea Turtles")
    canvas.create_text((150,750),text="Coral Reef")
    canvas.create_text((50,15),text="Scuba Boat")
    #creates indenting lines and numbers for graph
    x = 0
    y = 20
    t = 0
    textLocation=40
    num = 2
    size = 800
    while t < 800:
        canvas.create_line(x,t,y,t,fill="grey")
        canvas.create_text((textLocation,30), text=str(num)+"m")
        canvas.create_text((30,textLocation), text=str(num)+"m")
        canvas.create_line(t,x,t,y,fill="grey")
        t += size/20
        textLocation +=40
        num += 2
#window properties
window =tk.Tk()
window.title("Graphing with Tkinter")
window.geometry("1024x910")
window.config(bg="light gray")
#create labels
lblX1 = tk.Label(window, text="X1:")
lblY1 = tk.Label(window, text="Y1:")
lblX2 = tk.Label(window, text="X2:")
lblY2 = tk.Label(window, text="Y2:")
#create text
txtX1 = tk.Entry(window)
txtY1 = tk.Entry(window)
txtX2 = tk.Entry(window)
txtY2 = tk.Entry(window)
#buttons
btn = tk.Button(window,text="Draw!",padx=20, command=draw)
btnClear = tk.Button(window,text="clear",padx=20,command=clear)
#create canvas
canvas = tk.Canvas(window,width=800,height=800)
canvas.config(bg="light blue")
#add to canvas
lblX1.grid(row=0,column=1)
lblY1.grid(row=1,column=1)
lblX2.grid(row=2,column=1)
lblY2.grid(row=3,column=1)
txtX1.grid(row=0,column=2)
txtY1.grid(row=1,column=2)
txtX2.grid(row=2,column=2)
txtY2.grid(row=3,column=2)
btn.grid(row=4, column=1)
btnClear.grid(row=4,column=2,padx=10)
canvas.grid(row=4,column=3)
#build window
window.after_idle(graph)
window.mainloop()

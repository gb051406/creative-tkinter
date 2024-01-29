import tkinter as tk


#custom functions
def draw():
    x1 = int(txtX1.get())
    y1 = int(txtY1.get())
    x2 = int(txtX2.get())
    y2 = int(txtY2.get())
    x1 +=400
    y1 +=400
    x2+=400
    y2+=400
    canvas.create_line(x1,y1,x2,y2)
def clear():
    canvas.delete("all")
    canvas.create_line(400, 0, 400,800)
    canvas.create_line(0,400,800,400)
    x = 390
    y = 410
    t = 0
    s = 800
    while t < 800:
        canvas.create_line(x,t,y,t)
        canvas.create_line(t,x,t,y)
        t += 800/20
def graph():
    canvas.create_line(400, 0, 400,800)
    canvas.create_line(0,400,800,400)
    x = 390
    y = 410
    t = 0
    size = 800
    while t < 800:
        canvas.create_line(x,t,y,t)
        canvas.create_line(t,x,t,y)
        t += size/20
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
#create GUI
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

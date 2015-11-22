from Tkinter import *
import os

global ch
ch = 0
def keypress(event): 
    global ch
    ch = event.char
    if (ch == "q"): 
        root.destroy()

def main(): 
    global ch
    if (ch == "a"): 
        print "Pressed:", ch
    else: 
        os.system("clear")
    root.after(100, main)

root = Tk()
frame = Frame(root, width = 0, height = 0)
frame.bind_all("<Key>", keypress)
frame.pack()

root.after(10, main)
root.mainloop()
print ch

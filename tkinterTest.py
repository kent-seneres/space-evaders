from Tkinter import *
import os
import time

ch = -1
returnedVals = {}
returnedVals['ch'] = -1

def keypress(event): 
	returnedVals['ch'] = event.char

def end(): 
	root.destroy()
	
def processInput(): 
	ch = returnedVals['ch']
	if (ch != -1): 
		if (ch == 'a'): 
			print "Moving left"
		elif (ch == 'd'):
			print "Moving right"
		else: 
			os.system("cls" if os.name == "nt" else "clear")
			root.unbind_all("<Key>")
			
		returnedVals['ch'] = -1
		
def countdown(timeout, startTime): 
	if (time.time() - startTime < timeout): 
		processInput()
		root.after(100, countdown, timeout, startTime)
	else: 
		print "Times up"
		time.sleep(1)
		end()
		
def main(timeout, startTime): 
	while (time.time() - startTime < timeout): 
		root.update()
		ch = returnedVals['ch']
		print ch
		print "Counting down ... "
		time.sleep(0.01)
		if (ch == 'q'): 
			"PRESSED Q"
			break
		
root = Tk()
root.withdraw()
#frame = Frame(root, width = 0, height = 0) 
#frame.bind_all("<Key>", lambda event, p1 = 1:keypress(event, p1))
#frame.bind_all("<Key>", keypress)
#frame.pack()

root.bind_all("<Key>", keypress)

speed = 2
#root.after(0, countdown, speed, time.time())
#root.after(0, main, 2, time.time())

root.mainloop()

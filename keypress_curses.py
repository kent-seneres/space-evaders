import curses

import os, random, time, getpass

window = curses.initscr()
window.nodelay(1)
curses.noecho()

startTime = time.time()
timeout = 1

while True:

    c = window.getch()
    if (c != -1): 
        ch = c
        window.addstr("Pressed: " + chr(ch) + "\n")
        window.refresh()
    if (time.time() - startTime) > timeout: 
    	break


curses.endwin()    
print ch

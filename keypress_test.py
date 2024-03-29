import os

class _Getch:
    """Gets a single character from standard input.  Does not echo to the
screen."""
    def __init__(self):
        try:
            self.impl = _GetchWindows()
        except ImportError:
            self.impl = _GetchUnix()

    def __call__(self): return self.impl()


class _GetchUnix:
    def __init__(self):
        import tty, sys

    def __call__(self):
    	import sys, select, termios, tty
		
		old_settings = termios.tcgetattr(sys.stdin)
		try:
				tty.setcbreak(sys.stdin.fileno())

				i = 0
				while 1:
				        print i
				        i += 1

				        if iselect.select([sys.stdin], [], [], 0) == ([sys.stdin], [], []):
				                c = sys.stdin.read(1)
				                if c == '\x1b':         # x1b is ESC
				                        break

		finally:
				termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)
		return c

class _GetchWindows:
    def __init__(self):
        import msvcrt

    def __call__(self):
        import msvcrt
        return msvcrt.getch()


getch = _Getch()

done = False
while not done:
	char = getch()
	print type(char)
	if char == 'c':
		os.system('cls' if os.name == 'nt' else 'clear')		
	elif char == 'd': 
		done = True

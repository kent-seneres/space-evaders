from Tkinter import *
import time, os, random, getpass

class Game:
    def __init__(self, root, rowsize, iconsize, numObs, left, right, blast, numBlast, clear):

        self.root = root
        self.root.bind_all("<Key>", self.keypress)

        self.DELAY = 25
        self.LOGO_SIZE = 11

        self.ROWSIZE = rowsize
        # SIZE must be the same as the number of lines in art text files
        self.SIZE = iconsize        
        self.NUM_OBSTACLES = numObs
        self.LEFT = left
        self.RIGHT = right
        self.BLAST = blast
        self.NUM_BLAST_START = numBlast
        self.CLEAR = clear
        self.move = -1
        self.numBlasts = self.NUM_BLAST_START
        self.crash = False
        self.sideCrash = False

        self.logo = []
        self.ship = []
        self.obstacleList = []
        self.blast = []
        self.explosion = []
        self.emptyBlock = [(self.SIZE * " ") for i in range(self.SIZE)]

        self.emptyRow = [self.emptyBlock for i in range(self.ROWSIZE)]
        self.shipRow = self.emptyRow[:]
        self.nextRow = self.emptyRow[:]
        self.newRow = self.emptyRow[:]
        
        self.loadFiles()

        self.shipRow[self.ROWSIZE / 2] = self.ship
        speed = 1
        self.gameStart = time.time()

        self.updateGame()

    def updateGame(self):
        
        # self.printNumBlasts()
        
        self.clearScreen()

        if (self.sideCrash == False):
            self.createShipRowWithObstacles()
            self.createNewRow()
        
        self.printScreen()

        if (self.crash == False and self.sideCrash == False):
            self.countdown(1, time.time())
        # else game over 
        
    def loadFiles(self):
        f = open("ship.txt", "r")
        self.ship = [f.readline().rstrip('\r\n') for i in range(self.SIZE)]
    
        obFileList = ["obstacle"+str(i+1)+".txt" for i in range(self.NUM_OBSTACLES)]
        for i in range(self.NUM_OBSTACLES):
            f = open(obFileList[i], "r")
            self.obstacleList.append([f.readline().rstrip("\r\n") for j in range(self.SIZE)])

        f = open("blast.txt", "r")
        self.blast = [f.readline().rstrip("\r\n") for i in range(self.SIZE)]

        f = open("explosion.txt", "r")
        self.explosion = [f.readline().rstrip("\r\n") for i in range(self.SIZE)]

        f = open("logo.txt", "r")
        self.logo= [f.readline() for i in range(self.LOGO_SIZE)]
        f.close()

    def printIntro(self):
        line = 15*' ' + 24*'-'

        print
        print line
        print line
        print 15*' ' + "||  " + self.LEFT + "  to move left   ||"
        print 15*' ' + "||  " + self.RIGHT + "  to move right  ||"
        print 15*' ' + "||  " + self.BLAST + "  to use blaster ||"
        print line
        print line
        print

    def startGame(self):
        self.printIntro()
        getpass.getpass("Press ENTER to play ")
                
        self.updateGame()
        
    def clearScreen(self):
        os.system(self.CLEAR)
            
    def keypress(self, event):
        self.move = event.char

    def processInput(self):
        if (self.move != -1):
            self.clearScreen()
            if (self.move == self.LEFT):
                self.shiftLeft()
            elif (self.move == self.RIGHT):
                self.shiftRight()
            elif (self.move == self.BLAST):
                if (self.numBlasts > 0):
                    self.blaster()
                    
            self.move = -1
            if (self.crash == False):
                self.printScreen()
                

    def countdown(self, timeout, startTime):
        if (time.time() - startTime < timeout and self.sideCrash == False):
            self.processInput()
            self.root.after(self.DELAY, self.countdown, timeout, startTime)
        else:
            self.updateGame()

    def printRow(self, row):
        for i in range(self.SIZE):
            for j in range(len(row)):
                print row[j][i],
            print

    def printScreen(self):
        self.printRow(self.shipRow)
        self.printRow(self.nextRow)
        self.printRow(self.newRow)

    def shiftLeft(self):
        shipLoc = self.shipRow.index(self.ship)
        if (self.shipRow[shipLoc - 1] != self.emptyBlock):
            self.sideCrash = True
            self.shipRow[shipLoc - 1] = self.explosion
        else:
            self.shipRow[shipLoc - 1] = self.ship

        self.shipRow[shipLoc] = self.emptyBlock

    def shiftRight(self):
        shipLoc = self.shipRow.index(self.ship)
        
        if (shipLoc == self.ROWSIZE - 1):
            shipLoc = -1

        if (self.shipRow[shipLoc + 1] != self.emptyBlock):
            self.sideCrash = True
            self.shipRow[shipLoc + 1] = self.explosion
        else:
            self.shipRow[shipLoc + 1] = self.ship

        self.shipRow[shipLoc] = self.emptyBlock

    def createShipRowWithObstacles(self):
        for i in range(self.ROWSIZE):
            if (self.nextRow[i] in self.obstacleList):
                if (self.shipRow[i] == self.ship):
                    self.crash = True
                    self.shipRow[i] = self.explosion
                else:
                    self.shipRow[i] = self.nextRow[i]
            elif (self.shipRow[i] != self.ship):
                self.shipRow[i] = self.emptyBlock

    def createNewRow(self):
        # control percentage of number of obstacles
        numObstacles = [0, 1, 1, 1, 1, 2, 2, 2, 2, 3]

        # move the obstacles up
        for i in range(self.ROWSIZE):
            self.nextRow[i] = self.newRow[i]

        # create new incoming obstacles
        self.newRow = self.emptyRow[:]
        for i in range(random.choice(numObstacles)):
            self.newRow[random.randrange(self.ROWSIZE)] = random.choice(self.obstacleList)

    def blaster(self):
        i = self.shipRow.index(self.ship)
        if (self.nextRow[i] in self.obstacleList):
            self.nextRow[i] = self.explosion
        else:
            self.nextRow[i] = self.blast

        if (self.newRow[i] in self.obstacleList):
            self.newRow[i] = self.explosion
        else:
            self.newRow[i] = self.blast

        self.numBlasts -= 1
    
root = Tk()
clear = "cls" if os.name == "nt" else "clear"

root.withdraw()
root.focus_force()
app = Game(root, 5, 10, 4, 'a', 'd', 's', 5, clear)
root.mainloop()


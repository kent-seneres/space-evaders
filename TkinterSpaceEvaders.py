"""

COS 125 Fall 2014   10/24/14
Kent Seneres

    PROJECT 1
"Space Evaders"

This game runs on python command line. Instead of
running the python module on IDLE, just double click
the file to start the game.
Unfortunately, because the game uses methods from modules
specific to Windows operating system, the game will not
run on other operating systems. Maybe the next version
will have cross platform support.


As the opening screen says, the default window size
should be Width = 55 and Height = 35 for the game to
look nice. However, it may vary with each computer.
The game will still run as intended if the screen size
is not optimal, but it won't look as pleasant.

To move left, press 'a'
To move right, press 'd'
To use the blaster, which blasts away the obstacle in
front of the space ship to avoid a crash, press 's'

The ship can move through one end of the screen to the
other. The speed at which the obstacles come increases
throughout the game. The game ends when the ship crashes
into an asteroid.

The three highest scores are printed at the end of the
game, and the user is prompted to hit enter to play again.
"""

import msvcrt, os, random, time, getpass

from Tkinter import *

#initializing string "objects"
b = ' '
e = 10*b
u = '_'
fs = '/'
bs = '\\'
v = '|'
o = '('
c = ')'

shipLine1 = 2*b + u + 4*b + u + 2*b
shipLine2 = u + v + b + v + 2*u + v + b+ v + u
shipLine3 = bs + 8*b + fs
shipLine4 = u + bs + 6*b + fs + u
shipLine5 = bs + 3*b + 2*u + 3*b + fs
shipLine6 = b + 2*bs + fs + 2*b + bs + 2*fs + b
shipLine7 = 2*b + 2*bs + 2*b + 2*fs + 2*b
shipLine8 = 3*b + 2*bs + 2*fs + 3*b
shipLine9 = 4*b + bs + fs + 4*b
shipLine10 = e

blastLine1 = 4*b + 2*v + 4*b
blastLine2 = 4*b + 2*v + 4*b
blastLine3 = 4*b + 2*v + 4*b
blastLine4 = 4*b + 2*v + 4*b
blastLine5 = 4*b + 2*v + 4*b
blastLine6 = 4*b + 2*v + 4*b
blastLine7 = 4*b + 2*v + 4*b
blastLine8 = 4*b + 2*v + 4*b
blastLine9 = 4*b + 2*v + 4*b
blastLine10 = 4*b + 2*v + 4*b

explosionLine1 = e
explosionLine2 = e
explosionLine3 = e
explosionLine4 = 2*b + o + bs + 2*b + fs + c + 2*b
explosionLine5 = b + o + bs + 2*b + 2*fs + c + 2*b
explosionLine6 = 2*b + 2*o + 2*u + c + 3*b
explosionLine7 = e
explosionLine8 = e
explosionLine9 = e
explosionLine10 = e

obstacle1Line1 = e
obstacle1Line2 = e
obstacle1Line3 = e
obstacle1Line4 = 4*b + 2*u + 4*b
obstacle1Line5 = 3*b + fs + 2*b + bs + 3*b
obstacle1Line6 = 2*b + v + 4*b + v + 2*b
obstacle1Line7 = 3*b + bs + 2*u + fs + 3*b
obstacle1Line8 = e
obstacle1Line9 = e
obstacle1Line10 = e

obstacle2Line1 = e
obstacle2Line2 = e
obstacle2Line3 = 2*b + 6*u + 2*b
obstacle2Line4 = b + fs + 6*b + bs + b
obstacle2Line5 = b + v + 6*b + v + b
obstacle2Line6 = 2*b + bs + 4*b + fs + 2*b
obstacle2Line7 = 3*b + bs + 2*u + fs + 3*b
obstacle2Line8 = e
obstacle2Line9 = e
obstacle2Line10 = e

obstacle3Line1 = e
obstacle3Line2 = e
obstacle3Line3 = 4*b + 2*u + 4*b
obstacle3Line4 = 3*b + fs + 2*b + bs + 3*b
obstacle3Line5 = 2*b + bs + 3*b + v + 3*b
obstacle3Line6 = 2*b + v + 3*b + v + 3*b
obstacle3Line7 = 3*b + bs + b + fs + 4*b
obstacle3Line8 = 4*b + bs + v + 4*b
obstacle3Line9 = e
obstacle3Line10 = e

obstacle4Line1 = 6*b + u + 3*b
obstacle4Line2 = 2*b + 3*u + fs + b + bs + 2*b
obstacle4Line3 = b + fs + 6*b + bs + b
obstacle4Line4 = fs + 7*b + v + b
obstacle4Line5 = v + 7*b + v + b
obstacle4Line6 = bs + 7*b + fs + b
obstacle4Line7 = b + v + 5*b + fs + 2*b
obstacle4Line8 = b + v + 3*b + u + fs + 3*b
obstacle4Line9 = b + bs + 2*u + fs + 5*b
obstacle4Line10 = e

ship = [shipLine1, shipLine2, shipLine3, shipLine4, shipLine5, shipLine6,
    shipLine7, shipLine8, shipLine9, shipLine10]

blast = [blastLine1, blastLine2, blastLine3, blastLine4, blastLine5,
         blastLine6, blastLine7, blastLine8, blastLine9, blastLine10]

explosion = [explosionLine1, explosionLine2, explosionLine3, explosionLine4,
             explosionLine5, explosionLine6, explosionLine7, explosionLine8,
             explosionLine9, explosionLine10]

obstacle1 = [obstacle1Line1, obstacle1Line2, obstacle1Line3, obstacle1Line4,
             obstacle1Line5, obstacle1Line6, obstacle1Line7, obstacle1Line8,
             obstacle1Line9, obstacle1Line10]

obstacle2 = [obstacle2Line1, obstacle2Line2, obstacle2Line3, obstacle2Line4,
             obstacle2Line5, obstacle2Line6, obstacle2Line7, obstacle2Line8,
             obstacle2Line9, obstacle2Line10]

obstacle3 = [obstacle3Line1, obstacle3Line2, obstacle3Line3, obstacle3Line4,
             obstacle3Line5, obstacle3Line6, obstacle3Line7, obstacle3Line8,
             obstacle3Line9, obstacle3Line10]

obstacle4 = [obstacle4Line1, obstacle4Line2, obstacle4Line3, obstacle4Line4,
             obstacle4Line5, obstacle4Line6, obstacle4Line7, obstacle4Line8,
             obstacle4Line9, obstacle4Line10]

obstacleList = [obstacle1, obstacle2, obstacle3, obstacle4]
emptyBlock = [e, e, e, e, e, e, e, e, e, e]

crash = False
numBlasts = 5
move = -1

def printLogo():    
    print """
              **** ****    *    **** *****
             *     *   *  * *  *     *    
              ***  ****  *   * *     *****
                 * *     ***** *     *    
             ****  *     *   *  **** *****

        ***** *   *   *   ****  ***** ****   ****
        *     *   *  * *  *   * *     *   * *    
        ***** *   * *   * *   * ***** ****   *** 
        *      * *  ***** *   * *     *  *      *
        *****   *   *   * ****  ***** *   * **** 
    """
    
def printIntro():
    
    print
    print 15*' ' + 24*'-'
    print 15*' ' + 24*'-'
    print 15*' ' + "||  4  to move left   ||"
    print 15*' ' + "||  6  to move right  ||"
    print 15*' ' + "||  5  to use blaster ||"
    print 15*' ' + 24*'-'
    print 15*' ' + 24*'-'
    print

def promptCallibration():
    
    print 10*' ' + "If screen is callibrated, hit ENTER "
    print 5*' ' + 45*'_'
    getpass.getpass( """
                To callibrate screen:
            
            - Right click on TOP of window
            - Click "Defaults"
            - Go to "Layout"
            - Find "Window Size"
            - Enter "55" for WIDTH
            - Enter "35" for HEIGHT
            - RESTART GAME
                         """)
        
def sortScores(scores):   
    sortedList = []
    for i in range(len(scores)):
        score = ''
        for j in range(len(scores[i])):
            if scores[i][j] == '\n':
                j = 10
            else:
                score += scores[i][j]
        if scores[i] != '':
            #need to turn list elements into Integers
            #to sort numerically
            sortedList.append(int(score))
    
    sortedList.sort()
    sortedList.reverse()

    #reconstruct a list of strings with newline character
    for i in range(len(sortedList)):
        sortedList[i] = str(sortedList[i])+'\n'
        
    return sortedList

def addScore(score):       
    inFile = file('scores.txt', 'r')
    scores = []
    newScore = score + '\n'
    #keeps track of the top 5 scores
    for i in range(5):
        line = inFile.readline()
        scores.append(line)
    inFile.close()

    inFile = file('scores.txt', 'w')
    scores.append(newScore)    
    scores = sortScores(scores)
    
    if newScore == scores[0]:
        print 18*' ' + "NEW HIGH SCORE" + '\n'
        
    for i in range(len(scores)):
        if i < 3:
            #displays only the top 3 scores
            print 20*' ' + str(i+1) + ': ' + scores[i],            
        inFile.write(scores[i])
        
    inFile.close()

def findShip(state):
    #returns index of ship from the list state
    for i in range(len(state)):
        if state[i] == ship:
            return i

def printState(state):
    for i in range(10):
        for j in range(len(state)):
            print state[j][i],
        print
    
def stateWithObstacles(state, obstacles):
    global crash
    
    newState = state
    shipLoc = findShip(state)
    
    for i in range(len(state)):
        if obstacles[i] in obstacleList:
            if state[i] == ship:
                crash = True
            else:
                newState[i] = obstacles[i]
        else:
            newState[i] = emptyBlock
            
    if crash:
        newState[shipLoc] = explosion
    else:
        newState[shipLoc] = ship
        
    return newState

def printNumBlasts():
    x = ''
    for i in range(numBlasts):
        x += "|"
    print "Blasts remaining: " + str(x)
    print
    
def blaster(state, obstacles1, obstacles2):
    newOb1 = obstacles1
    newOb2 = obstacles2
    shipLoc = findShip(state)

    if obstacles1[shipLoc] in obstacleList:
        newOb1[shipLoc] = explosion
    else:
        newOb1[shipLoc] = blast

    if obstacles2[shipLoc] in obstacleList:
        newOb2[shipLoc] = explosion
    else:
        newOb2[shipLoc] = blast
     
    return newOb1, newOb2
  
def shiftLeft(state):
    global crash
    newState = state
    shipLoc = findShip(state)

    if state[shipLoc-1] != emptyBlock:
        crash = True
        newState[shipLoc] = emptyBlock
        newState[shipLoc-1] = explosion
    else:
        newState[shipLoc-1] = ship    
        newState[shipLoc] = emptyBlock
        
    return newState                   

def shiftRight(state):
    global crash
    newState = state
    shipLoc = findShip(state)

    #wraps around screen
    if shipLoc == len(state)-1:
        shipLoc = -1
        
    if state[shipLoc+1] != emptyBlock:
        crash = True
        newState[shipLoc] = emptyBlock
        newState[shipLoc+1] = explosion
    else:
        newState[shipLoc+1] = ship
        newState[shipLoc] = emptyBlock

    return newState

def createObstacle(obstacleList, previousObstacles):
    numObstacles = [0,1,1,1,1,1,1,1,2,2,2,2,3,3]
    obstacles = [emptyBlock, emptyBlock, emptyBlock, emptyBlock, emptyBlock]
    
    for i in range(random.choice(numObstacles)):
        obstacles[random.randrange(5)] = random.choice(obstacleList)
        
    return obstacles
    
##    
##def processInput(timeout, state, obstacles1, obstacles2):
##    global numBlasts, crash
##    shipLoc = findShip(state)
##    startTime = time.time()
##    move = ' '
##
##    while True:
##        if msvcrt.kbhit():
##            move = msvcrt.getch()            
##            os.system('cls')
##            
##            if move == 'a' or move == '4':
##                state = shiftLeft(state)
##            elif move == 'd' or move == '6':
##                state = shiftRight(state)
##            elif move == 's' or move == '5':
##                if numBlasts < 1:
##                    if obstacles1[shipLoc] == ship:
##                        crash = True
##                        state[shipLoc] = explosion
##                else:
##                    obstacles1, obstacles2 = blaster(state, obstacles1, obstacles2)
##                    numBlasts -= 1
##  
##            if crash == False:
##                printNumBlasts()
##                printState(state)
##                printState(obstacles1)
##                printState(obstacles2)
##            else:
##                break
##            
##        if (time.time() - startTime) > timeout:
##            break
##
##
##    return state

def keypress(event):
    global move
    move = event.char

def processInput(state, obstacles1, obstacles2):
    global numBlasts, crash, move
    shipLoc = findShip(state)
    if (move != -1):
        if move == 'a' or move == '4':
            state = shiftLeft(state)
        elif move == 'd' or move == '6':
            state = shiftRight(state)
        elif move == 's' or move == '5':
            if numBlasts < 1:
                if obstacles1[shipLoc] == ship:
                    crash = True
                    state[shipLoc] = explosion
            else:
                obstacles1, obstacles2 = blaster(state, obstacles1, obstacles2)
                numBlasts -= 1

        if crash == False:
            printNumBlasts()
            printState(state)
            printState(obstacles1)
            printState(obstacles2)
        else:
            break
        move = -1

def countdown(timeout, startTime):
    if (time.time() - startTime < timeout):
        state = processInput()
        root.after(100, countdown, timeout, startTime)
    else:
        # done
    
def playGame():
    global crash, numBlasts
    crash = False
    numBlasts = 5
    state = [emptyBlock, emptyBlock, ship, emptyBlock, emptyBlock]
    emptyObstacles = [emptyBlock, emptyBlock, emptyBlock,
                      emptyBlock, emptyBlock]
    
    startTime = time.time()
    totalTime = 0
    count = 15
    
    obstacles1 = emptyObstacles
    obstacles2 = emptyObstacles

    while crash == False:
        printNumBlasts()
        
        if totalTime > 60:
            speed = 0.1
        elif totalTime > 50:
            speed = 0.20
        elif totalTime > 40:
            speed = 0.30
        elif totalTime > 30:
            speed = 0.40
        elif totalTime > 20:
            speed = 0.50
        elif totalTime > 10:
            speed = 0.60
        else:
            speed = 0.80

        if count == 15:
            obstacles1 = emptyObstacles
            obstacles2 = createObstacle(obstacleList, emptyObstacles)
        else:
            obstacles1 = obstacles2
            obstacles2 = createObstacle(obstacleList, obstacles1)
            if count%15 == 0:
                numBlasts += 1
            
        printState(state)
        printState(obstacles1)
        printState(obstacles2)

        state = processInput(speed, state, obstacles1, obstacles2)
        
        if crash == False:
            state = stateWithObstacles(state, obstacles1)
             
        count += 1
        os.system('cls')
        totalTime = time.time() - startTime
    
    printState(state)
    printState(obstacles2)
    score = str(int(totalTime) * int(1/speed) * 25)

    print 20*' ' + "YOU CRASHED" + '\n'
    print 20*' ' + "SCORE: " + score + '\n'
    addScore(score)
    print


printLogo()
printIntro()
promptCallibration()
os.system('cls')

while True:
    playGame()
    #getpass prevents terminal from closing and hide keypresses
    getpass.getpass(13*' ' + "Press enter to play again.")
    os.system('cls')


#!usr/bin/python

import math

#tic-tac-toe
#[1,2,3]
#[4,5,6]
#[7,8,9]

#[1,2,3,4]
#[5,6,7,8]
#[9,10,11,12]
#[13,14,15,16]

#setup
boardSize     = 3
total         = boardSize**2
positions     = range(1,(total)+1)
startCount    = 0
usedPositions = []

#functions
def printBoard(positions):
    blankRow = ' - | - | -'
    row      = ' '
    for index, val in enumerate(positions):
        row += str(val) + ' | '
        if (index+1)%boardSize == 0:
            print row
            if (index+1) != total:
                print blankRow
            row = ' '

def checkRow(user, position):
    lastInRow = boardSize
    while lastInRow <= total:
        if position <= lastInRow:
            break
        lastInRow *= 3

    return all([ positions[index] == user for index in range(lastInRow-boardSize, lastInRow)])

def checkColumn(user, position):
    lastInColumn = position
    while lastInColumn <= total-boardSize:
        if total-boardSize < lastInColumn <= total:
            break
        lastInColumn += boardSize

    return all([ positions[index] == user for index in range(lastInColumn-(boardSize*(boardSize-1))-1,lastInColumn,boardSize)])

def checkLeftDiagnals(user, position):
    return all([ positions[index] == user for index in range(0,total,boardSize+1)])

def checkRightDiagnal(user, position):
    return all([ positions[index] == user for index in range(boardSize-1,(total-(boardSize-1)),boardSize-1)])

def checkWinner(user, position):
    result = False
    if len(usedPositions) >= (boardSize*2)-1:
        #check position corner
        if position == 1 or position == boardSize or position == total or position == (total-(boardSize-1)):
            #check diagnal
            if position == 1 or position == total:
                result = checkLeftDiagnals(user, position)
            else:
                result = checkRightDiagnal(user, position)
        #check position middle
        elif position%2 != 0 and math.ceil(total/2):
            #check diagnals
            result = checkLeftDiagnals(user, position)
            if not result:
                result = checkRightDiagnal(user, position)

        #all check rows and columns
        if not result:
            result = checkRow(user, position)
        if not result:
           result = checkColumn(user, position)

    return result

# two person function
def selectPosition(user):
    position = int(raw_input(user + '\'s please choose a number: '))
    while position in usedPositions:
        print str(position) + ' is already being used'
        position = int(raw_input(user + '\'s please choose a different number: '))
    usedPositions.append(position)
    positions[int(position) - 1] = user
    printBoard(positions)
    return checkWinner(user,position)
# end of functions


### set up game ###

# user can choose 1 player or 2 player
# 1 player user will play against the computer
# 2 player user will play against another user
print '1. one player'
print '2. two player'

game = 0
while game not in ['1','2']:
    game = raw_input('Please select an option (1 or 2): ')
game = int(game)

if game == 1:

    # user can choose easy or hard
    # easy will just choose a random number that is not being used
    # hard will go throud minmax algorithm to choose best location
    '''
    print '1. easy'
    print '2. hard'

    level = 0
    while level not in ['1','2']:
        level = raw_input('Please select an option (1 or 2): ')
    level = int(level)

    # let user choose X's or 0's
    # X's will go first
    user = ''
    while user not in ['X','O']:
        user = raw_input('X\'s will go first. X\'s or O\'s (X or O): ').upper()

    if level == 1:

    else:
    '''
    print 'Coming Soon!'
else:
    #two player
    printBoard(positions)
    while startCount < total:
        startCount += 1
        if startCount%2 == 0:
            user = 'O'
        else:
            user = 'X'
        if selectPosition(user):
            print 'GAME OVER ' + user + '\'s WIN!!!'
            break

# include "gameBoard.py"
#from gameBoard import *
from properties import *

import pygame
import sys

grid = [[0]*8 for y in range(8)]


def updateBackgroundGrid(player, col, row):
    if (player == 'p1'):
        grid[row][col] = 1
    elif (player == 'p2'):
        grid[row][col] = 2
    else:
        grid[row][col] = -1


def placeTile(col, row, color):
    midX = (col+1)*(TILESIZE) - (TILESIZE/2)
    midY = (row+1)*(TILESIZE) - (TILESIZE/2)
    pygame.draw.circle(screen, color, (int(midX), int(midY)), 20)
    pygame.display.update()


def checkRight(startX, startY, player):
    count = 0
    endVals = []
    wSquare = WIDTH / TILESIZE - 1

    while (startX <= wSquare):
        if (grid[startY][startX] == 0 or grid[startY][startX] == -1) or (startX == wSquare and grid[startY][startX] != player):
            print("Right if")
            count = 0
            break
        elif grid[startY][startX] == player or grid[startY][startX] == -1:
            print("Right elif")
            break
        else:
            print("Right else")
            count += 1
            startX += 1

    if count >= 1:

        endVals.append(startX)
        endVals.append(startY)
        # return empList
    else:
        endVals.append(-1)
        endVals.append(-1)
    # print("RIGHT")
    return endVals


def checkLeft(startX, startY, player):

    count = 0
    endVals = []

    while (0 <= startX):
        if (grid[startY][startX] == 0 or grid[startY][startX] == -1) or (startX == 0 and grid[startY][startX] != player):
            print("Left IF")
            count = 0
            break
        elif grid[startY][startX] == player or grid[startY][startX] == -1:
            print("Left ELIF")
            break
        else:
            print("ELSE")
            count += 1
            startX -= 1

    if count >= 1:
        endVals.append(startX)
        endVals.append(startY)
        # return empList
    else:
        endVals.append(-1)
        endVals.append(-1)
    return endVals


def checkUpDown(startX, startY, player, dir):
    count = 0
    endVals = []
    hSquare = HEIGHT / TILESIZE - 1
    step = 0
    if (dir == 'UP'):
        step = -1
    else:
        step = 1

    while (startY <= hSquare):
        if (grid[startY][startX] == 0 or grid[startY][startX] == -1) or (startY == hSquare and grid[startY][startX] != player):
            count = 0
            break
        elif grid[startY][startX] == player or grid[startY][startX] == -1:
            break

        else:
            count += 1
            startY += step

    if count >= 1:
        endVals.append(startX)
        endVals.append(startY)
        # return empList
    else:
        endVals.append(-1)
        endVals.append(-1)

    return endVals


def checkDown(startX, startY, player):
    count = 0
    endVals = []
    hSquare = HEIGHT / TILESIZE - 1

    while (startY <= hSquare):
        if (grid[startY][startX] == 0 or grid[startY][startX] == -1) or (startY == hSquare and grid[startY][startX] != player):
            count = 0
            break
        elif grid[startY][startX] == player or grid[startY][startX] == -1:
            break

        else:
            count += 1
            startY += 1

    if count >= 1:
        endVals.append(startX)
        endVals.append(startY)
        # return empList
    else:
        endVals.append(-1)
        endVals.append(-1)

    return endVals


def checkUp(startX, startY, player):
    count = 0
    endVals = []
    hSquare = HEIGHT / TILESIZE - 1

    while (0 <= startY):
        if (grid[startY][startX] == 0 or grid[startY][startX] == -1) or (startY == hSquare and grid[startY][startX] != player):
            #print("if ")
            count = 0
            break
        elif grid[startY][startX] == player or grid[startY][startX] == -1:
            break
        else:
           # print("else")
            count += 1
            startY -= 1

    if count >= 1:

        endVals.append(startX)
        endVals.append(startY)
        # return empList
    else:
        endVals.append(-1)
        endVals.append(-1)
    return endVals


def checkDiag(startX, startY, player):
    d = [[-1, -1], [1, 1], [1, -1], [-1, 1]]

    endVals = []
    hSquare = HEIGHT / TILESIZE - 1
    count = 0

    done = False
    tempX = startX
    tempY = startY

    for di in d:
        startX += di[1]
        startY += di[0]
        print("L/R: " + str(di[1]) + "  U/D: " + str(di[0]))
        while not done:
            if (startY <= hSquare and startX <= hSquare) and ((grid[startY][startX] == 0 or grid[startY][startX] == -1) or ((startY == hSquare or startX == hSquare) and grid[startY][startX] != player)):
                print("IF Diag")
                count = 0
                done = True
            elif startY < 0 or startX < 0 or startY > hSquare or startX > hSquare or grid[startY][startX] == player or grid[startY][startX] == -1:
                print("ELIF Diag")
                done = True
            else:
                print("Else Diag")
                count += 1
                startY += di[0]
                startX += di[1]

        if count >= 1:
            endVals.append(startX)
            endVals.append(startY)
            count = 0

            # return empList
        else:
            endVals.append(-1)
            endVals.append(-1)

        done = False
        startX = tempX
        startY = tempY

    return endVals

import pygame
from properties import *
from model import *
# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)


# game settings
WIDTH = 512  # 16 * 64 or 32 * 32 or 64 * 16
HEIGHT = 512  # 16 * 48 or 32 * 24 or 64 * 12
FPS = 60


#BGCOLOR = DARKGREY
TILESIZE = 64
size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)


def getWidth():
    return WIDTH


def getHeight():
    return HEIGHT


def initializeBoard():
    placeTile(3, 3, RED)
    updateBackgroundGrid('p2', 3, 3)
    placeTile(3, 4, WHITE)
    updateBackgroundGrid('p1', 3, 4)
    placeTile(4, 3, WHITE)
    updateBackgroundGrid('p1', 4, 3)
    placeTile(4, 4, RED)
    updateBackgroundGrid('p2', 4, 4)


def drawCircle(col, row):
    updateBackgroundGrid('p', col, row)
    midX = (col+1)*(TILESIZE) - (TILESIZE/2)
    midY = (row + 1) * (TILESIZE) - (TILESIZE / 2)
    pygame.draw.circle(screen,  GREEN, (int(midX), int(midY)), 19, 1)
    pygame.display.update()


def clearGrid():
    for row_index, row in enumerate(grid):
        for col_index, item in enumerate(row):
            if (grid[row_index][col_index] == -1):
                grid[row_index][col_index] = 0
                midX = (col_index+1)*(TILESIZE) - (TILESIZE/2)
                midY = (row_index+1)*(TILESIZE) - (TILESIZE/2)
                pygame.draw.circle(screen, BLACK, (int(midX), int(midY)), 22)
                pygame.display.update()


def placeTile(col, row, color):
    midX = (col+1)*(TILESIZE) - (TILESIZE/2)
    midY = (row+1)*(TILESIZE) - (TILESIZE/2)
    pygame.draw.circle(screen, color, (int(midX), int(midY)), 20)
    pygame.display.update()


def transformTiles(player, recentTileX, recentTileY):

    arg = ''
    if player == 1:
        arg = 'p1'
        color = WHITE
    else:
        arg = 'p2'
        color = RED

    tempX = recentTileX
    tempY = recentTileY

    print("------------------------------------------------")
    # Combine to create left right as well
    right = checkRight(recentTileX + 1, recentTileY, player)
    left = checkLeft(recentTileX - 1, recentTileY, player)

    up = checkUp(recentTileX, recentTileY - 1, player)
    down = checkDown(recentTileX, recentTileY + 1, player)

    #up = checkUpDown(recentTileX, recentTileY - 1, player, 'UP')
    #down = checkUpDown(recentTileX, recentTileY + 1, player, 'DOWN')

    diag = checkDiag(recentTileX, recentTileY, player)
    print("------------------------------------------------")

    if (right[0] != -1 and right[1] != -1):
        while (tempX < right[0]):
            updateBackgroundGrid(arg, tempX, tempY)
            placeTile(tempX, tempY, color)
            tempX += 1

    tempX = recentTileX
    tempY = recentTileY

    if (left[0] != -1 and left[1] != -1):
        while (tempX > left[0]):
            updateBackgroundGrid(arg, tempX, tempY)
            placeTile(tempX, tempY, color)
            tempX -= 1

    tempX = recentTileX
    tempY = recentTileY
    if (up[0] != -1 and up[1] != -1):
        while (tempY > up[1]):
            updateBackgroundGrid(arg, tempX, tempY)
            placeTile(tempX, tempY, color)
            tempY -= 1
    tempX = recentTileX
    tempY = recentTileY
    if (down[0] != -1 and down[1] != -1):
        while (tempY < down[1]):
            updateBackgroundGrid(arg, tempX, tempY)
            placeTile(tempX, tempY, color)
            tempY += 1
    tempX = recentTileX
    tempY = recentTileY
    if (diag[0] != -1 and diag[1] != -1):
        while (tempY > diag[1] and tempX > diag[0]):
            updateBackgroundGrid(arg, tempX, tempY)
            placeTile(tempX, tempY, color)
            tempY -= 1
            tempX -= 1
    tempX = recentTileX
    tempY = recentTileY
    if (diag[2] != -1 and diag[3] != -1):
        while (tempY < diag[3] and tempX < diag[2]):
            updateBackgroundGrid(arg, tempX, tempY)
            placeTile(tempX, tempY, color)
            tempY += 1
            tempX += 1
    tempX = recentTileX
    tempY = recentTileY
    if (diag[4] != -1 and diag[5] != -1):
        while (tempY < diag[5] and tempX > diag[4]):
            updateBackgroundGrid(arg, tempX, tempY)
            placeTile(tempX, tempY, color)
            tempY += 1
            tempX -= 1
    tempX = recentTileX
    tempY = recentTileY
    if (diag[6] != -1 and diag[7] != -1):
        while (tempY > diag[7] and tempX < diag[6]):
            updateBackgroundGrid(arg, tempX, tempY)
            placeTile(tempX, tempY, color)
            tempY -= 1
            tempX += 1


def showValidMoves(currPlayer):
    # 1) Get the current turn
    # 2) Go through the matrix to show the valid moves by checking in all directions for each value
    # 3) ex. if white turn, then check all sides with each white placed on board, to show possible

    print("VALID MOVES " + str(currPlayer))

    for row_index, row in enumerate(grid):
        for col_index, item in enumerate(row):
            startX = col_index
            startY = row_index
            if(grid[startY][startX] == 0):
                grid[startY][startX] = currPlayer

                print("-------- IN col " + str(startX) + " Row:  " +
                      str(startY) + "-------------------")

                up = checkUp(startX, startY - 1, currPlayer)

                down = checkDown(startX, startY + 1, currPlayer)

                left = checkLeft(startX - 1, startY, currPlayer)

                right = checkRight(startX + 1, startY, currPlayer)

                diag = checkDiag(startX, startY, currPlayer)

                grid[startY][startX] = -1

                if up[0] != -1 and up[1] != -1:
                    print("Up")
                    drawCircle(startX, startY)

                if down[0] != -1 and down[1] != -1:
                    print("down")
                    drawCircle(startX, startY)

                if left[0] != -1 and left[1] != -1:
                    print("LEft")
                    drawCircle(startX, startY)

                if right[0] != -1 and right[1] != -1:
                    print("RIGht")
                    drawCircle(startX, startY)

                if diag[0] != -1 and diag[1] != -1:
                    print("Diag 0")
                    drawCircle(startX, startY)

                if diag[2] != -1 and diag[3] != -1:
                    print("Diag 2")
                    drawCircle(startX, startY)

                if diag[4] != -1 and diag[5] != -1:
                    print("Diag 4")
                    drawCircle(startX, startY)

                if diag[6] != -1 and diag[7] != -1:
                    print("Diag 6")
                    drawCircle(startX, startY)

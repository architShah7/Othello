import pygame
from model import *
#import model
from gameBoard import *
from properties import *
#import gameBoard


def main():
    turn = 'p1'
    FPS = 60
   # BGCOLOR = DARKGREY
    #WIDTH = getWidth()
    #HEIGHT = getHeight()

    GRIDWIDTH = WIDTH / TILESIZE
    GRIDHEIGHT = HEIGHT / TILESIZE

    pygame.init()

    # Set the width and height of the screen [width, height]

    pygame.display.set_caption("Othello")

    # Loop until the user clicks the close button.
    done = False

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    screen.fill(BLACK)

    for x in range(0, WIDTH, TILESIZE):
        pygame.draw.line(screen, YELLOW, (x, 0), (x, HEIGHT))
        # pygame.display.update()

    for y in range(0, HEIGHT, TILESIZE):
        pygame.draw.line(screen, YELLOW, (0, y), (WIDTH, y))

    pygame.display.update()

    clock.tick(60)
    p1Done = False
    p2Done = True

    initializeBoard()

    while not done:

        showValidMoves(1)

        while not p1Done and not done:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    x = pos[0]
                    y = pos[1]

                    # translate pix to board coordinate
                    col = int(x/TILESIZE)
                    row = int(y/TILESIZE)
                    # print("X: " + str(col) + "y: " + str(row))
                    # showValidMoves(1)

                    placeTile(col, row, WHITE)
                    updateBackgroundGrid('p1', col, row)
                    transformTiles(1, col, row)
                    clearGrid()
                    p1Done = True
                    p2Done = False

            # Check/show valid moves

            # Check win/Game End
        # print(grid)
        # clock.tick(60)
        showValidMoves(2)

        while not p2Done and not done:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    x = pos[0]
                    y = pos[1]

                    # translate pix to board coordinate
                    col = int(x/TILESIZE)
                    row = int(y/TILESIZE)
                    # print("X: " + str(col) + "y: " + str(row))

                    placeTile(col, row, RED)
                    updateBackgroundGrid('p2', col, row)
                # Check/show valid moves
                    transformTiles(2, col, row)
                    clearGrid()
                    p2Done = True
                    p1Done = False
                # Check win/Game End

        # print(grid)
   # clock.tick(60)
    pygame.quit()


if __name__ == '__main__':
    main()

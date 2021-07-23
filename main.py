import pygame
import math

#initialise
pygame.init()

#Screen
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

#Title and icon
pygame.display.set_caption("Tic Tac Toe")
icon = pygame.image.load("tic-tac-toe.png")
pygame.display.set_icon(icon)

#FPS
FPS = 15
clock = pygame.time.Clock()

#Color
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

#Fonts
TITLE_FONT = pygame.font.SysFont("Comic Sans MS", 45)

#Center
centerLoc = ["",(250, 175), (400, 175), (550, 175), (250, 325), (400, 325), (550, 325), (250, 475), (400, 475), (550, 475)]
occupied = []
Xs = []
Os = []


def getIndex(x, y):
    for loc in centerLoc[1:]:
        distance = math.sqrt((x - loc[0])**2 + (y - loc[1])**2)
        if distance < 75:
            return centerLoc.index(loc)

def isWinner():
    winner = 0
    for item in [Xs, Os]:
        if (((1 in item) and (2 in item) and (3 in item)) or
            ((4 in item) and (5 in item) and (6 in item)) or
            ((7 in item) and (8 in item) and (9 in item)) or
            ((1 in item) and (4 in item) and (7 in item)) or
            ((2 in item) and (5 in item) and (8 in item)) or
            ((3 in item) and (6 in item) and (9 in item)) or
            ((1 in item) and (5 in item) and (9 in item)) or
            ((7 in item) and (5 in item) and (3 in item))):
            return winner
        else:
            winner += 1
    return winner


#draw
def drawGrid():
    
    #Grid
    pygame.draw.line(screen, BLACK, (WIDTH/2 - 75, HEIGHT/2 - 200), (WIDTH/2 - 75, HEIGHT/2 + 250), 5)
    pygame.draw.line(screen, BLACK, (WIDTH/2 + 75, HEIGHT/2 - 200), (WIDTH/2 + 75, HEIGHT/2 + 250), 5)
    pygame.draw.line(screen, BLACK, (WIDTH/2 - 225, HEIGHT/2 - 50), (WIDTH/2 + 225, HEIGHT/2 -50), 5)
    pygame.draw.line(screen, BLACK, (WIDTH/2 - 225, HEIGHT/2 + 100), (WIDTH/2 + 225, HEIGHT/2 + 100), 5)
    
    pygame.display.update()

def drawXO():
    O = pygame.image.load("rec.png")
    X = pygame.image.load("cancel.png")

    for ind in Os:
        x, y = centerLoc[ind]        
        screen.blit(O, (x - O.get_width()/2, y - O.get_height()/2))
        
    for ind in Xs:
        x, y = centerLoc[ind]
        screen.blit(X, (x - O.get_width()/2, y - O.get_height()/2))
    
    pygame.display.update()

count = 0
#Game Loop
run = True
while run:
    clock.tick(FPS)
    
    screen.fill(WHITE)
    
    #title
    title = TITLE_FONT.render("TIC TAC TOE", 1, (0, 0, 0))
    screen.blit(title, (WIDTH/2 - title.get_width()/2, 50 - title.get_height()/2))

    drawGrid()
    drawXO()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            Mx, My = pygame.mouse.get_pos()
            
            index = getIndex(Mx, My)
            if index != None:
                if index not in occupied:
                    count += 1
                    if count % 2 == 0:
                        Os.append(index)
                        occupied.append(index)
                    else:
                        Xs.append(index)
                        occupied.append(index)
                else:
                    print("occupied")
        if(isWinner() == 0):
            print("X wins")
        if(isWinner() == 1):
            print("O wins")
        

pygame.display.quit()

        

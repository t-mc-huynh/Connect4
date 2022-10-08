import numpy as np
import pygame
import sys
import math

BLUE = (8, 11, 115)
BLACK = (33, 33, 33)
RED = (250, 44, 17)
YELLOW = (250, 250, 17)

ROW = 6
COLUMN = 7

def create_board():
    board = np.zeros((ROW,COLUMN))
    return board

def print_board(board):
    print(np.flip(board, 0))

board = create_board()
print_board(board)
game_over = False
turn = 0

pygame.init()

SQUARESIZE = 100

width = COLUMN * SQUARESIZE
height = (ROW+1) * SQUARESIZE

size = (width, height)
 
RADIUS = int(SQUARESIZE/2 - 5)

screen = pygame.display.set_mode(size)

def draw_board(board):
    for column in range(COLUMN):
        for row in range(ROW):
            pygame.draw.rect(screen, BLUE, (column*SQUARESIZE, row*SQUARESIZE+SQUARESIZE, SQUARESIZE, SQUARESIZE))
            pygame.draw.circle(screen, BLACK, (int(column*SQUARESIZE+SQUARESIZE/2), int(row*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)), RADIUS)
     
    for column in range(COLUMN):
        for row in range(ROW):      
            if board[row][column] == 1:
                pygame.draw.circle(screen, RED, (int(column*SQUARESIZE+SQUARESIZE/2), height-int(row*SQUARESIZE+SQUARESIZE/2)), RADIUS)
            elif board[row][column] == 2: 
                pygame.draw.circle(screen, YELLOW, (int(column*SQUARESIZE+SQUARESIZE/2), height-int(row*SQUARESIZE+SQUARESIZE/2)), RADIUS)
    pygame.display.update()


draw_board(board)
pygame.display.update()

myfont = pygame.font.SysFont("monospace", 75)

def move_pieces(board, row, column, piece):
    board[row][column] = piece
    
def check_valid(board, column):
    return board[5][column] == 0

def place_piece(board, column):
    for i in range(ROW):
        if board[i][column] == 0:
            return i
        
def define_winner(board, piece):
    for column in range(COLUMN-3):
        for row in range(ROW):
            if board[row][column] == piece and board[row][column+1] == piece and board[row][column+2] == piece and board[row][column+3] == piece:
                return True
 
    # Check vertical locations for win
    for column in range(COLUMN):
        for row in range(ROW-3):
            if board[row][column] == piece and board[row+1][column] == piece and board[row+2][column] == piece and board[row+3][column] == piece:
                return True
 
    # Check positively sloped diaganols
    for column in range(COLUMN-3):
        for row in range(ROW-3):
            if board[row][column] == piece and board[row+1][column+1] == piece and board[row+2][column+2] == piece and board[row+3][column+3] == piece:
                return True
 
    # Check negatively sloped diaganols
    for column in range(COLUMN-3):
        for row in range(3, ROW):
            if board[row][column] == piece and board[row-1][column+1] == piece and board[row-2][column+2] == piece and board[row-3][column+3] == piece:
                return True

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        
        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(screen, BLACK, (0,0, width, SQUARESIZE))
            posx = event.pos[0]
            if turn == 0:
                pygame.draw.circle(screen, RED, (posx, int(SQUARESIZE/2)), RADIUS)
            else: 
                pygame.draw.circle(screen, YELLOW, (posx, int(SQUARESIZE/2)), RADIUS)
        pygame.display.update()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.rect(screen, BLACK, (0,0, width, SQUARESIZE))
            #print(event.pos)
            # Ask for Player 1 Input
            if turn == 0:
                posx = event.pos[0]
                col = int(math.floor(posx/SQUARESIZE))
 
                if check_valid(board, col):
                    row = place_piece(board, col)
                    move_pieces(board, row, col, 1)
 
                    if define_winner(board, 1):
                        label = myfont.render("Player 1 wins!!", 1, RED)
                        screen.blit(label, (40,10))
                        game_over = True

            else:               
                posx = event.pos[0]
                col = int(math.floor(posx/SQUARESIZE))
 
                if check_valid(board, col):
                    row = place_piece(board, col)
                    move_pieces(board, row, col, 2)
 
                    if define_winner(board, 2):
                        label = myfont.render("Player 2 wins!!", 1, YELLOW)
                        screen.blit(label, (40,10))
                        game_over = True
            
            print_board(board)
            draw_board(board)
 
            turn += 1
            turn = turn % 2
 
            if game_over:
                pygame.time.wait(3000)
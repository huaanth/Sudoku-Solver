import pygame
from main import random_board, solve, valid
import time

pygame.font.init()

class Grid:
    board = random_board()

    def __init__(self, rows, cols, width, height, win):
        self.rows = rows
        self.cols = cols
        self.width = width
        self.height = height
        self.win = win

class Box:
    #will draw the stuff in the box
    rows = 9
    cols = 9
    def __init__(self, value, row, col, width, height):
        self.value = value
        self.temp = 0
        self.row= row
        self.col = col
        self.width = width
        self.height = height
        self.selected = False        
        
def main():
    win = pygame.display.set_mode((540,600))
    pygame.display.set_caption("Sudoku")
    board = Grid(9,9,540,540,win)
    key = None
    run = True
    start_time = time.time()
    wrong =0
    while run:
        play_time = round(time.time()- start_time)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    key=1
                if event.key == pygame.K_2:
                    key=2
                if event.key == pygame.K_3:
                    key=3
                if event.key == pygame.K_4:
                    key=4
                if event.key == pygame.K_5:
                    key=5
                if event.key == pygame.K_6:
                    key=6
                if event.key == pygame.K_7:
                    key=7
                if event.key == pygame.K_8:
                    key=8
                if event.key == pygame.K_9:
                    key=9
                if event.key == pygame.K_KP1:
                    key=1
                if event.key == pygame.K_KP2:
                    key=2
                if event.key == pygame.K_KP3:
                    key=3
                if event.key == pygame.K_KP4:
                    key=4
                if event.key == pygame.K_KP5:
                    key=5
                if event.key == pygame.K_KP6:
                    key=6
                if event.key == pygame.K_KP7:
                    key=7
                if event.key == pygame.K_KP8:
                    key=8
                if event.key == pygame.K_KP9:
                    key=9
        

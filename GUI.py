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
        pass #continue tomorrow

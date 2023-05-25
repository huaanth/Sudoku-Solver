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

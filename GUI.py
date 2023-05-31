import pygame
from main import random_board, solve, valid, find_empty
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
        self.boxes = [[Box(self.board[i][j],i,j,width,height) for j in range(cols)]for i in range(rows)]
        self.model = None
        self.update_model()
        self.selected = None
    
    def update_model(self):
        self.model =[[self.boxes[i][j].value for j in range(self.cols)] for i in range(self.rows)]
    
    def place (self,val):
        row, col = self.selected
        if self.boxes[row][col].value == 0:
            self.boxes[row][col].set(val)
            self.update_model()

            if valid(self.model,val, (row,col)) and solve(self.model):
                return True
            else:
                self.boxes[row][col].set(0)
                self.boxes[row][col].temp_set(0)
                self.update_model()
                return False
            
    def sketch(self, val):
        row, col = self.selected
        self.boxes[row][col].temp_set(val)
    
    def draw(self):
        #lines
        dist = self.width/9
        for i in range(self.rows+1):
            if i%3 == 0 and i !=0:
                t = 4
            else:
                t = 1
            pygame.draw.line(self.win, (0,0,0),(0, i*dist),(self.width, i*dist), t)
            pygame.draw.line(self.win, (0,0,0),(i*dist,0),(i*dist,self.height), t)
        #the boxes
        for i in range(self.rows):
            for j in range(self.cols):
                self.boxes[i][j].draw(self.win)
    
    def select(self,row,col):
        #will reset all other boxes and only allow one box to be selected
        for i in range(self.rows):
            for j in range(self.cols):
                self.boxes[i][j].selected = False
        
        self.boxes[row][col].selected = True
        self.selected = (row,col)

    def clear(self):
        row,col = self.selected
        if self.boxes[row][col].value ==0:
            self.boxes[row][col].temp_set(0)
            
    def click(self, pos):
        if pos[0] < self.width and pos[1] < self.height:
            dist = self.width /9
            x = pos[0]// dist
            y = pos[1] // dist
            return (int(y), int(x))
        else:
            return None
    
    def is_finished(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.boxes[i][j].value == 0:
                    return False
        return True
    
    def solve_gui(self):
        self.update_model()
        find = find_empty(self.model)
        if not find:
            return True
        else:
            row, col = find

        for i in range(1,10):
            if valid(self.model,i, (row,col)):
                self.model[row][col] = i
                self.boxes[row][col].set(i)
                self.boxes[row][col].change(self.win, True)
                self.update_model()
                pygame.display.update()
                pygame.time.delay(100)
            
                if self.solve_gui():
                    return True
            
                self.model[row][col] =0
                self.boxes[row][col].set(0)
                self.update_model()
                self.boxes[row][col].change(self.win, False)
                pygame.display.update()
                pygame.time.delay(100)
                
        return False
            
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
        
    def draw(self,win):
        fnt = pygame.font.SysFont("timesnewroman",40)
        dist = self.width/9
        x = self.col *dist
        y= self.row *dist

        if self.temp!= 0 and self.value == 0:
            text = fnt.render(str(self.temp), 1, (128,128,128))
            win.blit(text, (x+5,y+5))
        elif not(self.temp ==0):
            #need this to create the text from (1-9)
            text = fnt.render(str(self.value), 1, (0,0,0))
            #allows for the pixels to go on the screen
            win.blit(text,(x+(dist - text.get_width()/2), y+(dist - text.get_width()/2)))
        
        if self.selected:
            pygame.draw.rect(win,(255, 0, 0), (x,y,dist,dist),3)
    
    def change(self, win, w=True):
        fnt = pygame.font.SysFont("timesnewroman",40)
        dist = self.width/9
        x = self.col *dist
        y= self.row *dist
        pygame.draw.rect(win,(255, 255, 255), (x,y,dist,dist),0)
        text = fnt.render(str(self.value), 1, (0,0,0))
        win.blit(text,(x+(dist - text.get_width()/2), y+(dist - text.get_width()/2)))

        if w:
            pygame.draw.rect(win,(0, 255, 0), (x,y,dist,dist),3)
        else:
            pygame.draw.rect(win,(255, 0, 0), (x,y,dist,dist),3)
    
    def set(self, val):
        self.value = val
    
    def temp_set(self,val):
        self.temp = val

def form_time(t):
    sec = t%60
    min = t//60
    form = " " + str(min) +": "+str(sec)
    return form

def redraw_window(win,board,time,strikes):
    win.fill((255,255,255))
    #draw the time
    fnt = pygame.font.SysFont("timesnewroman",40)
    text = fnt.render("Time: " +form_time(time),1 ,(0,0,0))
    win.blit(text, (540 - 160,560))
    #draw the strikes
    text = fnt.render("X "*strikes,1,(255,0,0))
    win.blit(text,(20,560))
    board.draw()
    
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
                if event.key == pygame.K_DELETE:
                    board.clear()
                    key = None
                if event.key == pygame.K_SPACE:
                    board.solve_gui()
                if event.key == pygame.K_RETURN:
                    row,col = board.selected
                    if board.boxes[row][col].temp !=0:
                        if board.place(board.boxes[row][col].temp):
                            print("Success")
                        else:
                            print("Wrong")
                            wrong +=1
                        key = None
                        if board.is_finished():
                            print("Game Over")
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                clicked = board.click(pos)
                if clicked:
                    board.select(clicked[0],clicked[1])
                    key= None
        if board.selected and key != None:
            board.sketch(key)
        redraw_window(win,board,play_time,wrong)
        pygame.display.update()
main()
pygame.quit()
        


import pygame

SCREEN_WIDTH = 300 #屏幕宽度
SCREEN_HEIGHT = 300 #屏幕高度
BOARD_ROWS = 3 #行
BOARD_COLS = 3 #列 

NOT_END = 0
DRAW = 1
HUMAN_WIN = 2
COMPUTER_WIN = 3
EMPTY = 0
HUMAN = 1
COMPUTER = 2
Status = 1
BOARD_SIZE = 100 #棋盘大小
BOARD_COLOR = (0, 0 , 0) #棋盘颜色
BOARD_LINE_WIDTH = 3 #线宽
PLAYER_COLOR = (255 , 0 , 0) #玩家颜色
COMPUTER_COLOR = (0, 0, 255) #机器颜色
OPTION = [(1, 1), (0, 0), (0, 2), (2, 0), (2, 2), (0, 1), (1, 0), (1, 2), (2, 1)] #最佳序列
board = [[EMPTY for _ in range(3)] for _ in range(3)] #初始化为空
import os
os.chdir("C:/Users/28314/Desktop/codescat/Python")
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("井字棋")
def check_move(x,y):
    if x >= 3 or x < 0 or y < 0 or y >= 3:
        return False
    elif board[x][y] == EMPTY:
        return True
    elif board[x][y] == HUMAN or board[x][y] == COMPUTER:
        return False
def check_Player_win():
    for i in range(3):
        if board[i][0] == HUMAN and board[i][1] == HUMAN and board[i][2] == HUMAN:
            return True
        if board[0][i] == HUMAN and board[1][i] == HUMAN and board[2][i] == HUMAN:
            return True
    if board[0][0] == HUMAN and board[1][1] == HUMAN and board[2][2] == HUMAN:
        return True
    if board[0][2] == HUMAN and board[1][1] == HUMAN and board [2][0] == HUMAN:
        return True
    return False
def check_computer_win():
    for i in range(3):
        if board[i][0] == COMPUTER and board[i][1] == COMPUTER and board[i][2] == COMPUTER:
            return True
        if board[0][i] == COMPUTER and board[1][i] == COMPUTER and board[2][i] == COMPUTER:
            return True
    if board[0][0] == COMPUTER and board[1][1] == COMPUTER and board[2][2] == COMPUTER:
        return True
    if board[0][2] == COMPUTER and board[1][1] == COMPUTER and board [2][0] == COMPUTER:
        return True
    return False
def check_draw():
    if check_computer_win() == False and check_Player_win() == False:
        for i in range(3):
            for j in range(3):
                if board[i][j] == 0:
                    return False
        return True
    return False
def computer_move():
    for i in range(3):
        if board[i][0] == EMPTY and board[i][1] == COMPUTER and board[i][2] == COMPUTER:
            return (i,0)
        if board[i][1] == EMPTY and board[i][0] == COMPUTER and board[i][2] == COMPUTER:
            return (i,1)
        if board[i][2] == EMPTY and board[i][1] == COMPUTER and board[i][0] == COMPUTER:
            return (i,2)
        if board[0][i] == EMPTY and board[1][i] == COMPUTER and board[2][i] == COMPUTER:
            return (0,i)
        if board[1][i] == EMPTY and board[0][i] == COMPUTER and board[2][i] == COMPUTER:
            return (1,i)
        if board[2][i] == EMPTY and board[1][i] == COMPUTER and board[0][i] == COMPUTER:
            return (2,i)
    if board[0][0] == EMPTY and board[1][1] == COMPUTER and board[2][2] == COMPUTER:
        return (0,0)
    if board[1][1] == EMPTY and board[0][0] == COMPUTER and board[2][2] == COMPUTER:
        return (1,1)
    if board[2][2] == EMPTY and board[1][1] == COMPUTER and board[0][0] == COMPUTER:
        return (2,2)
    if board[0][2] == EMPTY and board[1][1] == COMPUTER and board[2][0] == COMPUTER:
        return (0,2)
    if board[1][1] == EMPTY and board[0][2] == COMPUTER and board[2][0] == COMPUTER:
        return (1,1)
    if board[2][0] == EMPTY and board[1][1] == COMPUTER and board[0][2] == COMPUTER:
        return (2,0)
    for i in range(3):
        if board[i][0] == EMPTY and board[i][1] == HUMAN and board[i][2] == HUMAN:
            return (i,0)
        if board[i][1] == EMPTY and board[i][0] == HUMAN and board[i][2] == HUMAN:
            return (i,1)
        if board[i][2] == EMPTY and board[i][1] == HUMAN and board[i][0] == HUMAN:
            return (i,2)
        if board[0][i] == EMPTY and board[1][i] == HUMAN and board[2][i] == HUMAN:
            return (0,i)
        if board[1][i] == EMPTY and board[0][i] == HUMAN and board[2][i] == HUMAN:
            return (1,i)
        if board[2][i] == EMPTY and board[1][i] == HUMAN and board[0][i] == HUMAN:
            return (2,i)
    if board[0][0] == EMPTY and board[1][1] == HUMAN and board[2][2] == HUMAN:
        return (0,0)
    if board[1][1] == EMPTY and board[0][0] == HUMAN and board[2][2] == HUMAN:
        return (1,1)
    if board[2][2] == EMPTY and board[1][1] == HUMAN and board[0][0] == HUMAN:
        return (2,2)
    if board[0][2] == EMPTY and board[1][1] == HUMAN and board[2][0] == HUMAN:
        return (0,2)
    if board[1][1] == EMPTY and board[0][2] == HUMAN and board[2][0] == HUMAN:
        return (1,1)
    if board[2][0] == EMPTY and board[1][1] == HUMAN and board[0][2] == HUMAN:
        return (2,0)
    for item in OPTION:
        if board[item[0]][item[1]] == EMPTY:
            return item
    gameover()
    return (4,4)
def gameover():
    if check_computer_win() and check_Player_win():
        gameOverFont = pygame.font.Font('pytext.ttf',72)
        gameOverSurf = gameOverFont.render('Its a Draw!!!',True,(0,0,0))
        gameOverRect = gameOverSurf.get_rect()
        gameOverRect.center = (SCREEN_HEIGHT // 2,SCREEN_WIDTH // 2)
        screen.blit(gameOverSurf,gameOverRect)
        pygame.display.update()
    elif check_Player_win():
        gameOverFont = pygame.font.Font('pytext.ttf',64)
        gameOverSurf = gameOverFont.render('You Win!!!',True,(0,0,0))
        gameOverRect = gameOverSurf.get_rect()
        gameOverRect.center = (SCREEN_HEIGHT // 2,SCREEN_WIDTH // 2)
        screen.blit(gameOverSurf,gameOverRect)
        pygame.display.update()
    elif check_computer_win():
        gameOverFont = pygame.font.Font('pytext.ttf',64)
        gameOverSurf = gameOverFont.render('You Lose!!!',True,(0,0,0))
        gameOverRect = gameOverSurf.get_rect()
        gameOverRect.center = (SCREEN_HEIGHT // 2,SCREEN_WIDTH // 2)
        screen.blit(gameOverSurf,gameOverRect)
        pygame.display.update()
    elif check_draw():
        gameOverFont = pygame.font.Font('pytext.ttf',64)
        gameOverSurf = gameOverFont.render('Its a Draw!!!',True,(0,0,0))
        gameOverRect = gameOverSurf.get_rect()
        gameOverRect.center = (SCREEN_HEIGHT // 2,SCREEN_WIDTH // 2)
        screen.blit(gameOverSurf,gameOverRect)
        pygame.display.update()
screen.fill((255,255,255))
for row in range(BOARD_ROWS):
    for col in range(BOARD_COLS):
        rect = pygame.Rect(col * BOARD_SIZE, row * BOARD_SIZE, BOARD_SIZE, BOARD_SIZE)
        pygame.draw.rect(screen, BOARD_COLOR, rect, BOARD_LINE_WIDTH)
pygame.display.update()
running = True
Status = True
while running == True:
    for even in pygame.event.get():
        if even.type == pygame.QUIT:
            running = False
        if Status == False:
            continue
        if even.type == pygame.MOUSEBUTTONDOWN and Status == True:
            x, y = pygame.mouse.get_pos()
            col = x // BOARD_SIZE
            row = y // BOARD_SIZE
            if check_move(row,col) == True:
                board[row][col] = HUMAN
                player_x = col
                player_y = row
                center_x = player_x * BOARD_SIZE + BOARD_SIZE // 2
                center_y = player_y * BOARD_SIZE + BOARD_SIZE // 2
                pygame.draw.circle(screen, PLAYER_COLOR, (center_x, center_y), BOARD_SIZE // 2 - BOARD_LINE_WIDTH)
                pygame.display.update()
                item = computer_move()
                if item[0] != 4:
                    board[item[0]][item[1]] = COMPUTER
                    computer_x = item[1]
                    computer_y = item[0]
                    center_x = computer_x * BOARD_SIZE + BOARD_SIZE // 2
                    center_y = computer_y * BOARD_SIZE + BOARD_SIZE // 2
                    pygame.draw.circle(screen, COMPUTER_COLOR, (center_x, center_y), BOARD_SIZE // 2 - BOARD_LINE_WIDTH)
                    pygame.display.update()
            if check_computer_win() or check_Player_win() or check_draw():
                gameover()
                Status = False

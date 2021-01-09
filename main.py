import pygame
import time
from Check import check, isDraw
from bot import best_move
from copy import deepcopy
import random
board = [["0", "0", "0", "0", "0", "0", "0"],
	    ["0", "0", "0", "0", "0", "0", "0"],
	    ["0", "0", "0", "0", "0", "0", "0"],
	    ["0", "0", "0", "0", "0", "0", "0"],
	    ["0", "0", "0", "0", "0", "0", "0"],
	    ["0", "0", "0", "0", "0", "0", "0"]]

swap = {"R": "Y", "Y": "R"}
turn = "R"
gameOver = False
bot = 1
depth = 3

def draw_grid():
	pygame.draw.rect(screen, (0,191,255), (0,0,560,480))
	for i in range(6):
		for j in range(7):
			x = 40 + 80*j
			y = 40 + 80*i
			color = (255,255,255)
			if board[i][j]=="R":
				color = (255, 0, 0)
			elif board[i][j]=="Y":
				color = (255, 255, 0)
			pygame.draw.circle(screen, color, (x,y), 35)

def win(turn):
	global gameOver
	gameOver = True
	if turn=="R":
		turn = "Red"
	else:
		turn = "Yellow"

	font=pygame.font.SysFont(None,60)#font for setting font size and style
	screen_text=font.render(turn+' is Winner!!',True,(0,0,0))
	screen.blit(screen_text,[120,500])

def draw():
	global gameOver
	gameOver = True
	font=pygame.font.SysFont(None,60)#font for setting font size and style
	screen_text=font.render('Draw!!!',True,(0,0,0))
	screen.blit(screen_text,[120,500])	


def drop_coin_animation(a,b,c):
	pass


def drop_coin(color,row):
    for i in range(5,-1,-1):
        drop_coin_animation(i,row,color)
        if board[i][row]=="0":
            board[i][row]=color
            break

def click(row):
	if gameOver or board[0][row]!="0":
		return
	global turn
	drop_coin(turn,row)

	if check(board):
		win(turn)
	elif isDraw(board):
		draw()

	
	turn = swap[turn]

def play(row,onlybot=0):
	if not onlybot: click(row)
	if bot:
		row = best_move(deepcopy(board),turn,depth)
		click(row)
	

def frame_update():
	draw_grid()
	pygame.display.update()


pygame.init()

pygame.display.set_mode((560,560))
pygame.display.set_caption("connect4")
screen = pygame.display.get_surface()
screen.fill((255, 255, 255))

if random.choice([0,1]):
	play(None,onlybot=1)


while 1:
	for i in pygame.event.get():
		if i.type==pygame.QUIT:
			pygame.quit()
			exit()
		elif i.type==pygame.MOUSEBUTTONDOWN:
			row = i.pos[0]//80
			play(row)

		frame_update()
	
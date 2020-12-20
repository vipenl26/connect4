import pygame

m =  [["0", "0", "0", "0", "0", "0", "0"],
	  ["0", "0", "0", "0", "0", "0", "0"],
	  ["0", "0", "0", "0", "0", "0", "0"],
	  ["0", "0", "0", "0", "0", "0", "0"],
	  ["0", "0", "0", "0", "0", "0", "0"],
	  ["0", "0", "0", "0", "0", "0", "0"]]

def draw_grid():
	pygame.draw.rect(screen, (0,191,255), (0,0,560,480))
	for i in range(6):
		for j in range(7):
			x = 40 + 80*j
			y = 40 + 80*i
			color = (255,255,255)
			if m[i][j]=="R":
				color = (255, 0, 0)
			elif m[i][j]=="Y":
				color = (255, 255, 0)
			pygame.draw.circle(screen, color, (x,y), 35)

def draw_coins():
	pass

def drop_coin(color, x, y):
	pass

def click(row):
	print(row)
	pass


pygame.init()

pygame.display.set_mode((560,560))
pygame.display.set_caption("connect4")
screen = pygame.display.get_surface()
screen.fill((255, 255, 255))


draw_grid()

while 1:
	for i in pygame.event.get():
		if i.type==pygame.QUIT:
			pygame.quit()
			exit()
		elif i.type==pygame.MOUSEBUTTONDOWN:
			row = i.pos[0]//80
			click(row)
	pygame.display.update()
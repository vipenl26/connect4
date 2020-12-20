import pygame



pygame.init()

pygame.display.set_mode((600,600))
pygame.display.set_caption("connect4")
screen=pygame.display.get_surface()

while 1:
	for i in pygame.event.get():
		if i.type==pygame.QUIT:
			pygame.quit()
			exit()
	pygame.display.update()
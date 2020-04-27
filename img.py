import pygame
import random

pygame.init()
width=800
height=600
disp=pygame.display.set_mode((width,height))
pygame.display.set_caption('Race Game')
clk=pygame.time.Clock()
car=pygame.image.load("car.png")
enemy=pygame.image.load("car2.jpg")

crashed=False


while not crashed:
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			pygame.quit()
			quit()
	disp.fill((255,255,255))
	disp.blit(car,(400,500))
	disp.blit(enemy,(400,0))
	pygame.display.update()
	clk.tick(60)
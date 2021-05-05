import pygame,sys

clock = pygame.time.Clock()
from pygame.locals import *
pygame.init()
pygame.display.set_caption("Game")
Window_size = (400,400)
screen = pygame.display.set_mode(Window_size,0,32)
player_img = pygame.image.load('images/player.png')

moving_right = False
moving_left = False
jumping = False

player_loc = [50,50]

movement_speed = 10
jump_speed = 0.2

jump = 0

fill = (2,2,2)

player_rect = pygame.Rect(player_loc[0],player_loc[1],player_img.get_width(), player_img.get_height())
test_rect = pygame.Rect(100,100,100,50)


while True:

	screen.fill(fill)

	screen.blit(player_img,player_loc)

	if player_loc[1] > Window_size[1]-player_img.get_height():
		jump = -jump
	else:
		jump += jump_speed
	player_loc[1] += jump

	if moving_right == True:
		player_loc[0] += movement_speed
	
	if moving_left == True:
		player_loc[0] -= movement_speed

	player_rect.x = player_loc[0]
	player_rect.y = player_loc[1]

	if player_rect.colliderect(test_rect):
		pygame.draw.rect(screen,(255,0,0),test_rect)
	else:
		pygame.draw.rect(screen,(240,0,0),test_rect)




	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()

		if event.type == KEYDOWN:

			if event.key == K_RIGHT:
				moving_right = True
				print("RIGHT")

			if event.key == K_LEFT:
				moving_left = True
				print("LEFT")

			if event.key == K_SPACE:
				jumping = True
				print("SPACE")

		if event.type == KEYUP:

			if event.key == K_RIGHT:
				moving_right = False
				print("RIGHT DISABLED")

			if event.key == K_LEFT:
				moving_left = False
				print("LEFT DISABLED")

			if event.key == K_SPACE:
				jumping = False
				print("SPACE DISABLED")


	pygame.display.update()
	clock.tick(60)
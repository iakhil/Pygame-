import pygame

#Initializing pygame.
pygame.init()

#Creating a window of size 500x400
win = pygame.display.set_mode((500,480))

#Setting the window's caption.
pygame.display.set_caption("Check Collision")

#Initializing run variable as True.
run = True

#Initializing the velocity variable as 2.
vel = 2

#RGB code of white color.
white = (255,255,255)

#RGB code of black color.
black = (0,0,0)

#Declaring x and y coordinates.
x = 100
y = 40

#Function to check collision. The function takes in two arguments--the two rectangles.

def det_col(rec1,rec2):

	#Using pygame's colliderect function.

	if(pygame.Rect.colliderect(rec1,rec2)):

		#Terminating the main loop when collision is detencted.
		run = False
		print("Collision detected!")
	else:
		run = True

	return run




while(run):

	#Defining first rectangle using pygame.rect.
	
	rec1 = pygame.Rect(x,y,50,40)
	
	#Defining second rectangle.
	rec2 = pygame.Rect(120,250,60,50)
	
	#Drawing first rectangle..
	pygame.draw.rect(win,(white),rec1)

	#Drawings second rectangle.


	pygame.draw.rect(win,(222,112,33),rec2)

	#Updating the display.
	pygame.display.update()

	for event in pygame.event.get():

		if(event.type == pygame.QUIT):

			run = False

	#Creating an instance of keys.

	keys = pygame.key.get_pressed()

	#Controlling left movement.

	if(keys[pygame.K_LEFT]):

		x -= vel

		run = det_col(rec1,rec2)


	#Controlling right movement.
		
	if(keys[pygame.K_RIGHT]):

		x += vel

		run = det_col(rec1,rec2)
		


	#Controlling up movement. 	

	if(keys[pygame.K_UP]):

		y -= vel

		#x += vel

		run = det_col(rec1,rec2)
				
	#Controlling down movement.

	if(keys[pygame.K_DOWN]):

		
		y += vel


		run = det_col(rec1,rec2)
			
	#Filling the window with black color to conceal rectangle's previous movements.

	win.fill((0,0,0))
	
	pygame.display.update()
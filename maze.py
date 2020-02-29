import pygame

pygame.init()
win = pygame.display.set_mode((500,480))
pygame.font.init()

s = 0

text = pygame.font.SysFont('cominsanms',50)

text_surface = text.render(f'Score: {s}',False,(255,255,255))






#screen = pygame.display()
x = 50
y = 380

hitbox = (x + 20, y, 30, 40)
vel = 5
left = False
right = False
up = False
down = False
walkCount = 0
color = (123,44,199)
line_color = (255,255,255)
clock = pygame.time.Clock()
walkRight = [pygame.image.load('R1.png'),pygame.image.load('R2.png'),pygame.image.load('R3.png'),pygame.image.load('R4.png'),pygame.image.load('R5.png'),
pygame.image.load('R6.png'),pygame.image.load('R7.png'),pygame.image.load('R8.png'),pygame.image.load('R9.png')]

walkLeft = [pygame.image.load('L1.png'),pygame.image.load('L2.png'),pygame.image.load('L3.png'),pygame.image.load('L4.png'),pygame.image.load('L5.png'),
pygame.image.load('L6.png'),pygame.image.load('L7.png'),pygame.image.load('L8.png'),pygame.image.load('L9.png')]

char = pygame.image.load("standing.png")

run = True

black = (0,0,0)

def maz():
	
	pygame.draw.line(win,line_color,(60,30),(260,30),4)
	pygame.display.flip()

def coin():

	wall = pygame.image.load("wall.png")
	
	coin = pygame.image.load("coin.png")

	vel = pygame.image.load("velo.png")

	wall = pygame.image.load("swall.jpg")

	coin_rect = coin.get_rect()

	pygame.draw.rect(win,(255,0,0),coin_rect,2)

	#global coin

	#global rec1 

	rec1 = (50,100,30,40)

	#pygame.colliderect(rec1,)
	#pygame.draw.rect(win,(255,0,0),coin_rect,2)
	
	pygame.draw.rect(win,(0,0,0),hitbox,2)

	win.blit(coin,(50,100))

	win.blit(coin,(169,240))

	win.blit(coin,(440,260))

	win.blit(coin,(130,400))

	#win.blit(wall,(30,289))
	
	pygame.display.flip()









def redrawGameWindow():
	global walkCount
	win.blit(win,(0,0))
	if(walkCount + 1 > 27):
		walkCount = 0


	
	if(left):
		win.blit(walkLeft[walkCount//3],(x,y))
		walkCount += 1
		#win.blit(win,(x,y))
		#win.fill(black)


	elif(right):
		win.blit(walkRight[walkCount//3],(x,y))
		walkCount += 1
		#win.blit(win,(x,y))

	else:
		win.blit(char, (x,y))

	#win.fill(black)
	hitbox = (x + 20, y+10, 25, 55)

	pygame.draw.rect(win,(0,0,255),hitbox,2)
	pygame.display.update()

	#win.fill(color)

while(run):

	ticks = pygame.time.get_ticks()	
	seconds = (20000 - ticks)/1000

	counter = text.render(f'Time: {seconds}',False,(0,199,255))

	if(seconds == 0):

		game_over = text.render("Game Over",False,(255,255,255))

		win.blit(game_over,(250,300))

		pygame.display.update()

	win.blit(text_surface,(300,80))

	pygame.display.update()


	win.blit(counter,(280,400))

	pygame.display.update()
	clock.tick(27) 


	for event in pygame.event.get():
		if(event.type == pygame.QUIT):
			run = False

	keys = pygame.key.get_pressed()

	if(keys[pygame.K_LEFT] and x > vel):
		x -= vel
		left = True
		right = False


	elif(keys[pygame.K_RIGHT] and x < 500 - vel):

		x += vel
		left = False
		right = True


	elif(keys[pygame.K_UP] and y > vel):
		
		up = True
		down = False
		y -= vel


		"""
		"""
	if(keys[pygame.K_DOWN]):
			down = True
			up = False
			y += vel

		#return(x,y)
	win.fill(black)

	#return x
	#	return y
	"""
	#if(x == 50 and y == 100):
	#run = False

	"""
	"""
	def check_coll(x,y):

		if((x >= 50) and (y < 105)):

			
			s += 10

			win.fill(black, (50,100,20,30))
			
			pygame.draw.rect(win,(100,233,114),(50,100,40,30))

			pygame.display.update()


	



	"""
	"""def check_coll(x,y):

	if(x == 50 and y == 100):
c
		s += 10

		pygame.draw.rect(win,(100,233,114),(50,100,40,30))

		pygame.display.update()

	"""


	#maz()
	#check_coll()

	redrawGameWindow()
	#move()
	coin()



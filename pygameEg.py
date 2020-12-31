#Arushi's code!
#printing the cords where user points the mouse using some functions from pygame module!
import pygame 
x = y = 0
running = 1
screen = pygame.display.set_mode((640, 400))

while running:
    for event in pygame.event.get():
    #event = pygame.event.poll()
       if event.type == pygame.QUIT:
           running = 0
       if event.type == pygame.MOUSEBUTTONDOWN:    #Checking the condition when the mouse pointer get pressed!
            
            print ("mouse at (%d, %d)" % event.pos)
   

    screen.fill((200, 50, 50))
    pygame.display.update()
pygame.quit()

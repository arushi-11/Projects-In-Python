#code to draw a line with the points where the user presses the mousepointer!
import pygame
pygame.init()

white=(255,255,255)
green=(0,255,0)

l=[]
temp=0
window=pygame.display.set_mode((500,400))
pygame.display.set_caption("MY GAME WINDOW")
running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event.type is pygame.MOUSEBUTTONDOWN:    #Checking the condition when the mouse pointer get pressed!
            x= pygame.mouse.get_pos()       #copy the coordinates of the position into x!
            l.append(x)
            temp+=1
    window.fill((200,50,50)) 
    if temp>=2:
        pygame.draw.line(window,green,l[0],l[1],10)
    pygame.display.update()
pygame.quit()

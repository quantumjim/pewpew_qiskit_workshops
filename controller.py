import pygame

with open('input.txt','w') as file:
    file.write('')

pygame.init()
clock = pygame.time.Clock()

pygame.display.init()
screen = pygame.display.set_mode((400, 225))

background = pygame.image.load("controller.png").convert()
background = pygame.transform.scale(background, (400, 225))

screen.blit(background, (0,0))
pygame.display.flip()

pos = {'l':(57,116),'u':(107, 56),'r':(163, 112),'d':(103, 172),'o':(355, 85),'x':(294, 143)}
w = 30

while True:
    
    for event in pygame.event.get():  
        if event.type == pygame.MOUSEBUTTONDOWN:
            (x,y) = event.pos
            for b in pos:
                if (x<(pos[b][0]+w)) and (x>(pos[b][0]-w)) and (y<(pos[b][1]+w)) and (y>(pos[b][1]-w)):
                    with open('input.txt','a') as file:
                        file.write(b)
                
    clock.tick(20)
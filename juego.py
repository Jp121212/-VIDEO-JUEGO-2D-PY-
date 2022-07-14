import pygame 
pygame.init()

size = (800,500)

##Mis colores
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)


##Creando la pantalla
screen = pygame.display.set_mode(size)

while True:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    screen.fill(white)
    ##Dibujo
    pygame.draw.line(screen,red,[0,0],[100,100])

    #Dibujo


    ##Aqui se actualiza la pantalla
    pygame.display.flip()
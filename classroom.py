import sys,pygame

pygame.init()

size = height, width = 800,600

screen = pygame.display.set_mode(size)

background = pygame.image.load("classroom.png")
player = pygame.image.load("stickfig.png")

x,y = 0,0
speed = 8 

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    keys=pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x = x - speed

    if keys[pygame.K_RIGHT]:
        x = x + speed

    if keys[pygame.K_UP]:
        y = y - speed

    if keys[pygame.K_DOWN]:
        y = y + speed

    screen.blit(background,(0,0))

    screen.blit(player,(x,y))

    pygame.display.flip()

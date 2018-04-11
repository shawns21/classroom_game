import sys,pygame

class Wall(pygame.sprite.Sprite):
    def __init__(self, width, height):
        super(Wall, self).__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill((0,0,0))
        self.rect = self.image.get_rect()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()

        self.image = pygame.image.load("stickfig.png")
        self.rect = self.image.get_rect()


pygame.init()

size = height, width = 800,600
screen = pygame.display.set_mode(size)

background = pygame.image.load("classroom.png")

speed = 5 

wall_list = pygame.sprite.Group()
all_list = pygame.sprite.Group()

wall1 = Wall(1,105)
wall1.rect.x = 265
wall1.rect.y = 0

wall2 = Wall(1,90)
wall2.rect.x = 265
wall2.rect.y = 207

wall3 = Wall(265,1)
wall3.rect.x = 0
wall3.rect.y = 300

wall4 = Wall(1,102)
wall4.rect.x = 535
wall4.rect.y = 0

wall5 = Wall(1,99)
wall5.rect.x = 535
wall5.rect.y = 200

wall6 = Wall(265,1)
wall6.rect.x = 535
wall6.rect.y = 300

wall7 = Wall(1,88)
wall7.rect.x = 265
wall7.rect.y = 300

wall8 = Wall(1,110)
wall8.rect.x = 265
wall8.rect.y = 490

wall9 = Wall(1,140)
wall9.rect.x = 535
wall9.rect.y = 300

wall10 = Wall(1,61)
wall10.rect.x = 535
wall10.rect.y = 539

wall11 = Wall(1,600)
wall11.rect.x = 0
wall11.rect.y = 0

wall12 = Wall(800,1)
wall12.rect.x = 0
wall12.rect.y = 0

wall13 = Wall(800,1)
wall13.rect.x = 0
wall13.rect.y = 600

wall14 = Wall(1,600)
wall14.rect.x = 800
wall14.rect.y = 0


wall_list.add(wall1)
wall_list.add(wall2)
wall_list.add(wall3)
wall_list.add(wall4)
wall_list.add(wall5)
wall_list.add(wall6)
wall_list.add(wall7)
wall_list.add(wall8)
wall_list.add(wall9)
wall_list.add(wall10)
wall_list.add(wall11)
wall_list.add(wall12)
wall_list.add(wall13)
wall_list.add(wall14)

all_list.add(wall1)
all_list.add(wall2)
all_list.add(wall3)
all_list.add(wall4)
all_list.add(wall5)
all_list.add(wall6)
all_list.add(wall7)
all_list.add(wall8)
all_list.add(wall9)
all_list.add(wall10)
all_list.add(wall11)
all_list.add(wall12)
all_list.add(wall13)
all_list.add(wall14)

p1 = Player()
p1.rect.x = 380
p1.rect.y = 280

all_list.add(p1)

clock = pygame.time.Clock()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    x,y = 0,0

    keys=pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x = x - speed

    if keys[pygame.K_RIGHT]:
        x = x + speed

    if keys[pygame.K_UP]:
        y = y - speed

    if keys[pygame.K_DOWN]:
        y = y + speed

    p1.rect.x = p1.rect.x + x
    p1.rect.y = p1.rect.y + y

    for wall in pygame.sprite.spritecollide(p1, wall_list, False):
        if x < 0:
            p1.rect.left = wall.rect.right
        if x > 0:
            p1.rect.right = wall.rect.left
        if y > 0:
            p1.rect.bottom = wall.rect.top
        if y < 0: 
            p1.rect.top = wall.rect.bottom

    screen.blit(background, (0,0))
    all_list.draw(screen)

    pygame.display.flip()

    clock.tick(30)

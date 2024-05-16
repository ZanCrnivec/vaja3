import pygame
import sys
import random
pygame.init()

display = pygame.display.set_mode((1000,800))
pygame.display.set_caption("Nočna straža")
pygame.display.set_icon(pygame.image.load("drevo.png"))
clock = pygame.time.Clock()


class Player:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    def main(self, display):
        pygame.draw.rect(display, (255,0,0), (self.x, self.y, self.width, self.height)), 

class Tree:
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = image
    def draw(self, display, scroll):
        display.blit(self.image, (self.x - scroll[0], self.y - scroll[1]))

class Stick:
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = pygame.transform.scale(image, (100, 100))
    def draw(self, display, scroll):
        display.blit(self.image, (self.x - scroll[0], self.y - scroll[1]))

class StaminaBar():
    def __init__(self, x, y, width, height, max_stamina,):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.stamina = max_stamina
        self.max_stamina = max_stamina  
    def draw(self, display):    
        ratio = self.stamina / self.max_stamina
        pygame.draw.rect(display, "black", (self.x, self.y, self.width, self.height))
        pygame.draw.rect(display, "white", (self.x+4, self.y+4, (self.width * ratio)-8, self.height-8))

stamina_bar = StaminaBar(325, 600, 400, 30, 100)

tree_list = []
for i in range(100):
    tree = Tree(random.randint(-2000, 2000), random.randint(-2000, 2000), pygame.image.load("drevo.png"))
    tree_list.append(tree)
    tree_list.sort(key=lambda tree: tree.y)

stick_amount = 0
stick_list = []
def spawn_stick():
    stick = Stick(random.randint(-2000, 2000), random.randint(-2000, 2000), pygame.image.load("palca.png"))
    stick_list.append(stick)
    stick_list.sort(key=lambda stick: stick.y)
 
player = Player(500, 400, 32, 32)

display_scroll = [0,0]

while True:
    display.fill((25,165,85))
    
    if stick_amount < 31:
        if random.randint(1,2) == 1:
            spawn_stick()
            stick_amount += 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            pygame.quit()
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LSHIFT] and stamina_bar.stamina > 0:
        speed = 6
        stamina_bar.stamina -= 0.5
    else:
        speed = 3
        if stamina_bar.stamina < stamina_bar.max_stamina:
            if keys[pygame.K_a] or keys[pygame.K_d] or keys[pygame.K_w] or keys[pygame.K_s]:
                stamina_bar.stamina += 0.05
            else:
                stamina_bar.stamina += 0.2
    
    if keys[pygame.K_a]:
        display_scroll[0] -= speed
    if keys[pygame.K_d]:
        display_scroll[0] += speed
    if keys[pygame.K_w]:
        display_scroll[1] -= speed
    if keys[pygame.K_s]:
        display_scroll[1] += speed

    pygame.draw.rect(display, (255,255,255), (100-display_scroll[0], 100-display_scroll[1], 16, 16))

    for tree in tree_list:
        tree.draw(display, display_scroll)

    
    for stick in stick_list:
            stick.draw(display, display_scroll)
    
    stamina_bar.draw(display)
    
    player.main(display)

    clock.tick(60)
    pygame.display.update()

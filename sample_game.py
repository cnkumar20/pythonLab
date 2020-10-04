import pygame
pygame.init()
screen = pygame.display.set_mode((600,600))
running = True
pygame.display.set_caption("ko-ko")
icon = pygame.image.load("krishna.png")
pygame.display.set_icon(icon)
#player
player_img = pygame.image.load("pacman.png")
player_x = 300
player_y = 500

def player():
    screen.blit(player_img,(player_x,player_y))
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running= False
        screen.fill((0,0,0))
        player()
        pygame.display.update()

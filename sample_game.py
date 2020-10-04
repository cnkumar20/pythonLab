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

def player(x,y):
    screen.blit(player_img,(x,y))
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.type is pygame.K_a:
                print("A is pressed")
            if event.type is pygame.K_d:
                print("Left is pressed")
                player_x -= 5
            if event.type is pygame.K_a:
                print("Right is pressed")
                player_x += 5
            else:
                print("Nothing pressed"+)
        if event.type == pygame.QUIT:
            running= False
        screen.fill((0,0,0))
        player(player_x,player_y)
        pygame.display.update()

import pygame

    #___________________________________

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


    #___________________________________

def draw_player1():
    player1_image = pygame.image.load("brawler game/Assets/images/players/player1.png").convert_alpha()
    player1_image = pygame.transform.scale(player1_image, (100, 100))
    player1_rect = player1_image.get_rect(midbottom=(SCREEN_WIDTH // 4, SCREEN_HEIGHT - 10))
    player1_lives = 3 # initial number of livesm
    
    screen.blit(player1_image, player1_rect)

    return player1_lives

    #___________________________________

def draw_player2():
    player2_image = pygame.image.load("brawler game/Assets/images/players/player2.png").convert_alpha()
    player2_image = pygame.transform.scale(player2_image, (100, 100))
    player2_rect = player2_image.get_rect(midbottom=(3 * SCREEN_WIDTH // 4, SCREEN_HEIGHT - 10))
    player2_lives = 3

    screen.blit(player2_image, player2_rect)

    return player2_lives

    #___________________________________

def bg_image():
    bg_image = pygame.image.load("brawler game/Assets/images/background/background.jpg").convert_alpha()

    #___________________________________



    
def draw_laser():
    laser_image = pygame.image.load("brawler game/Assets/images/laser.png").convert_alpha()
    laser_image = pygame.transform.scale(laser_image, (100,50))
    laser_rect = laser_image.get_rect(midbottom=(1000,1000))  
    
    if laser == True:
        laser_rect.move_ip(-20,0)

        if laser_rect.colliderect(player1_rect):
            player1_lives -= 1
            laser_rect.midbottom = (1000, 1000)  # reset laser position
            laser = False

    screen.blit(laser_image, laser_rect)
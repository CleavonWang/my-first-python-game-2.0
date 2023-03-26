import pygame

pygame.init()


regenerated = False
laser = False
fire  = False
blade = False
punch = False



# creating game window
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Brawler")

# load background image
bg_image = pygame.image.load("brawler game/Assets/images/background/background.jpg").convert_alpha()


# load player images and resize them  (and laser)
player1_image = pygame.image.load("brawler game/Assets/images/players/player1.png").convert_alpha()
player1_image = pygame.transform.scale(player1_image, (100, 100))
player1_rect = player1_image.get_rect(midbottom=(SCREEN_WIDTH // 4, SCREEN_HEIGHT - 10))
player1_lives = 3 # initial number of livesm

player2_image = pygame.image.load("brawler game/Assets/images/players/player2.png").convert_alpha()
player2_image = pygame.transform.scale(player2_image, (100, 100))
player2_rect = player2_image.get_rect(midbottom=(3 * SCREEN_WIDTH // 4, SCREEN_HEIGHT - 10))
player2_lives = 3

laser_image = pygame.image.load("brawler game/Assets/images/laser.png").convert_alpha()
laser_image = pygame.transform.scale(laser_image, (100,50))
laser_rect = laser_image.get_rect(midbottom=(1000,1000))

fire_image = pygame.image.load("brawler game/Assets/images/fire.png")
fire_image = pygame.transform.scale(fire_image, (200,50))
fire_rect = fire_image.get_rect(midbottom=(-1000,-1000))

blade_image = pygame.image.load("brawler game/Assets/images/blade.png")
blade_image = pygame.transform.scale(blade_image, (50,50))
blade_rect = blade_image.get_rect(midbottom=(-10000,-10000))

punch_image = pygame.image.load("brawler game/Assets/images/punch.png")
punch_image = pygame.transform.scale(punch_image, (200,100))
punch_rect = punch_image.get_rect(midbottom=(1000,-1000))



# function for drawing background
def draw_bg():
    scaled_bg = pygame.transform.scale(bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.blit(scaled_bg, (0, 0))

#drawing lives for players

def draw_player1():
    screen.blit(player1_image, player1_rect)

def draw_player2():
    screen.blit(player2_image, player2_rect)
   
    # display player 1 lives
    font = pygame.font.Font(None, 36)
    lives_text = font.render(f"Lives: {player1_lives}", True, (0, 0, 255))
    screen.blit(lives_text, (SCREEN_WIDTH - 150, 20))

    #display player 2 lives
    lives_text = font.render(f"Lives: {player2_lives}", True, (255,  0, 0))
    screen.blit(lives_text, (SCREEN_WIDTH - 150, 50))

# function for drawing players
def draw_players():
    screen.blit(player1_image, player1_rect)
    screen.blit(player2_image, player2_rect)

#drawing laserbream player2 ability
def draw_laser():
    screen.blit(laser_image, laser_rect)

#drawing fire player 1 ability
def draw_fire():
    screen.blit(fire_image, fire_rect)

#drawing shuriken player 2 ability
def draw_blade():
    screen.blit(blade_image, blade_rect)

#drawing punch player 1 ability
def draw_punch():
    screen.blit(punch_image, punch_rect)


# game loop
run = True
clock = pygame.time.Clock()
while run:
    clock.tick(60)  # limit frame rate to 60 FPS

    # draw background and players
    draw_bg()

    draw_player1()
    
        
    draw_player2()

    draw_laser()
    if laser == True:
        laser_rect.move_ip(-20,0)

        if laser_rect.colliderect(player1_rect):
            player1_lives -= 1
            laser_rect.midbottom = (1000, 1000)  # reset laser position
            laser = False

    draw_fire()
    if fire == True:
        fire_rect.move_ip(20,0)

        if fire_rect.colliderect(player2_rect):
            player2_lives -=1
            fire_rect.midbottom = (-1000, -1000)
            fire = False

    draw_blade()
    if blade == True:
        blade_rect.move_ip(-30,0)

        if blade_rect.colliderect(player1_rect):
            player1_lives -= 1
            blade_rect.midbottom = (30000, 30000)  # reset shuricken position
            blade = False

    draw_punch()
    if punch == True:
        punch_rect.move_ip(30,0)

        if punch_rect.colliderect(player2_rect):
            player2_lives -= 1 
            punch_rect.midbottom = (-1000, -1000)
            punch = False

   
   #player live count
    font = pygame.font.Font(None, 36)
    lives_text = font.render(f"Player One Lives: {player1_lives}", True, (0, 0, 255))
    screen.blit(lives_text, (SCREEN_WIDTH - 1000, 0))



    # check if player 1 needs to regenerate health
    if player1_lives == 0 and not regenerated:
        regenerated = True

        player1_image = pygame.image.load("brawler game/Assets/images/players/player1rage.png").convert_alpha()
        player1_image = pygame.transform.scale(player1_image, (100, 100))
        player1_rect = player1_image.get_rect(midbottom=(SCREEN_WIDTH // 4, SCREEN_HEIGHT - 10))
        player1_lives = 3

        if blade_rect.colliderect(player1_rect):
            player1_lives -= 1

        if laser_rect.colliderect(player1_rect):
            player1_lives -= 1

    if player1_lives == 0:
        pygame.quit()


    font = pygame.font.Font(None, 36)
    lives_text = font.render(f"Player Two Lives: {player2_lives}", True, (225, 0, 0))
    screen.blit(lives_text, (SCREEN_WIDTH - 500, 0))

    if player2_lives == 0:
        player2_lives = 3

        player2_image = pygame.image.load("brawler game/Assets/images/players/player2rage.jpeg").convert_alpha()
        player2_image = pygame.transform.scale(player2_image, (100, 100))
        player2_rect = player2_image.get_rect(midbottom=(3 * SCREEN_WIDTH // 4, SCREEN_HEIGHT - 10))
    

    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


        # handle player 1 input
        if event.type == pygame.KEYDOWN and event.key == pygame.K_a:
            player1_rect.move_ip(-10, 0)
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_d:
            player1_rect.move_ip(10, 0)
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_w:
            player1_rect.move_ip(0, -10)
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_s:
            player1_rect.move_ip(0, 10)
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            fire_rect.midbottom = player1_rect.midbottom
            fire = True
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_m:
            punch_rect.midbottom = player1_rect.midbottom
            punch = True

        # handle player 2 input
        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            player2_rect.move_ip(-10, 0)
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            player2_rect.move_ip(10, 0)
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            player2_rect.move_ip(0, -10)
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            player2_rect.move_ip(0, 10)
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_o:
            laser_rect.midbottom = player2_rect.midbottom
            laser = True
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_p:
            blade_rect.midbottom=player2_rect.midbottom
            blade = True


     

    # update display
    pygame.display.update()

# exit pygame
pygame.quit()
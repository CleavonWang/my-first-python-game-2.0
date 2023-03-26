import pygame
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


def bg_image():
    bg_image = pygame.image.load("brawler game/Assets/images/background/background.jpg").convert_alpha()
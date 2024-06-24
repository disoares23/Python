import pygame

pygame.mixer.init()

bg = pygame.mixer.Sound('bg.mp3')
level_up = pygame.mixer.Sound('level_up.mp3')
game_over = pygame.mixer.Sound('game_over.mp3')
step = pygame.mixer.Sound('step.mp3')

bg.play()
bg.set_volume(0.2)


def play_level_up():
    level_up.play()


def play_game_over():
    game_over.play()


def play_step():
    step.play()

import pygame
pygame.init()
pygame.mixer.music.load('nome_da_musica_na_pasta.mp3')
pygame.mixer.music.play()
pygame.event.wait()
import pygame
import time
pygame.mixer.init()
pygame.mixer.music.load("C:/Users/ahm_2/Downloads/Ceg - First Class (Official Video).mp3")
pygame.mixer.music.play()

while pygame.mixer.music.get_busy() == True:
    continue

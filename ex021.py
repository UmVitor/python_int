#Faça um programa que reproduza o audio de um arquivo MP3
import pygame
pygame.mixer.init()
pygame.mixer.music.load('test.mp3')
pygame.mixer.music.play()
pygame.event.wait()
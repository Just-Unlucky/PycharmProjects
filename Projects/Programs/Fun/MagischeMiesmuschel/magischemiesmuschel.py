import pygame
import random
import sys

go = True

pygame.init()
screen = pygame.display.set_mode([500, 500])
hintergrund = pygame.image.load("hintergrund.jpg")
screen.blit(hintergrund, (0, 0))
pygame.display.set_caption('Magische Miesmuschel')
pygame.display.flip()

font = pygame.font.SysFont(None, 60)


def textSchreiben(ausgabetext, farbe):
    text = font.render(ausgabetext, True, farbe)
    size_rect = text.get_rect(center=(500 / 2, 54))
    screen.blit(text, size_rect)
    pygame.display.flip()


while go:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            x = random.randint(1, 5)
            screen.blit(hintergrund, (0, 0))
            if x == 1:
                textSchreiben("Du hast gelogen!", (255, 255, 255))
            elif x == 2:
                textSchreiben("Das stimmt!", (255, 255, 255))
            elif x == 3:
                textSchreiben("Das ist leider falsch!", (255, 255, 255))
            elif x == 4:
                textSchreiben("Das ist wahr!", (255, 255, 255))
            elif x == 5:
                textSchreiben("Du lügst!", (255, 255, 255))
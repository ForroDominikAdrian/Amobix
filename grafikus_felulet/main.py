import pygame
import sys

pygame.init()

# Ablak mérete
szelesseg = 800
magasagg = 800
sorok = 3
oszlop = 3

screen = pygame.display.set_mode((szelesseg, magasagg))
pygame.display.set_caption("Amőba")

cella_szelesseg = szelesseg // oszlop
cella_magasagg = magasagg // sorok

def draw_grid():
    # függőleges vonalak
    for col in range(1, oszlop):
        x = col * cella_szelesseg
        pygame.draw.line(screen, "white", (x, 0), (x, magasagg), 3)

    # vízszintes vonalak
    for row in range(1, sorok):
        y = row * cella_magasagg
        pygame.draw.line(screen, "white", (0, y), (szelesseg, y), 3)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill("black")
    draw_grid()

    pygame.display.update()
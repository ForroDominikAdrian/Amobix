import pygame
import sys

pygame.init()

# Beállítások
szelesseg = 600
magassag = 600
sorok = 3
oszlop = 3
cella_meret = szelesseg // oszlop

screen = pygame.display.set_mode((szelesseg, magassag))
pygame.display.set_caption("Amőba")

# Színek és tábla (0: üres, 1: X, 2: O)
tabla = [[0 for _ in range(oszlop)] for _ in range(sorok)]
jatekos = 1  # 1-es az X, 2-es az O

def draw_grid():
    for i in range(1, oszlop):
        # Függőleges
        pygame.draw.line(screen, "white", (i * cella_meret, 0), (i * cella_meret, magassag), 3)
        # Vízszintes
        pygame.draw.line(screen, "white", (0, i * cella_meret), (szelesseg, i * cella_meret), 3)

def draw_shapes():
    for r in range(sorok):
        for c in range(oszlop):
            kozep_x = c * cella_meret + cella_meret // 2
            kozep_y = r * cella_meret + cella_meret // 2
            
            if tabla[r][c] == 1: # X kirajzolása
                offset = 50
                pygame.draw.line(screen, "red", (kozep_x - offset, kozep_y - offset), (kozep_x + offset, kozep_y + offset), 5)
                pygame.draw.line(screen, "red", (kozep_x + offset, kozep_y - offset), (kozep_x - offset, kozep_y + offset), 5)
            
            elif tabla[r][c] == 2: # O kirajzolása
                pygame.draw.circle(screen, "blue", (kozep_x, kozep_y), 60, 5)

# Fő ciklus
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Kattintás koordinátáinak átszámítása sorrá és oszloppá
            mouseX, mouseY = event.pos
            katt_sor = mouseY // cella_meret
            katt_oszlop = mouseX // cella_meret
            
            # Ha üres a cella, lerakjuk a jelet
            if tabla[katt_sor][katt_oszlop] == 0:
                tabla[katt_sor][katt_oszlop] = jatekos
                # Játékos váltása (ha 1 volt -> 2 lesz, ha 2 volt -> 1 lesz)
                jatekos = 3 - jatekos

    screen.fill("black")
    draw_grid()
    draw_shapes()
    
    pygame.display.update()
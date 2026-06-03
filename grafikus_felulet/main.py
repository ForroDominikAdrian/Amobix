import pygame
import sys

pygame.init()

# Beállítások
szelesseg = 600
jatek_magassag = 600
info_sav_magassag = 100  # Extra hely alul a pontszámoknak
magassag = jatek_magassag + info_sav_magassag

sorok = 3
oszlop = 3
cella_meret = szelesseg // oszlop

screen = pygame.display.set_mode((szelesseg, magassag))
pygame.display.set_caption("Amőba + Pontszámok")

# Betűtípus a pontszámokhoz
font = pygame.font.SysFont("Arial", 30, bold=True)

# Pontszámok és állapotok
pont_X = 0
pont_O = 0
tabla = [[0 for _ in range(oszlop)] for _ in range(sorok)]
jatekos = 1  # 1-es az X, 2-es az O
jatek_vege = False


def draw_grid():
    for i in range(1, oszlop):
        pygame.draw.line(
            screen, "white", (i * cella_meret, 0), (i * cella_meret, jatek_magassag), 3
        )
        pygame.draw.line(
            screen, "white", (0, i * cella_meret), (szelesseg, i * cella_meret), 3
        )
    pygame.draw.line(
        screen, "gray", (0, jatek_magassag), (szelesseg, jatek_magassag), 5
    )


def draw_shapes():
    for r in range(sorok):
        for c in range(oszlop):
            kozep_x = c * cella_meret + cella_meret // 2
            kozep_y = r * cella_meret + cella_meret // 2

            if tabla[r][c] == 1:
                offset = 50
                pygame.draw.line(
                    screen,
                    "red",
                    (kozep_x - offset, kozep_y - offset),
                    (kozep_x + offset, kozep_y + offset),
                    5,
                )
                pygame.draw.line(
                    screen,
                    "red",
                    (kozep_x + offset, kozep_y - offset),
                    (kozep_x - offset, kozep_y + offset),
                    5,
                )

            elif tabla[r][c] == 2:
                pygame.draw.circle(screen, "yellow", (kozep_x, kozep_y), 60, 5)


def draw_score():
    szoveg_X = font.render(f"X (Piros): {pont_X}", True, "red")
    szoveg_O = font.render(f"O (Sárga): {pont_O}", True, "yellow")

    screen.blit(szoveg_X, (50, jatek_magassag + 30))
    screen.blit(szoveg_O, (szelesseg - 200, jatek_magassag + 30))

    if jatek_vege:
        szoveg_ujra = font.render("Kattints az új körhöz!", True, "yellow")
        screen.blit(
            szoveg_ujra,
            (szelesseg // 2 - szoveg_ujra.get_width() // 2, jatek_magassag + 65),
        )


def ellenoriz_gyoztes(p):

    for i in range(3):
        if (
            tabla[i][0] != 0
            and tabla[i][0] == p
            and tabla[i][1] == p
            and tabla[i][2] == p
        ):
            return True
        if (
            tabla[0][i] != 0
            and tabla[0][i] == p
            and tabla[1][i] == p
            and tabla[2][i] == p
        ):
            return True

    if tabla[1][1] != 0:
        if tabla[0][0] == p and tabla[1][1] == p and tabla[2][2] == p:
            return True
        if tabla[0][2] == p and tabla[1][1] == p and tabla[2][0] == p:
            return True

    return False


def tabla_tele_van():
    for sor in tabla:
        if 0 in sor:
            return False
    return True


def reset_jatek():
    global tabla, jatekos, jatek_vege
    tabla = [[0 for _ in range(oszlop)] for _ in range(sorok)]
    jatekos = 1
    jatek_vege = False


# Fő ciklus
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if jatek_vege:
                reset_jatek()
                continue

            mouseX, mouseY = event.pos
            if mouseY < jatek_magassag:
                katt_sor = mouseY // cella_meret
                katt_oszlop = mouseX // cella_meret

                if tabla[katt_sor][katt_oszlop] == 0:
                    tabla[katt_sor][katt_oszlop] = jatekos

                    if ellenoriz_gyoztes(jatekos):
                        if jatekos == 1:
                            pont_X += 1
                        else:
                            pont_O += 1
                        jatek_vege = True
                    elif tabla_tele_van():
                        jatek_vege = True
                    else:
                        jatekos = 3 - jatekos

    screen.fill("black")
    draw_grid()
    draw_shapes()
    draw_score()

    pygame.display.update()

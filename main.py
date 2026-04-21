import random
import os
import time


# 1. Képernyő törlés a szépség érdekében
def torles():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


# 2. Üres tábla generálása egyszerű ciklusokkal
def ures_tabla_generalas(meret):
    tabla = []
    for i in range(meret):
        sor = []
        for j in range(meret):
            sor.append(" ")
        tabla.append(sor)
    return tabla


jatektabla = []
jatek_mod = ""
nehezseg = 0
bot_jel = ""
player_jel = ""


def tabla_rajzol():
    torles()
    print("--- TIC TAC TOE ---")
    for sor in jatektabla:
        print(" | ".join(sor))
        print("-" * (len(sor) * 4 - 1))


# 3. Nyerés ellenőrzése sima ciklusokkal és if-ekkel
def nyeres_ellenorzes(tabla, jel):
    meret = len(tabla)

    # Sorok ellenőrzése
    for i in range(meret):
        nyert = True
        for j in range(meret):
            if tabla[i][j] != jel:
                nyert = False
        if nyert:
            return True

    # Oszlopok ellenőrzése
    for j in range(meret):
        nyert = True
        for i in range(meret):
            if tabla[i][j] != jel:
                nyert = False
        if nyert:
            return True

    # Keresztbe (átlók) ellenőrzése
    nyert1 = True
    nyert2 = True
    for i in range(meret):
        if tabla[i][i] != jel:
            nyert1 = False
        if tabla[i][meret - 1 - i] != jel:
            nyert2 = False

    if nyert1 or nyert2:
        return True

    return False


# 4. Ellenőrizzük, hogy tele van-e a tábla
def betelt_e():
    for sor in jatektabla:
        for mezo in sor:
            if mezo == " ":
                return False
    return True


# 5. Játékos lépése try-except használatával
def jatekos_lepes(aktualis_jel):
    while True:
        try:
            meret = len(jatektabla)
            print(f"Játékos ({aktualis_jel}) jön!")
            sor = (
                int(
                    input(
                        f"Kérlek add meg hogy melyik sorba szeretnél rakni (1-{meret}): "
                    )
                )
                - 1
            )
            oszlop = (
                int(input(f"Most jöhet hogy hanyadik oszlopba raknál! (1-{meret}): "))
                - 1
            )

            if sor < 0 or sor >= meret or oszlop < 0 or oszlop >= meret:
                raise IndexError(f"Csak 1 és {meret} közötti számot adhatsz meg!")

            if jatektabla[sor][oszlop] != " ":
                raise UserWarning("Ez a mező már foglalt!")

            jatektabla[sor][oszlop] = aktualis_jel
            print(
                f"Sikeresen kiválasztottad a(z) {sor + 1}. sort és {oszlop + 1}. oszlopot!"
            )
            time.sleep(1)
            return sor, oszlop

        except ValueError:
            print("Hiba: Kérlek csak számokat adj meg!")
        except IndexError as e:
            print(f"Hiba: {e}")
        except UserWarning as e:
            print(f"Hiba: {e}")
        except Exception as e:
            print(f"Váratlan hiba történt: {e}")


# 6. A Bot lépésének logikája (üres helyek keresése)
def bot_lepes():
    print("A gép gondolkodik...")
    time.sleep(1.5)

    ures_helyek = []
    for r in range(3):
        for c in range(3):
            if jatektabla[r][c] == " ":
                ures_helyek.append([r, c])

    if nehezseg == 1:
        lepes = random.choice(ures_helyek)
        jatektabla[lepes[0]][lepes[1]] = bot_jel
        return

    # 7. Nehéz mód: a gép megpróbál nyerni vagy védekezni
    for hely in ures_helyek:
        r = hely[0]
        c = hely[1]
        jatektabla[r][c] = bot_jel
        if nyeres_ellenorzes(jatektabla, bot_jel):
            return
        jatektabla[r][c] = " "

    for hely in ures_helyek:
        r = hely[0]
        c = hely[1]
        jatektabla[r][c] = player_jel
        if nyeres_ellenorzes(jatektabla, player_jel):
            jatektabla[r][c] = bot_jel
            return
        jatektabla[r][c] = " "

    sarkok = [[0, 0], [0, 2], [2, 0], [2, 2]]
    szabad_sarkok = []
    for sarok in sarkok:
        if sarok in ures_helyek:
            szabad_sarkok.append(sarok)

    if len(szabad_sarkok) > 0:
        lepes = random.choice(szabad_sarkok)
    else:
        lepes = random.choice(ures_helyek)

    jatektabla[lepes[0]][lepes[1]] = bot_jel


# 8. A bot csalása, ha kikapna vagy döntetlen lenne
def bot_csal(utolso_sor, utolso_oszlop, dontetlen_volt):
    global jatektabla
    print("\n!!! RENDSZERHIBA !!!")
    time.sleep(1)
    if dontetlen_volt:
        print("A Gép nem fogadja el a döntetlent...")
    else:
        print("A Gép megtagadja a vereséget...")
    time.sleep(1.5)

    # 9. Pálya 4x4-re bővítése egyszerű listákkal
    uj_tabla = []
    for sor in jatektabla:
        uj_sor = []
        for mezo in sor:
            uj_sor.append(mezo)
        uj_sor.append(" ")
        uj_tabla.append(uj_sor)

    uj_tabla.append([" ", " ", " ", " "])
    jatektabla = uj_tabla

    if not dontetlen_volt:
        jatektabla[utolso_sor][utolso_oszlop] = " "

    for i in range(4):
        jatektabla[i][i] = bot_jel

    tabla_rajzol()
    if dontetlen_volt:
        print("A GÉP KIBŐVÍTETTE A PÁLYÁT, MERT NEM AKART DÖNTETLENT! NYERT!")
    else:
        print("A GÉP KIBŐVÍTETTE A PÁLYÁT ÉS NYERT! EZ LEHETETLEN!")


def jatek():
    global jatektabla, jatek_mod, nehezseg, bot_jel, player_jel
    jatektabla = ures_tabla_generalas(3)

    torles()

    while True:
        jatek_mod = input("PvP vagy PvE módot akarsz? (pvp/pve): ")
        jatek_mod = jatek_mod.lower()
        if jatek_mod == "pvp" or jatek_mod == "pve":
            break
        print("Hiba: Kérlek csak a 'pvp' vagy 'pve' szavakat használd!")

    if jatek_mod == "pve":
        print(
            "\nNehézségek:\n1. Könnyű (random)\n2. Nehéz (taktikus)\n3. Lehetetlen (csaló bot)"
        )
        while True:
            try:
                nehezseg = int(input("Válassz nehézséget (1-3): "))
                if nehezseg < 1 or nehezseg > 3:
                    raise UserWarning("Csak 1, 2 vagy 3 lehet a nehézség!")
                break
            except ValueError:
                print("Hiba: Kérlek csak számokat adj meg!")
            except UserWarning as e:
                print(f"Hiba: {e}")

    # 10. Random kezdő játékos sorsolása
    if random.randint(1, 2) == 1:
        player_jel = "X"
        if jatek_mod == "pve":
            bot_jel = "O"
        else:
            bot_jel = "X"
        aktualis_jel = "X"
        print("Az 1-es játékos kapta az X-et! Ő kezd.")
    else:
        player_jel = "O"
        bot_jel = "X"
        aktualis_jel = "X"
        print("A 2-es játékos / Gép kapta az X-et! Ő kezd.")

    time.sleep(2)

    while True:
        tabla_rajzol()

        if jatek_mod == "pve" and aktualis_jel == bot_jel:
            bot_lepes()
            if nyeres_ellenorzes(jatektabla, bot_jel):
                tabla_rajzol()
                print("A Gép nyert!")
                break
        else:
            sor, oszlop = jatekos_lepes(aktualis_jel)

            if nyeres_ellenorzes(jatektabla, aktualis_jel):
                if jatek_mod == "pve" and nehezseg == 3 and aktualis_jel == player_jel:
                    bot_csal(sor, oszlop, False)
                    break
                else:
                    tabla_rajzol()
                    print(f"A(z) {aktualis_jel} játékos nyert!")
                    break

        if betelt_e():
            if jatek_mod == "pve" and nehezseg == 3:
                bot_csal(0, 0, True)
                break
            else:
                tabla_rajzol()
                print("Döntetlen!")
                break

        if aktualis_jel == "X":
            aktualis_jel = "O"
        else:
            aktualis_jel = "X"


while True:
    jatek()
    ujra = input("\nAkarsz még egyet játszani? (i/n): ")
    if ujra.lower() != "i":
        break

import random
import os
import time
import platform
jatekmenet = True
i = 0
jatekos1 = "x"
jatekos2 = "o"
nyert = False
dontetlen = False
jatektabla = [    
                [[""][""][""]]
                [[""][""][""]]
                [[""][""][""]]
                                ] #3 dimenziós lista vagizásból 


def elhelyezes(sor,oszlop):
    nyertes = ""
    if i % 2 == 0:
        jatektabla[sor][oszlop][0] = jatekos1
    else:
        jatektabla[sor][oszlop][0] = jatekos2
    
    if jatektabla[0][0][0] == jatektabla[0][1][0] and jatektabla[0][0][0] == jatektabla[0][2][0]:
        if jatektabla[0][0][0] == jatekos1:
            
            return "Az 1-es számú játékos nyert!"
    pass



def jatek():
    while True:
        while True: #Formátum: 1-3 1-3
            while True:
                try:
                    # 1. Bekérjük az adatokat (ha a játékos 1-3 között gondolkodik, kivonunk 1-et a Python indexelés miatt)
                    change = int(input("Kérlek add meg hogy melyik sorba szeretnél rakni (1-3): ")) - 1
                    change2 = int(input("Most jöhet hogy hanyadik oszlopba raknál! (1-3): ")) - 1
                    
                    # 2. Először a határokat ellenőrizzük! (0, 1 vagy 2 lehet az index)
                    if change < 0 or change > 2 or change2 < 0 or change2 > 2:
                        raise IndexError("Csak 1 és 3 közötti számot adhatsz meg!")
                        
                    # 3. Utána ellenőrizzük, hogy szabad-e a hely
                    if jatektabla[change][change2][0] != "":
                        raise UserWarning("Ez a mező már foglalt!")
                        
                    # 4. Ha a kód idáig eljutott, az azt jelenti, hogy nem volt hiba. - Kilépünk a while ciklusból
                    break
                    
                # Hibák elkapása
                except ValueError:
                    # Ezt dobja az int(), ha betűt írnak be szám helyett
                    print("Hiba: Kérlek csak számokat adj meg!")
                except IndexError as e:
                    # Ezt dobjuk mi, vagy a rendszer, ha túllóg a táblán
                    print(f"Hiba: {e}")
                except UserWarning as e:
                    # Ezt dobjuk mi, ha foglalt a mező
                    print(f"Hiba: {e}")
                except Exception as e:
                    # Minden más, váratlan hiba elkapása
                    print(f"Váratlan hiba történt: {e}")
                    
            print(f"Sikeresen kiválasztottad a(z) {change + 1}. sort és {change2 + 1}. oszlopot!")
            elhelyezes(change,change2)
            i+=1
            break #Kilépünk a loop-ból, és ha kell, újraindul a loop. 
        

def jatek2():
    pass

while True:
    if random.randint(1,2) == 1:
        jatekos1="o"
        jatekos2="x"
        print("Az 2-es számú játékos lett az X ! Ő kezdheti a játékot.")
        while jatekmenet:
            jatek()
            
            
            break
    else:
        print("A 1-es számú játékos lett az X ! Ő kezdheti a játékot.")
        while jatekmenet:
            
            
            break
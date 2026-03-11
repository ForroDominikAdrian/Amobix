import random
jatekmenet = True
jatekos1 = "x"
jatekos2 = "o"
jatektabla = [[[""][""][""]]
              [[""][""][""]]
              [[""][""][""]]
                          ]


def jatek1():
    while True: #Formátum: 1-3 1-3
        try:
            change = input("Kérlek add meg hogy melyik sorba szeretnél rakni")
            change2 = input("Most jöhet hogy hanyadik oszlopba raknál!")
            if jatektabla[change][change2] != "":
                
        except:
            
    pass

def jatek2():
    pass

while True:
    if random.randint(1,2) == 1:
        jatekos1="o"
        jatekos2="x"
        print("Az 2-es számú játékos lett az X ! Ő kezdheti a játékot.")
        while jatekmenet:
            
            
            
            break
    else:
        print("A 1-es számú játékos lett az X ! Ő kezdheti a játékot.")
        while jatekmenet:
            jatektabla = [[""][""][""]
                          [""][""][""]
                          [""][""][""]
                          ]
            
            
            break
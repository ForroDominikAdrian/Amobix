# Amobix 

Az **Amobix** egy sokoldalú, a legújabb Python verzióban írt Amőba (Tic-Tac-Toe) játék. A projekt különlegessége a moduláris felépítés: a játékmenet magja és a mesterséges intelligencia egy stabil konzolos alapra épül, amelyből a Pygame-es asztali verzió, illetve a jövőben érkező webes felület is táplálkozik.

## ✨ Játékmódok és Funkciók

A játékban lehetőség van egymás ellen, illetve a gép ellen is játszani (PvP és PvAI). 

**AI Nehézségi szintek:**
* **Kezdő:** Teljesen véletlenszerűen lép.
* **Haladó:** Nem teljesen random, próbál taktikázni.
* **Csaló (Kizárólag a konzolos verzióban!):** Szabálytalan eszközöket is bevet a győzelem érdekében, igazi kihívás!

---

## 👥 A Csapat és a Szerepkörök

A projektet három fő részre osztottuk, hogy a fejlesztés párhuzamosan és hatékonyan folyhasson:

* **Dominik – Alap verzió (Konzol) és AI (Mesterséges Intelligencia)**
    * *Szerepe:* Ő felel a projekt "agyáért". A konzolos verzió tartalmazza a játék logikáját, a szabályrendszert és a nyerési feltételek ellenőrzését. Mivel a többi felület is az ő kódját használja alapként, a stabil és hibamentes játékmenet szempontjából ez a legkritikusabb réteg. Ő fejlesztette a különböző nehézségű AI ellenfeleket is.
* **Attila (Atka) – Pygame grafikus felület**
    * *Szerepe:* Ő felel az asztali, natív játékélményért. A Pygame segítségével a száraz konzolos kód egy interaktív, vizuálisan vonzó és gyorsan reagáló asztali alkalmazássá válik. Az ő munkája hidalja át a szakadékot a háttérlogika és a hagyományos PC-s játékosok között.
* **Milán – Webes felület és kommunikáció (Hamarosan!)**
    * *Szerepe:* Az ő feladata lesz a játék széles körben, telepítés nélkül is elérhetővé tétele. A webes kommunikáció biztosítja majd, hogy a böngészőből érkező lépéseket a Python logika feldolgozza. Jelenleg ez a modul még fejlesztés alatt áll.

---

## 🚀 Telepítés és Futtatás

Mivel a projekt a legújabb Python verzióra épül, futtatásához egy friss Python környezet ajánlott. Külön függőségi (requirements) fájlt nem használunk.

**1. A repository letöltése:**
`git clone https://github.com/ForroDominikAdrian/Amobix.git`
`cd Amobix`

**2. A konzolos verzió indítása:**
> Ez az alapverzió, amely tartalmazza a "Csaló" nehézségi szintet is az AI ellen!
`python main_console.py`
*(Megjegyzés: a main_console.py helyére írd be a konzolos fájl pontos nevét, ha más)*

**3. A Pygame (grafikus) verzió indítása:**
> A futtatáshoz a pygame modul telepítése szükséges lehet (`pip install pygame`).
`python main_pygame.py`
*(Megjegyzés: a main_pygame.py helyére írd be a Pygame indítófájl pontos nevét, ha más)*
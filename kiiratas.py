import random

#kiiratás class ----
class Kiiratas:
    #saját statok ----
    exp = 0
    szint = 0
    Hp = 100
    Mana = 100
    Ero = 1
    Gyorsasag = 1
    penz = 0
    def adatok(self):
        # szint ----
        if self.exp >= 100 and self.exp <= 219:
            self.szint = 1
            self.Hp = 105
            self.Mana = 101
            self.Ero = 2
        elif self.exp >= 220 and self.exp <= 349:
            self.szint = 2
            self.Hp = 107
            self.Mana = 102
            self.Ero = 3
        elif self.exp >= 350 and self.exp <= 489:
            self.szint = 3
            self.Hp = 110
            self.Mana = 103
            self.Ero = 4
        elif self.exp >= 490 and self.exp <= 599:
            self.szint = 4
            self.Hp = 112
            self.Mana = 105
            self.Ero = 6
        elif self.exp >= 600 and self.exp <= 739:
            self.szint = 5
            self.Hp = 118
            self.Mana = 105
            self.Ero = 7
        elif self.exp >= 740 and self.exp <= 889:
            self.szint = 6
            self.Hp = 120
            self.Mana = 106
            self.Ero = 8
            self.Gyorsasag = 2
        elif self.exp >= 890 and self.exp <= 999:
            self.szint = 7
            self.Hp = 124
            self.Mana = 107
            self.Ero = 9
            self.Gyorsasag = 3
        elif self.exp >= 1000 and self.exp <= 1209:
            self.szint = 8
            self.Hp = 127
            self.Mana = 108
            self.Ero = 10
            self.Gyorsasag = 5
        elif self.exp >= 1210 and self.exp <= 1499:
            self.szint = 9
            self.Hp = 130
            self.Mana = 109
            self.Ero = 12
            self.Gyorsasag = 7
        elif self.exp >= 1500:
            self.szint = 10
            self.Hp = 150
            self.Mana = 115
            self.Ero = 15
            self.Gyorsasag = 10
        else:
            self.szint = 0
            self.Hp = 100
            self.Mana = 100
            self.Ero = 1
            self.Gyorsasag = 1

        print(f'\n------------------\n'
              f'Jelenlegi értékeid:\n'
              f'------------------')
        print(f'Tapasztalat pontjaid: {self.exp}')
        print(f'Szinted: {self.szint}')
        print(f'Életerőd: {self.Hp}')
        print(f'Manád: {self.Mana}')
        print(f'Erőd: {self.Ero}')
        print(f'Gyorsaságod: {self.Gyorsasag}')
        print(f'---------')
        print(f'Pénzed: {self.penz}')
        print(f'------------------')

    alvas = 0
    harcok = 1
    vasarlas = 0
    def harc(self):
        # szint < 5
        if self.Mana <= 20:
            alvas_input = input("Kevés a Mana-d, szeretnél aludni? (i/n): ")
            if alvas_input == "i" or alvas_input == "I":
                self.Mana = random.randint(80,90)
                print(f"A manád ennyire nőtt alvás közben: {self.Mana}")
            else:
                print("Hát ez sajnálatos, de muszáj vagy aludni, mivel mana nélkül nem tudsz harcolni.")
        else:
            if int(self.szint) >= 0 and int(self.szint) < 5:
                # szörny statok ----
                szornyelete = random.randint(20, 30)
                szornysebzese = random.randint(self.harcok, self.harcok + 5)
                szornyszint = random.randint(1, 6)
                szornyerteke = random.randint(szornyszint, szornyszint + 5)

                # támadás ----
                print('--------------------------------')
                print(f'A sebzési szinted: {self.Ero}\n'
                      f'--------------------------------')
                print(f'Egy {szornyszint} szintű szöryel harcolsz!')
                print(f'\n HP :{szornyelete} \n Sebzés: {szornysebzese} \n Értéke: {szornyerteke} érme')
                print(f'---------------------------------\n')

                while szornyelete >= 0 or self.Hp >= 0:
                    valasztas = input("Támadás / Védekezés")
                    if valasztas == "tamadas" or valasztas == "támadás" or valasztas == "Támadás" or valasztas == "t":
                        self.Mana -= random.randint(5,15)
                        sebzes = self.Ero + random.randint(1, 2)

                        randomkrit = random.randint(1, 10)
                        kritikus = random.randint(self.Ero + 2, self.Ero + 8)
                        if randomkrit >= 9:
                            szornyelete = szornyelete - kritikus
                            if szornyelete <= 0:
                                print('A szörnynek nem maradt élete!')
                            else:
                                print(
                                    f'A szönyet kritikusan eltaláltad, élete {kritikus} HP-val csökkent. A szörnynek {szornyelete} HP-ja maradt.')
                        else:
                            szornyelete = szornyelete - sebzes
                            if szornyelete <= 0:
                                print('A szörnynek nem maradt élete!')
                            else:
                                print(f'A szöny élete csökkent {sebzes} HP-val. A szörnynek {szornyelete} HP-ja maradt.')
                    else:
                        print('Nem tudom hogy ez mit jelent!')

                    if szornyelete <= 0:
                        print(
                            f'Gratulálok, legyőzted az ellenfelet, nehéz csata volt! \t A jutalmad {szornyerteke * 5} tapasztalat pont és {szornyerteke * 2} arany.')
                        self.penz += szornyerteke * 2
                        self.exp += szornyerteke * 5
                        self.adatok()
                        break
            # 5 < szint > 10
            if int(self.szint) >= 5 and int(self.szint) < 10:
                self.harcok = random.randint(3, 9)
                # szörny statok ----
                szornyelete = random.randint(50, 75)
                szornysebzese = random.randint(self.harcok, self.harcok + 13)
                szornyszint = random.randint(5, 9)
                szornyerteke = random.randint(szornyszint, szornyszint + 12)

                # támadás ----
                print('--------------------------------')
                print(f'A sebzési szinted: {self.Ero}\n'
                      f'--------------------------------')
                print(f'Egy {szornyszint} szintű szöryel harcolsz!')
                print(f'\n HP :{szornyelete} \n Sebzés: {szornysebzese} \n Értéke: {szornyerteke} érme')
                print(f'---------------------------------\n')

                while szornyelete >= 0 or self.Hp >= 0:
                    valasztas = input("Támadás / Védekezés")
                    if valasztas == "tamadas" or valasztas == "támadás" or valasztas == "Támadás" or valasztas == "t":
                        self.Mana -= random.randint(5,15)
                        sebzes = self.Ero + random.randint(1, 2)

                        randomkrit = random.randint(1, 10)
                        kritikus = random.randint(self.Ero + 2, self.Ero + 8)
                        if randomkrit >= 9:
                            szornyelete = szornyelete - kritikus
                            print(
                                f'A szönyet kritikusan eltaláltad, élete {kritikus} HP-val csökkent. A szörnynek {szornyelete} HP-ja maradt.')
                        else:
                            szornyelete = szornyelete - sebzes
                            print(f'A szöny élete csökkent {sebzes} HP-val. A szörnynek {szornyelete} HP-ja maradt.')
                    else:
                        print('Nem tudom hogy ez mit jelent!')

                    if szornyelete == 0 or szornyelete < 0:
                        print(f'Gratulálok, legyőzted az ellenfelet, nehéz csata volt! \t A jutalmad {szornyerteke * 5} tapasztalat pont és {szornyerteke * 2} arany.')
                        self.penz += szornyerteke * 2
                        self.exp += szornyerteke * 5
                        self.adatok()
                        break
            # szint > 10
            if int(self.szint) >= 10:
                self.harcok = random.randint(9, 25)
                # szörny statok ----
                szornyelete = random.randint(100, 160)
                szornysebzese = random.randint(self.harcok, self.harcok + 17)
                szornyszint = random.randint(10, 16)
                szornyerteke = random.randint(szornyszint, szornyszint + 18)

                # támadás ----
                print('--------------------------------')
                print(f'A sebzési szinted: {self.Ero}\n'
                      f'--------------------------------')
                print(f'Egy {szornyszint} szintű szöryel harcolsz!')
                print(f'\n HP :{szornyelete} \n Sebzés: {szornysebzese} \n Értéke: {szornyerteke} érme')
                print(f'---------------------------------\n')

                while szornyelete >= 0 or self.Hp >= 0:
                    valasztas = input("Támadás / Védekezés")
                    if valasztas == "tamadas" or valasztas == "támadás" or valasztas == "Támadás" or valasztas == "t":
                        self.Mana -= random.randint(5,15)
                        sebzes = self.Ero + random.randint(1, 2)

                        randomkrit = random.randint(1, 10)
                        kritikus = random.randint(self.Ero + 2, self.Ero + 8)
                        if randomkrit >= 9:
                            szornyelete = szornyelete - kritikus
                            print(
                                f'A szönyet kritikusan eltaláltad, élete {kritikus} HP-val csökkent. A szörnynek {szornyelete} HP-ja maradt.')
                        else:
                            szornyelete = szornyelete - sebzes
                            print(f'A szöny élete csökkent {sebzes} HP-val. A szörnynek {szornyelete} HP-ja maradt.')
                    else:
                        print('Nem tudom hogy ez mit jelent!')

                    if szornyelete == 0 or szornyelete < 0:
                        print(f'Gratulálok, legyőzted az ellenfelet, nehéz csata volt! \t A jutalmad {szornyerteke * 5} tapasztalat pont és {szornyerteke * 2} arany.')
                        self.penz += szornyerteke * 2
                        self.exp += szornyerteke * 5
                        self.adatok()
                        break
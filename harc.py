#import ----
import kiiratas
import random

stat = kiiratas.Kiiratas()

class HarcKiiratas:
    alvas = 0
    harcok = 1
    vasarlas = 0
    def harc(self):
        print(stat.exp)
        # szint < 5
        if int(stat.szint) >= 0 and int(stat.szint) < 5:
            # szörny statok ----
            szornyelete = random.randint(20, 30)
            szornysebzese = random.randint(self.harcok, self.harcok + 5)
            szornyszint = random.randint(1, 6)
            szornyerteke = random.randint(szornyszint, szornyszint + 5)

            # támadás ----
            print('--------------------------------')
            print(f'A sebzési szinted: {stat.Ero}\n'
                  f'--------------------------------')
            print(f'Egy {szornyszint} szintű szöryel harcolsz!')
            print(f'\n HP :{szornyelete} \n Sebzés: {szornysebzese} \n Értéke: {szornyerteke} érme')
            print(f'---------------------------------\n')

            while szornyelete >= 0 or stat.Hp >= 0:
                valasztas = input("Támadás / Védekezés")
                if valasztas == "tamadas" or valasztas == "támadás" or valasztas == "Támadás" or valasztas == "t":
                    sebzes = stat.Ero + random.randint(1, 2)

                    randomkrit = random.randint(1, 10)
                    kritikus = random.randint(stat.Ero + 2, stat.Ero + 8)
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
                        f'Gratulálok, legyőzted az ellenfelet, nehéz csata volt! \t A jutalmad {szornyerteke * 5} tapasztalat pont')
                    stat.penz += szornyerteke * 2
                    stat.exp += szornyerteke * 5
                    stat.adatok()
                    break
        # 5 < szint > 10
        if int(stat.szint) >= 5 and int(stat.szint) < 10:
            self.harcok = random.randint(3, 9)
            # szörny statok ----
            szornyelete = random.randint(50, 75)
            szornysebzese = random.randint(self.harcok, self.harcok + 13)
            szornyszint = random.randint(5, 9)
            szornyerteke = random.randint(szornyszint, szornyszint + 12)

            # támadás ----
            print('--------------------------------')
            print(f'A sebzési szinted: {stat.Ero}\n'
                  f'--------------------------------')
            print(f'Egy {szornyszint} szintű szöryel harcolsz!')
            print(f'\n HP :{szornyelete} \n Sebzés: {szornysebzese} \n Értéke: {szornyerteke} érme')
            print(f'---------------------------------\n')

            while szornyelete >= 0 or stat.Hp >= 0:
                valasztas = input("Támadás / Védekezés")
                if valasztas == "tamadas" or valasztas == "támadás" or valasztas == "Támadás":
                    sebzes = stat.Ero + random.randint(1, 2)

                    randomkrit = random.randint(1, 10)
                    kritikus = random.randint(stat.Ero + 2, stat.Ero + 8)
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
                    print(f'Gratulálok, legyőzted az ellenfelet, nehéz csata volt! \t A jutalmad {szornyerteke}')
                    stat.penz += szornyerteke
                    break
        # szint > 10
        if int(stat.szint) >= 10:
            self.harcok = random.randint(9, 25)
            # szörny statok ----
            szornyelete = random.randint(100, 160)
            szornysebzese = random.randint(self.harcok, self.harcok + 17)
            szornyszint = random.randint(10, 16)
            szornyerteke = random.randint(szornyszint, szornyszint + 18)

            # támadás ----
            print('--------------------------------')
            print(f'A sebzési szinted: {stat.Ero}\n'
                  f'--------------------------------')
            print(f'Egy {szornyszint} szintű szöryel harcolsz!')
            print(f'\n HP :{szornyelete} \n Sebzés: {szornysebzese} \n Értéke: {szornyerteke} érme')
            print(f'---------------------------------\n')

            while szornyelete >= 0 or stat.Hp >= 0:
                valasztas = input("Támadás / Védekezés")
                if valasztas == "tamadas" or valasztas == "támadás" or valasztas == "Támadás":
                    sebzes = stat.Ero + random.randint(1, 2)

                    randomkrit = random.randint(1, 10)
                    kritikus = random.randint(stat.Ero + 2, stat.Ero + 8)
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
                    print(f'Gratulálok, legyőzted az ellenfelet, nehéz csata volt! \t A jutalmad {szornyerteke}')
                    stat.penz += szornyerteke
                    break
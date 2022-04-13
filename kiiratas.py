#saját statok ----
szint = 0
Hp = 100
Mana = 100
Ero = 1
Gyorsasag = 1
penz = 0

#kiiratás függvény ----
class Kiiratas:
    def adatok(self):
        print(f'\n------------------\n'
              f'Jelenlegi értékeid:\n'
              f'------------------')
        print(f'Szinted: {szint}')
        print(f'Életerőd: {Hp}')
        print(f'Manád: {Mana}')
        print(f'Erőd: {Ero}')
        print(f'Gyorsaságod: {Gyorsasag}')
        print(f'------------------')

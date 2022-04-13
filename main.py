#import ----
import kiiratas
import random
#statok ----
stat = kiiratas.Kiiratas()
alvas = 0
harc = 1
vasarlas = 0

#title ----
print(f'\n------------------------\n'
      f'A HATALMAS HARCOS JÁTÉK\n'
      f'------------------------\n')

#harc ----
bekert = input("Mit szeretnél csinálni? (alvás, harc, fejlesztés)")

if bekert == "harc" or bekert == "harcolas" or bekert == "harcolás":
      if int(kiiratas.szint) >= 0 and int(kiiratas.szint) < 3:

            szornyelete = random.randint(20, 30)
            szornysebzese = random.randint(harc, harc + 5)
            szornyszint = random.randint(1, 6)
            szornyerteke = random.randint(szornyszint, szornyszint + 5)

            print(f'\nA sebzési szinted: {kiiratas.Ero}\n'
                        f'--------------------------------')
            print(f'Egy {szornyszint} szintű szöryel harcolsz!')
            print(f'\n HP :{szornyelete} \n Sebzés: {szornysebzese} \n Értéke: {szornyerteke} érme')
            print(f'---------------------------------\n')

            while szornyelete >= 0 or kiiratas.Hp >= 0:
                  valasztas = input("Támadás / Védekezés")
                  if valasztas == "tamadas" or valasztas == "támadás" or valasztas == "Támadás":
                        sebzes = kiiratas.Ero + random.randint(1,2)

                        randomkrit = random.randint(1,10)
                        kritikus = random.randint(kiiratas.Ero + 2 , kiiratas.Ero + 8)
                        if randomkrit >= 9:
                              szornyelete = szornyelete - kritikus
                              print(f'A szönyet kritikusan eltaláltad, élete {kritikus} HP-val csökkent. A szörnynek {szornyelete} HP-ja maradt.')
                        else:
                              szornyelete = szornyelete - sebzes
                              print(f'A szöny élete csökkent {sebzes} HP-val. A szörnynek {szornyelete} HP-ja maradt.')


                  if szornyelete == 0 or szornyelete < 0:
                        print(f'Gratulálok, legyőzted az ellenfelet, nehéz csata volt! \t A jutalmad {szornyerteke}')
                        kiiratas.penz += szornyerteke
                        break

      if kiiratas.szint > 5 and kiiratas.szint < 10:
            harc = random.randint(4, 14)

      if kiiratas.szint > 10 and kiiratas.szint < 20:
            harc = random.randint(9, 25)

      else:
            bekert = input("Mit szeretnél csinálni? (alvás, harc, vásárlás)")
#harc vége ----
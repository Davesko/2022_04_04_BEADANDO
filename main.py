import kiiratas
import random
stat = kiiratas.Kiiratas()
alvas = 0
harc = 1
vasarlas = 0







print(f'\n------------------------\n'
      f'A HATALMAS HARCOS JÁTÉK\n'
      f'------------------------\n')

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

            while szornyelete <= 0 or kiiratas.Hp <= 0:

                  valasztas = input("Támadás / Védekezés")
                  if valasztas == "tamadas" or bekert == "támadás":

                        kritikus = random.randint(kiiratas.Ero + 2 , kiiratas.Ero + 8)
                        szornyelete = szornyelete - kiiratas.Ero

                        print(f'A szöny élete csökkent {kiiratas.Ero} HP val.')

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






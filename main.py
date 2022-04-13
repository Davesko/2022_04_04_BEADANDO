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

#profil ----
reg = input("Regisztráltál már (y/n):")
while True:
      if reg == "y":
            bejelentkezes = input('Felhasználónév megadása bejelentkezéshez (max 15 karakter):')
            felhaszalok = open('felhasznalok.txt', 'r')
            adatok = felhaszalok.readlines()
            for sorok in adatok:
                  sor = sorok.split(';')
                  if bejelentkezes == sor[0]:
                        #felhasznalo adatai file ----
                        nev = sor[0]
                        #felhasznalo adatai class ----
                        stat.exp = sor[1]
                        stat.szint = sor[2]
                        stat.Hp = sor[3]
                        stat.Mana = sor[4]
                        stat.Ero = sor[5]
                        stat.Gyorsasag = sor[6]
                        stat.penz = sor[7]
                        print(f"Bejelentkeztél: {sor[0]}\n"
                              f"Tapasztalati pontok: {stat.exp}\n"
                              f"Szint: {stat.szint}\n"
                              f"Hp: {stat.Hp}\n"
                              f"Mana: {stat.Mana}\n"
                              f"Ero: {stat.Ero}\n"
                              f"Gyorsaság: {stat.Gyorsasag}\n"
                              f"Pénz: {stat.penz}\n")

      elif reg == "n":
            regisztracio = input('Felhasználónév megadása regisztráláshoz (max 15 karakter):')
            with open('felhasznalok.txt', 'a') as felhaszalok:
                  felhaszalok.write(f"{regisztracio};"
                                    f"{stat.exp};"
                                    f"{stat.szint};"
                                    f"{stat.Hp};"
                                    f"{stat.Mana};"
                                    f"{stat.Ero};"
                                    f"{stat.Gyorsasag};"
                                    f"{stat.penz}\n")
      elif reg != "y" or reg != "n":
            print("Ez nem érthető számomra, írj y-t vagy n-t, vagy írd kicsivel!")

#műveletek ----
bekert = input("Mit szeretnél csinálni? [alvás] | [harc] | [fejlesztés] | [stat]::")
while True:
      #stat ----
      if bekert == "stat":
            stat.adatok()
            bekert = input("Mit szeretnél csinálni? (alvás, harc, fejlesztés, stat)")
            print('--------------------------------')
      #harc ----
      elif bekert == "harc" or bekert == "harcolas" or bekert == "harcolás":
            if int(stat.szint) >= 0 and int(stat.szint) < 3:

                  #szörny statok ----
                  szornyelete = random.randint(20, 30)
                  szornysebzese = random.randint(harc, harc + 5)
                  szornyszint = random.randint(1, 6)
                  szornyerteke = random.randint(szornyszint, szornyszint + 5)

                  #támadás ----
                  print('--------------------------------')
                  print(f'A sebzési szinted: {stat.Ero}\n'
                              f'--------------------------------')
                  print(f'Egy {szornyszint} szintű szöryel harcolsz!')
                  print(f'\n HP :{szornyelete} \n Sebzés: {szornysebzese} \n Értéke: {szornyerteke} érme')
                  print(f'---------------------------------\n')

                  while szornyelete >= 0 or stat.Hp >= 0:
                        valasztas = input("Támadás / Védekezés")
                        if valasztas == "tamadas" or valasztas == "támadás" or valasztas == "Támadás" or valasztas == "t":
                              sebzes = stat.Ero + random.randint(1,2)

                              randomkrit = random.randint(1,10)
                              kritikus = random.randint(stat.Ero + 2 , stat.Ero + 8)
                              if randomkrit >= 9:
                                    szornyelete = szornyelete - kritikus
                                    if szornyelete <= 0:
                                          print('A szörnynek nem maradt élete!')
                                    else:
                                          print(f'A szönyet kritikusan eltaláltad, élete {kritikus} HP-val csökkent. A szörnynek {szornyelete} HP-ja maradt.')
                              else:
                                    szornyelete = szornyelete - sebzes
                                    if szornyelete <= 0:
                                          print('A szörnynek nem maradt élete!')
                                    else:
                                          print(f'A szöny élete csökkent {sebzes} HP-val. A szörnynek {szornyelete} HP-ja maradt.')
                        else:
                            print('Nem tudom hogy ez mit jelent!')


                        if szornyelete <= 0:
                              print(f'Gratulálok, legyőzted az ellenfelet, nehéz csata volt! \t A jutalmad {szornyerteke * 5} tapasztalat pont')
                              stat.penz += szornyerteke * 2
                              stat.exp += szornyerteke * 5
                              stat.adatok()
                              break
            if int(stat.szint) > 5 and int(stat.szint) < 10:
                  harc = random.randint(3, 9)
                  #szörny statok ----
                  szornyelete = random.randint(50, 75)
                  szornysebzese = random.randint(harc, harc + 13)
                  szornyszint = random.randint(5, 9)
                  szornyerteke = random.randint(szornyszint, szornyszint + 12)

                  #támadás ----
                  print('--------------------------------')
                  print(f'A sebzési szinted: {stat.Ero}\n'
                              f'--------------------------------')
                  print(f'Egy {szornyszint} szintű szöryel harcolsz!')
                  print(f'\n HP :{szornyelete} \n Sebzés: {szornysebzese} \n Értéke: {szornyerteke} érme')
                  print(f'---------------------------------\n')

                  while szornyelete >= 0 or stat.Hp >= 0:
                        valasztas = input("Támadás / Védekezés")
                        if valasztas == "tamadas" or valasztas == "támadás" or valasztas == "Támadás":
                              sebzes = stat.Ero + random.randint(1,2)

                              randomkrit = random.randint(1,10)
                              kritikus = random.randint(stat.Ero + 2 , stat.Ero + 8)
                              if randomkrit >= 9:
                                    szornyelete = szornyelete - kritikus
                                    print(f'A szönyet kritikusan eltaláltad, élete {kritikus} HP-val csökkent. A szörnynek {szornyelete} HP-ja maradt.')
                              else:
                                    szornyelete = szornyelete - sebzes
                                    print(f'A szöny élete csökkent {sebzes} HP-val. A szörnynek {szornyelete} HP-ja maradt.')
                        else:
                            print('Nem tudom hogy ez mit jelent!')


                        if szornyelete == 0 or szornyelete < 0:
                              print(f'Gratulálok, legyőzted az ellenfelet, nehéz csata volt! \t A jutalmad {szornyerteke}')
                              stat.penz += szornyerteke
                              break
            if int(stat.szint) > 10:
                  harc = random.randint(9, 25)
                  #szörny statok ----
                  szornyelete = random.randint(100, 160)
                  szornysebzese = random.randint(harc, harc + 17)
                  szornyszint = random.randint(10, 16)
                  szornyerteke = random.randint(szornyszint, szornyszint + 18)

                  #támadás ----
                  print('--------------------------------')
                  print(f'A sebzési szinted: {stat.Ero}\n'
                              f'--------------------------------')
                  print(f'Egy {szornyszint} szintű szöryel harcolsz!')
                  print(f'\n HP :{szornyelete} \n Sebzés: {szornysebzese} \n Értéke: {szornyerteke} érme')
                  print(f'---------------------------------\n')

                  while szornyelete >= 0 or stat.Hp >= 0:
                        valasztas = input("Támadás / Védekezés")
                        if valasztas == "tamadas" or valasztas == "támadás" or valasztas == "Támadás":
                              sebzes = stat.Ero + random.randint(1,2)

                              randomkrit = random.randint(1,10)
                              kritikus = random.randint(stat.Ero + 2 , stat.Ero + 8)
                              if randomkrit >= 9:
                                    szornyelete = szornyelete - kritikus
                                    print(f'A szönyet kritikusan eltaláltad, élete {kritikus} HP-val csökkent. A szörnynek {szornyelete} HP-ja maradt.')
                              else:
                                    szornyelete = szornyelete - sebzes
                                    print(f'A szöny élete csökkent {sebzes} HP-val. A szörnynek {szornyelete} HP-ja maradt.')
                        else:
                            print('Nem tudom hogy ez mit jelent!')


                        if szornyelete == 0 or szornyelete < 0:
                              print(f'Gratulálok, legyőzted az ellenfelet, nehéz csata volt! \t A jutalmad {szornyerteke}')
                              stat.penz += szornyerteke
                              break
            else:
                  bekert = input("Mit szeretnél csinálni? (alvás, harc, vásárlás, stat)")
      #hiba ----
      elif bekert != "stat" and bekert != "harc" and bekert != "harcolas" and bekert != "harcolás":
            print('Nem tudom, hogy ez mit jelent!')
            bekert = input("Mit szeretnél csinálni? (alvás, harc, fejlesztés, stat)")

#harc vége ----
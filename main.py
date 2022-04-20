#import ----
import sys

import kiiratas
import random

bejelentkezve = 0

#statok ----
stat = kiiratas.Kiiratas()

#title ----
print(f'\n------------------------\n'
      f'A HATALMAS HARCOS JÁTÉK\n'
      f'------------------------\n')

# adatok ----
felhaszalok = open('felhasznalok.txt', 'r')
adatok = felhaszalok.readlines()
sor = []
for sorok in adatok:
      sor.append(sorok.strip().split(';'))
#reg / log ----
login = 0
nev = ""
while login < 100:
      reg = input("Regisztráltál már (i/n):")

      if reg == "i" or reg == "I":
            bekeres = input('Felhasználónév megadása bejelentkezéshez (max 15 karakter):')
            for i in sor:
                  if bekeres == i[0]:
                        bejelentkezve = 1
                        #felhasznalo adatai file ----
                        nev = i[0]
                        #felhasznalo adatai class ----
                        stat.exp = int(i[1])
                        stat.penz = int(i[2])
                        print(f"Bejelentkezve, mint {nev}")
                        stat.adatok()
                        login = 100
                        break
            else:
                  print("Nem található ilyen felhasználó")


      elif reg == "n"  or reg == "N":
            bekeres = input('Felhasználónév megadása bejelentkezéshez (max 15 karakter):')
            with open('felhasznalok.txt', 'a') as felhaszalok:
                  felhaszalok.write(f"{bekeres};"
                                    f"{stat.exp};"
                                    f"{stat.penz}\n")
                  felhaszalok.close()
            nev = bekeres
            stat.exp = 0
            stat.penz = 0
            bejelentkezve = 1
            print('-----------------')
            print(f'Regisztrálva és bejelentkezve, mint {nev}')
            break
      else:
            print("Ez nem érthető számomra, írj i-t vagy n-t!")

#main ----
while True:
      if bejelentkezve == 1:
            while True:
                  bekert = input("Mit szeretnél csinálni? [alvás] | [harc] | [fejlesztés] | [stat] | [exit]::")
                  # stat ----
                  if bekert == "stat":
                        stat.adatok()
                        bekert = input("Mit szeretnél csinálni? [alvás] | [harc] | [fejlesztés] | [stat]::")
                        print('--------------------------------')
                  # harc ----
                  elif bekert == "harc" or bekert == "harcolas" or bekert == "harcolás":
                        stat.Mana -= random.randint(5,15)
                        stat.harc()
                  # exit ----
                  elif bekert == "exit":
                        sys.exit()
                        # while True:
                        #       for i in sor:
                        #             if i.index(nev):
                        #                   print(i.index(nev))
                        #       # if nev in i[0]:
                        #       #       print(".--")
                        #       #       # with open('felhasznalok.txt', 'w') as mentes_file:
                        #       #       #       mentes_file.write(f"{nev};"
                        #       #       #                         f"{stat.exp};"
                        #       #       #                         f"{stat.penz}\n")
                        #       #       #       mentes_file.close()
                        #       #       #       sys.exit()
                        #       # else:
                        #       #       print(" ")
                  # hiba ----
                  elif bekert != "stat" and bekert != "harc" and bekert != "harcolas" and bekert != "harcolás" and bekert != "exit":
                        print('Nem tudom, hogy ez mit jelent!')
      break
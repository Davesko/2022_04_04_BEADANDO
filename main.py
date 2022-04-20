#import ----
import kiiratas
import random

bejelentkezve = 0

#statok ----
stat = kiiratas.Kiiratas()

#title ----
print(f'\n------------------------\n'
      f'A HATALMAS HARCOS JÁTÉK\n'
      f'------------------------\n')

#profil ----
reg = input("Regisztráltál már (i/n):")
felhaszalok = open('felhasznalok.txt', 'r')
#reg / log ----
i = 2
x = 2
y = 2
while True:
      if reg == "i" or reg == "I":
            bejelentkezes = input('Felhasználónév megadása bejelentkezéshez (max 15 karakter):')
            adatok = felhaszalok.readlines()
            for sorok in adatok:
                  sor = sorok.split(';')
                  if bejelentkezes == sor[0]:
                        bejelentkezve = 1
                        #felhasznalo adatai file ----
                        nev = sor[0]
                        #felhasznalo adatai class ----
                        stat.exp = int(sor[1])
                        stat.penz = int(sor[2])
                        stat.adatok()
                        break
                  else:
                        print("Nem található ilyen felhasználó")
            break
      elif reg == "n"  or reg == "N":
            regisztracio = input('Felhasználónév megadása regisztráláshoz (max 15 karakter):')
            with open('felhasznalok.txt', 'a') as felhaszalok:
                  felhaszalok.write(f"{regisztracio};"
                                    f"{stat.exp};"
                                    f"{stat.penz}\n")
                  break
      else:
            print("Ez nem érthető számomra, írj i-t vagy n-t!")

while i < 3:
      if bejelentkezve == 1:
            bekert = input("Mit szeretnél csinálni? [alvás] | [harc] | [fejlesztés] | [stat]::")
            while x < 3:
                  # stat ----
                  if bekert == "stat":
                        stat.adatok()
                        bekert = input("Mit szeretnél csinálni? [alvás] | [harc] | [fejlesztés] | [stat]::")
                        print('--------------------------------')
                        x += 1
                  # harc ----
                  elif bekert == "harc" or bekert == "harcolas" or bekert == "harcolás":
                        stat.harc()
                        x += 1
                  # hiba ----
                  elif bekert != "stat" and bekert != "harc" and bekert != "harcolas" and bekert != "harcolás":
                        print('Nem tudom, hogy ez mit jelent!')
                        bekert = input("Mit szeretnél csinálni? [alvás] | [harc] | [fejlesztés] | [stat]::")
                        x = 2
felhaszalok.close()
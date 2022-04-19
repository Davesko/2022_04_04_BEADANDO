#import ----
import kiiratas
import random
import harc

bejelentkezve = 0

#statok ----
stat = kiiratas.Kiiratas()
harcolas = harc.HarcKiiratas()

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
while i < 3:
      if reg == "i":
            bejelentkezes = input('Felhasználónév megadása bejelentkezéshez (max 15 karakter):')
            adatok = felhaszalok.readlines()
            for sorok in adatok:
                  sor = sorok.split(';')
                  while y < 3:
                        if bejelentkezes == sor[0]:
                              bejelentkezve = 1
                              #felhasznalo adatai file ----
                              nev = sor[0]
                              #felhasznalo adatai class ----
                              stat.exp = int(sor[1])
                              stat.szint = sor[2]
                              stat.Hp = sor[3]
                              stat.Mana = sor[4]
                              stat.Ero = sor[5]
                              stat.Gyorsasag = sor[6]
                              stat.penz = sor[7]
                              stat.adatok()
                              y += 1
                        else:
                              print("Nem található ilyen felhasználó")
                              y = 2
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
                  i = 2
      else:
            print("Ez nem érthető számomra, írj i-t vagy n-t, vagy írd kicsivel!")
      if bejelentkezve == 1:
            bekert = input("Mit szeretnél csinálni? [alvás] | [harc] | [fejlesztés] | [stat]::")
            while x < 3:
                  # stat ----
                  if bekert == "stat":
                        stat.adatok()
                        bekert = input("Mit szeretnél csinálni? [alvás] | [harc] | [fejlesztés] | [stat]::")
                        print('--------------------------------')
                        i += 1
                  # harc ----
                  elif bekert == "harc" or bekert == "harcolas" or bekert == "harcolás":
                        print(stat.exp)
                        harcolas.harc()
                        i += 1
                  # hiba ----
                  elif bekert != "stat" and bekert != "harc" and bekert != "harcolas" and bekert != "harcolás":
                        print('Nem tudom, hogy ez mit jelent!')
                        bekert = input("Mit szeretnél csinálni? (alvás, harc, fejlesztés, stat)")
                        x = 2
felhaszalok.close()
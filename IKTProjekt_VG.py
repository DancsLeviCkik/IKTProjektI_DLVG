import random

lista = []

menu = [
    ("A feladat"),
    ("B feladat"),
    ("C feladat"),
    ("D feladat"),
    ("Lista módosítása (hozzáadás, törlés, módosítás)"),
    ("Kilépés!"),
]

menuz=True

for i in range(len(menu)):
    print(f"{i+1}-{menu[i]}")

valasztas = input()

if (valasztas=='1'):
    pass

elif (valasztas=='2'):
    pass

elif (valasztas=='3'):
    pass

elif (valasztas=='4'):
    pass

elif (valasztas=='5'):
    if (not lista):
        print("A lista üres")
    else:
        for szam in lista:
            print(szam,end=", ")
        print(5)

        sorszam=input("Módositani vagy törölni kivánt szám")

        if (sorszam=="" or not sorszam.isnumeric()):
            print("Érvénytelen sorszám")
        else:
            sorsz=int(sorszam)
            if (0<=sorsz<len(lista)):
                muvelet=input("-Módositás, -Törlés")

                if (muvelet=="m"):
                    ertek=int(input("Új érték:"))
                    lista[sorsz]=ertek
                    print("Lista értéke:")
                    for number in (lista):
                        print(szam, end=", ")
                    print()

                elif (muvelet=="t"):
                    lista.pop(sorsz)
                    print("Elem törölve")
                    for number in (lista):
                        print(szam, end=", ")
                    print()
                else:
                    print("Érvénytelen muvelet")
            else:
                print("Érvénytelen sorszám")

elif (valasztas=='6'):
    print()

else:
    print("Érvénytelen választás")

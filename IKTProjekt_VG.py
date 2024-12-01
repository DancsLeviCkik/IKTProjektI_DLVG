import random 

tomb = []
meret = 0 
folytat = True

while folytat:
    print("n\Menü")
    if meret == 0:
        print("1. Tömb feltöltése véletlen számokkal")
        print("2. Tömb feltöltése billentyűzetről")
        print("3. Egy elem hozzáadása")
    else:
        print("1.Tömb kiirása")
        print("2.Tümb úritése")
        print("3.Egy elem hozzáadása")
        print("4.Egy elem módositása")
        print("5.Egy elem törlése")
        print("6.1a feladat")
        print("7.1b feladat")
        print("8.1c feladat")
        print("9.1d feladat")
        print("0.Kilépés")

valasztas = int(input("Válassz egyet!"))

if valasztas == 0:
    folytat == False #A ciklus befelyeződik, ha 0 a válasz
elif valasztas == 1:
    if meret == 0:
        meret = int(input("Hány elemet töltsek fel?"))
        tomb = [random.randint(1,100) for i in range(meret)]
    else:
        print(tomb)
    # Ide kell rakni a többit
else:
    print("Érvénytelen választás")


#Dancs Levente, Virágh Gergely 10.c Python első beadandó

#Dancs Levente, Virágh Gergely 10.c Python első beadandó

import random, math

#menü

t = []
j=0
i=0
mukodes=True

while mukodes==True:
    
    print("")

    print("1 - A feladat")
    print("2 - B feladat")
    print("3 - C feladat")
    print("4 - D feladat")
    print("5 - Tömb módosítása (elem hozzáadása, módosítása, törlése, feltöltés véletlen számokkal)")
    print("6 - Kilépés")

    valasztas = input()

    print("")

    if (valasztas=='1'):
        #1a

        t_abs=[]
        t_abs=[]

        i2=0
        i2=0

        for i2 in range(0,len(t),1):
            if t[i2]<0:
                t_abs.append(abs(t[i2]))
            else:
                t_abs.append(t[i2])
        for i2 in range(0,len(t),1):
            if t[i2]<0:
                t_abs.append(abs(t[i2]))
            else:
                t_abs.append(t[i2])

        i3=0
        lepesek=0
        i3=0
        lepesek=0

        for i3 in range(0,len(t),1):
            lepesek+=t[i3]
        for i3 in range(0,len(t),1):
            lepesek+=t[i3]

        i4=0
        lepesek_abszolut=0
        i4=0
        lepesek_abszolut=0

        for i4 in range(0,len(t),1):
            lepesek_abszolut+=t_abs[i4]
        for i4 in range(0,len(t),1):
            lepesek_abszolut+=t_abs[i4]

        print(f'{round(((lepesek_abszolut-lepesek)/lepesek_abszolut*100),2)} százalékkal ment többet')
        print(f'{round(((lepesek_abszolut-lepesek)/lepesek_abszolut*100),2)} százalékkal ment többet')

    elif (valasztas=='2'):
        #1b
    elif (valasztas=='2'):
        #1b

        t_lepessorozat=[]
        t_lepessorozat=[]

        i5=0    
        i5=0    

        haladas=0
        haladas=0

        for i5 in range(0,len(t),1):
            if t[i5] >= 0:
                haladas+=1
            else:
                t_lepessorozat.append(haladas)
                haladas-=haladas
        for i5 in range(0,len(t),1):
            if t[i5] >= 0:
                haladas+=1
            else:
                t_lepessorozat.append(haladas)
                haladas-=haladas

        i6=0                
        i6=0                

        max=t_lepessorozat[0]
        max=t_lepessorozat[0]

        for i6 in range(len(t_lepessorozat)):
            if max<t_lepessorozat[i6]:
                max=t_lepessorozat[i6]
        for i6 in range(len(t_lepessorozat)):
            if max<t_lepessorozat[i6]:
                max=t_lepessorozat[i6]

        print(max)
        print(max)

    elif (valasztas=='3'):
        #1c
    elif (valasztas=='3'):
        #1c

        t_abs=[]

        i1=0

        for i1 in range(0,len(t),1):
            if t[i1]<0:
                t_abs.append(abs(t[i1]))
            else:
                t_abs.append(t[i1])

        maxlepes=t_abs[0]
        t_abs=[]

        i1=0

        for i1 in range(0,len(t),1):
            if t[i1]<0:
                t_abs.append(abs(t[i1]))
            else:
                t_abs.append(t[i1])

        maxlepes=t_abs[0]

        i7=0
        i7=0

        for i7 in range(len(t_abs)):
            if maxlepes<t_abs[i7]:
                maxlepes=t_abs[i7]
        for i7 in range(len(t_abs)):
            if maxlepes<t_abs[i7]:
                maxlepes=t_abs[i7]

        i8=0
        maxlepes_szam=0
        i8=0
        maxlepes_szam=0

        for i8 in range(len(t_abs)):
            if t_abs[i8]==maxlepes:
                maxlepes_szam+=1
        for i8 in range(len(t_abs)):
            if t_abs[i8]==maxlepes:
                maxlepes_szam+=1

        print(f'{(maxlepes_szam)} db és {maxlepes} láb volt.')
        print(f'{(maxlepes_szam)} db és {maxlepes} láb volt.')


    elif (valasztas=='4'):
        #1d

        i9=0
        t0=[]   

        for i9 in range(len(t)):
            if t[i9]==0:
                t0.append(i9)

        if len(t0)>0:
            print("igen.")
        else:
            print("nem.")  

    elif (valasztas=='5'):
        if len(t)>0:
            print("Tömb értéke: ")
            print(t)
        else:
            print("A tömb üres.")

        muvelet=input("h-Hozzáadás,m-Módositás,t-Törlés,v-Véletlenszámokkal feltöltés: ")
        if (muvelet=="h"):
            elem=int(input("Hozzáadadni kívánt elem: "))
            t.append(elem)
            print("")
            print("Tömb módosított értéke: ")
            print(t)

        elif (muvelet=="m"):
            sorsz=int(input("Módosítani kívánt elem: "))
            ertek=int(input("Új érték: "))
            t[sorsz]=ertek
            print("")
            print("Tömb módosított értéke: ")
            print(t)

        elif (muvelet=="t"):
            sorsz2=int(input("Törölni kívánt elem: "))
            t.pop(sorsz2)
            print("Elem törölve")
            print("")
            print("Tömb módosított értéke: ")
            print(t)

        elif (muvelet=="v"):
            n=int(input("Hozzáadni kívánt véletlen számok mennyisége: "))
            for j in range(0,n,1):
             t.append(random.randint(-10,10))
            print("")
            print("Tömb módosított értéke: ")
            print("Sikeres feltöltés")
            print(t)
            
        else:
            print("Érvénytelen művelet")

    elif (valasztas=='6'):
        mukodes=False

    else:
        print("Érvénytelen választás") 
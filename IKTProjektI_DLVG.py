import random, math

n=int(input())
t=[]

i=0

for i in range(0,n,1):
    t.append(random.randint(-10,10))

#1a

t_abs=[]

i2=0

for i2 in range(0,len(t),1):
    if t[i2]<0:
        t_abs.append(abs(t[i2]))
    else:
        t_abs.append(t[i2])

i3=0
lepesek=0

for i3 in range(0,len(t),1):
    lepesek+=t[i3]

i4=0
lepesek_abszolut=0

for i4 in range(0,len(t),1):
    lepesek_abszolut+=t_abs[i4]

print(f'{round(((lepesek_abszolut-lepesek)/lepesek_abszolut*100),2)} százalékkal ment többet')

#1b

t_lepessorozat=[]

i5=0

haladas=0

for i5 in range(0,len(t),1):
    if t[i5] >= 0:
        haladas+=1
    else:
        t_lepessorozat.append(haladas)
        haladas-=haladas

i6=0                

max=t_lepessorozat[0]

for i6 in range(len(t_lepessorozat)):
    if max<t_lepessorozat[i6]:
        max=t_lepessorozat[i6]

print(max)

#1c

maxlepes=t_lepessorozat[0]

i7=0

for i7 in range(len(t_abs)):
    if maxlepes<t_abs[i7]:
        maxlepes=t_abs[i7]

i8=0
maxlepes_szam=0

for i8 in range(len(t_abs)):
    if t_abs[i8]==maxlepes:
        maxlepes_szam+=1

print(f'{(maxlepes_szam)} db és {maxlepes} láb volt.')

#1d

print("igen." if 0 in t else "nem.")
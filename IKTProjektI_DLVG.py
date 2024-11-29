import random, math

n=int(input())
t=[]

i=0

for i in range(0,n,1):
    t.append(random.randint(-10,10))

#1a

t_abs=[]

i=0

for i in range(0,n,1):
    if t[i]<0:
        t_abs.append(abs(t[i]))
    else:
        t_abs.append(t[i])

i=0
lepesek=0

for i in range(0,n,1):
    lepesek+=t[i]

i=0
lepesek_abszolut=0

for i in range(0,n,1):
    lepesek_abszolut+=t_abs[i]

print(f'{round(((lepesek_abszolut-lepesek)/lepesek_abszolut*100),2)} százalékkal ment többet')

#1b

t_lepessorozat=[]

i=0

haladas=0

for i in range(0,n,1):
    if t[i] >= 0:
        haladas+=1
    else:
        t_lepessorozat.append(haladas)
        haladas-=haladas

i=0                

max=t_lepessorozat[0]

for i in range(len(t_lepessorozat)):
    if max<t_lepessorozat[i]:
        max=t_lepessorozat[i]

print(max)
print(t_lepessorozat)

#1c


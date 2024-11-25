import random, math

n=int(input())
t=[]

i=0

for i in range(0,n,1):
    t.append(random.randint(-10,10))

#1a

t_abs=[]

c=0

for c in range(0,n,1):
    if t[c]<0:
        t_abs.append(abs(t[c]))
    else:
        t_abs.append(t[c])

a=0
lepesek=0

for a in range(0,n,1):
    lepesek+=t[a]

b=0
lepesek_abszolut=0

for b in range(0,n,1):
    lepesek_abszolut+=t_abs[b]

print(round(((lepesek_abszolut-lepesek)/lepesek_abszolut*100),2), "százalékkal ment többet.")
print(lepesek, lepesek_abszolut)
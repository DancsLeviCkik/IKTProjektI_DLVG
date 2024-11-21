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

for a in range(0,n,1):
    a+=t[a]

b=0

for b in range(0,n,1):
    b+=t_abs[b]

print(a/b*10000/100, "százalékkal ment többet.")
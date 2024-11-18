import random, math

n=int(input())
t=[]

i=0

for i in range(0,n,1):
    t.append(random.randint(-10,10))
    i+=1

#1a

t_abs=[]

c=0

for c in range(0,n,1):
    if t[c]<0:
        t_abs.append(abs(i))
    else:
        t_abs.append(i)
    c+=1    

print(t_abs)
#print(t/t_abs*10000/100, "százalékkal ment többet.")
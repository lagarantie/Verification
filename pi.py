import random
count=0.0
n=10000000000
for i in range (0, n):
    a=random.random()
    b=random.random()
    if (a**2+b**2)<1.0:
        count+=1

pi=(count/n)*4
print (pi)

    

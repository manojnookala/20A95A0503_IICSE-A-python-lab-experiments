PROGRAM:
  
import math as m
sum=0
n=2000000
for n in range(2,n+1):
    prime=True
    for i in range(2,int(m.sqrt(n)+1)):
        if n%i==0:
            prime=False
            break
        if prime:
            sum=sum+n
print("sum={}".format(sum))

OUTPUT:
sum=207851932781152

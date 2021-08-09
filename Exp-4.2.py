PROGRAM:
a=0
b=1
sum=0
while a<=4000000:
    if a%2==0:
        sum=sum+a
        a,b=b,a+b
print("Sum of even fibonacci number is",sum)

OUTPUT:
  

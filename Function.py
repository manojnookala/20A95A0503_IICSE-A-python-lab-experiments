def test():
    print ("test()")
    print ("I am Function")
    print ("Hello")
#call to test()
test()#fuction call

#function with parameters
def show(x):
    print("show()")
    print (x)
    print(type(x))

#call the sow()
show("Python")
show(10)
show(10.9999909)
set1={123,457,5678}
show(set1)#show set
list1=["python","Flat","co","Daa","Iot"]
show(list1)
dict1={5:"cse",12:"IT",3:"ece"}
show(dict1)
#tuple
tuple1=(10.4,10.5,340.45)
show(tuple1)


OUPUT:
    test()
I am Function
Hello
show()
Python
<class 'str'>
show()
10
<class 'int'>
show()
10.9999909
<class 'float'>
show()
{457, 123, 5678}
<class 'set'>
show()
['python', 'Flat', 'co', 'Daa', 'Iot']
<class 'list'>
show()
{5: 'cse', 12: 'IT', 3: 'ece'}
<class 'dict'>
show()
(10.4, 10.5, 340.45)
<class 'tuple'>
>>> 

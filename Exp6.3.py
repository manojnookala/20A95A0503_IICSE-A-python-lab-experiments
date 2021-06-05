Sort the two lists
L1=[45,63,23,12,78]
L2=[12,90,72,-1]
Combine L1&L2 as single list and display the elements in the sorted order
#Dislay
L3=[-1,12,12,23,45,63,72,78,90]
Perform sorting on the list.....

Program
l1=[]
l2=[]
n1=int(input("Enter number of elements:"))
for i in range(1,n1+1):
    b=int(input("Enter element:"))
    l1.append(b)
n2=int(input("Enter number of elements:"))
for i in range(1,n2+1):
    d=int(input("Enter element:"))
    l2.append(d)
new=l1+l2
new.sort()
print("Sorted list is:",new)
 #output
Enter number of elements:5
Enter element:45
Enter element:63
Enter element:23
Enter element:12
Enter element:78
Enter number of elements:4
Enter element:12
Enter element:90
Enter element:72
Enter element:-1
Sorted list is: [-1, 12, 12, 23, 45, 63, 72, 78, 90]
>>>

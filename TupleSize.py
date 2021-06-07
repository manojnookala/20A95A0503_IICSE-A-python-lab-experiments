#set creatiom
set1={1,2,3,4,5,6}
print("Element in the set1 is : {}".format(set1))
#set allow duplicates ?
set2={10,20,30,40,40,60}
print("Element in the set2 is : {}".format(set2))
#data type
print("Data type of set1",type(set1))
print("Data type of set2",type(set2))

#min and max element from the set2
min_ele=min(set2)
max_ele=max(set2)
print(" Min is %d and max is %d from the set2"%(min_ele,max_ele))

....
OUTPUT
Element in the set1 is : {1, 2, 3, 4, 5, 6}
Element in the set2 is : {20, 40, 10, 60, 30}
Data type of set1 <class 'set'>
Data type of set2 <class 'set'>
 Min is 10 and max is 60 from the set2
>>> 

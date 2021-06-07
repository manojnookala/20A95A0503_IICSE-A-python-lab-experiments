#Set operations
set1={1,2,3,4,5,10,12,13}
set2={10,11,12,13,14,15,17}
#union-All the element
#return the element
set3=set1.union(set2)
print(set3)
#update
set1.update(set2)
print(set1)
#intersection
set3=set1.intersection_update(set2)
print(set3)
set3=set2.intersection_update(set1)
print(set3)
#difference()
set3=set1.difference(set2)
print(set3)

#difference_update()
set3=set1.difference_update(set2)
print(set3)

#issubset()
set3=set1.issubset(set2)
print(set3)

#issuperset()
set3=set1.issuperset(set2)
print(set3)

...
OUTPUT
{1, 2, 3, 4, 5, 10, 11, 12, 13, 14, 15, 17}
{1, 2, 3, 4, 5, 10, 11, 12, 13, 14, 15, 17}
None
None
set()
None
True
False
>>>


    

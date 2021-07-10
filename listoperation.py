#listoperation
def list_sum(l):
    s=0
    for i in l:
        s+=i
    return s
def list_sort(l):
    l.sort()
    return l
def string_list_conversions(s):
    li = list(s)
    return li

#list access from another module
from listoperation import *
print(list_sum([1,2,3,4,5]))
print(list_sort([9,2,3,4,10]))
print(string_list_conversions("python programming lab"))

OUTPUT:
15
[2, 3, 4, 9, 10]
['p', 'y', 't', 'h', 'o', 'n', ' ', 'p', 'r', 'o', 'g', 'r', 'a', 'm', 'm', 'i', 'n', 'g', ' ', 'l', 'a', 'b']
>>>

dict={1:"cse",2:"it",3:"ece",4:" pet",5:"eee"}
res=dict.keys()
print(res)
dict.pop(5)
print(dict)
dict["new"]="Mech"
print(dict)
res=dict.values()
print(res)

...
OUTPUT
dict_keys([1, 2, 3, 4, 5])
{1: 'cse', 2: 'it', 3: 'ece', 4: ' pet'}
{1: 'cse', 2: 'it', 3: 'ece', 4: ' pet', 'new': 'Mech'}
dict_values(['cse', 'it', 'ece', ' pet', 'Mech'])

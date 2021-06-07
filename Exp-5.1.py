'''
5.1) Implement a python script to count frequency of characters in a given string.
'''
input_str = input('Enter a string: ')

alphabet_count = {}

for character in input_str:
	alphabet_count[character] = alphabet_count.get(character,0) + 1


for key in sorted(alphabet_count.keys()):
	print('Count of {} is {}'.format(key,alphabet_count[key]))
  .....
  
OUTPUT:
Enter a string: Python progamming lab
Count of   is 2
Count of P is 1
Count of a is 2
Count of b is 1
Count of g is 2
Count of h is 1
Count of i is 1
Count of l is 1
Count of m is 2
Count of n is 2
Count of o is 2
Count of p is 1
Count of r is 1
Count of t is 1
Count of y is 1
>>> 

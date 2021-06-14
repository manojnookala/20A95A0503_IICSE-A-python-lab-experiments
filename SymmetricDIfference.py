'''
HackerRank Problem: Symmetric Difference
'''
# Enter your code here. Read input from STDIN. Print output to STDOUT
M = int(input())
mset = set(map(int, input().split()))
N = int(input())
nset = set(map(int, input().split()))
mdef = mset.difference(nset)
ndef = nset.difference(mset)
output = mdef.union(ndef)
for i in sorted(list(output)):
    print(i)
'''
Input:
4
9 5 4 2
4 
12 4 11 2
Output:
5
9
11
12
>>>
'''

#Exception Handling
try:
    print(x)  #Generate Exception
except TypeError:      #Handler error
    print("X variable is not yet declared")

print("I am Normal Statement after exception Handling")



'''
   print(x)  #Generate Exception
NameError: name 'x' is not defined
'''

#Dictionary to store branchcode->name
dict_ds={05:"CSE",12:"IT",03:"ECE",04:"MECH"}
print dict_ds
#type of data structure
print type(dict_ds)
#accessing elements from the dictionary
res=dict_ds[12] #dictionary_name[key]
print "At key 12 the value is {}" .format(res)
#New dictionary
#Key-Unique,value:Repeated
dict_ds1={05:"CSE",05:"CSE-A","Name":"manoj","Fname":"NVVSatyanarayana"}
print dict_ds1
#Modify the values from the dictionary
print "Old value is %s" %dict_ds1["Name"]#dictionary_name[key]
dict_ds1["Name"]="Devi"#dictionary_name[key]=NewValue
print "New value is %s" %dict_ds1["Name"]#manoj
#Add New Keys to dictionary?
#dict_ds1[key]=value
dict_ds1["Department"]="CSE"
print "New Dict After Adding Key"
print dict_ds1
...
OUTPUT:
{4: 'MECH', 3: 'ECE', 12: 'IT', 5: 'CSE'}
<type 'dict'>
At key 12 the value is IT
{5: 'CSE-A', 'Fname': 'manoj', 'Name': 'manoj'}
Old value is manoj
New value is manu
New Dict After Adding Key
{'Department': 'CSE', 5: 'CSE-A', 'Fname': 'manu', 'Name': 'manoj'}
'''

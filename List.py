branch_name=["CSE","IT","ECE","MECH"]
print(branch_name)
print(branch_name[1])
colleges=["AEC","JNTUK","IIT",1,2,3,"KKD",8.8,"SURAMPALEM","KAKINADA"]
print(colleges)
#data tyep of colleges
print("Data Type of colleges is ",type(colleges))
#modifing list-YES
branch_name[3]="PT"
print(branch_name)
#Acces list
for i in branch_name:
    print(i)
    
    
    
Output:
    ['CSE', 'IT', 'ECE', 'MECH']
IT
['AEC', 'JNTUK', 'IIT', 1, 2, 3, 'KKD', 8.8, 'SURAMPALEM', 'KAKINADA']
Data Type of colleges is  <class 'list'>
['CSE', 'IT', 'ECE', 'PT']
CSE
IT
ECE
PT


class Parent:
    def anything(self):
        print('Function defined in parent class!')
        

class Child(Parent):
    def anything(self):
     print('Function defined in child class!')
     
obj = Parent()
obj.anything()
obj2 = Child()
obj2.anything()

OUTPUT:
    Function defined in parent class!
Function defined in child class!

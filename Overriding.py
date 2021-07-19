class Parent:
    def anything(self):
        print('Function defined in parent class!')
        

class Child(Parent):
     # empty class definition
    pass

   
obj2 = Child()
obj2.anything()

OUTPUT:
    Function defined in parent class!

try:
    a=int(raw_input("Enter A:"))
    b=int(raw_input("Enter B:"))
    c=int(raw_input("Enter C:"))
    a=a/b
    print(a)
    print(res)

except TypeError:
    print("Conversion Problem")

    
except NameError:
    print("Vaiable is not yet declared")


except ZeroDivisionError:
    print("Variable Don't perform division with zero")


except:
    pass

OUTPUT:
Enter a7
Enter b0
Enter c8
Dont perform division with zero

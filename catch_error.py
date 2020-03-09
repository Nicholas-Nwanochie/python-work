number = int(input("enter a number: "))
print(number)
# what if you dont type a number


try:
    number = int(input("enter a number: "))
    print(number)
except:
    print("invalid")



try:

    number = int(input("enter a number: "))
    print(number)
except ZeroDivisionError:
    print("Divided by zero")
except ValueError:
    print("invalid")



try:
    
    number = int(input("enter a number: "))
    print(number)
except ZeroDivisionError as err:
    print(err)
except ValueError:
    print("invalid")







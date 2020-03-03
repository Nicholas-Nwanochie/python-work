def say_hi(name, age):
    print("hello user " + name + " you are " + age)
print("top")
say_hi("mike", "30")
print("bottom")

say_hi("nick", "30")

def say_hi(name, age):
    print("hello user " + name + " you are " + str(age))
print("top")
say_hi("mike", 30)
print("bottom")

say_hi("nick", 20)

def addTwo(startingValue):
    endingValue = startingValue + 2
    print('The sum of', startingValue, 'and 2 is:', endingValue)
    say_hi()
addTwo(5)
addTwo(10)

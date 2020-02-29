for name in friends:
    print(name)

" for loop with numbers, last number is not shown"

for index in range(3, 10):
    print(index)
friends = ["jim", "beth", "kevin"]
for index in range(len(friends)):
    print(friends[index])

friends = ["jim", "beth", "kevin"]
for index in range(5):
    if index == 0:
        print("first go")
    else:
       print("not first")

for variable in range(1, 11):
    for inner in range(1, 11):
        sum = variable * inner

        print(variable, "*", inner, "=", sum)
        name ='nick'
print(f'hello {name}')

week= ["week1", "week2","week3", "week4","week5", "week6","week7", "week8"]
day = ["*   monday","*  tuesday","* wednsday","*    thursday","*    friday","*  saturday","*    sunday",]
nada = ["- sleep "" - sleep"]
for variable in week:
    print("")
    print("*", variable, "*")

    for inner in day:
        print("")
        print(inner)

        mystring ="".join(nada)
        for blah in nada:


            print(mystring ,",")


# # lists
#
# list = ['a', 'd', 'r']
#
# print(list)
# list.append("sd")
#
# list2 = ["x", "y", "z"]
# list.extend(list2)
# print(list)
#
# item = list.pop(1)
# print(item)
#
# list.reverse()
# print(list)
#
newlist = [1, 2, 3, ["x", "y", "z"]]
print(newlist[3][2])


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

first_col = [row[2] for row in matrix]

print(first_col)

todos = ["pet the cat", "go to work", "shop for groceries",
         "go home", "feed the cat"]

todos.append("binge watch a show")
todos.append("go to sleep")

count = 0

while count < len(todos):
    print(f"{count}: {todos[count]}")
    count += 1


a = 1, 2, 3, 4, 5
b = 3, 2, 4, 5, 6,
print(a)
print(b)
print(a+b)

todos = ["pet the cat", "go to work",
         "shop for groceries", "go home", "feed the cat"]

del todos[0]  # Remove the first one
print(todos)

del todos[1:3]  # Remove items at index 1 up but not including index 3
print(todos)


list1 = []
entry = input("add items")
print("add items to your list")
while len(entry) > 0:
    list1.append([entry])
    print(list1)
    entry = input("enter in an item you would like to add")
print(list1)

list_a = [1, 2, 3, 4, 5, 6]
while len(list_a) > 0:
    list_a.pop()
    print(list_a)

a = [[2, 4, 6, 8],
     [1, 3, 5, 7],
     [8, 6, 4, 2],
     [7, 5, 3, 1]]

i = 0
j = 0

while i < len(a):
    while j < len(a[i]):
        print(f"{a[i][j]}", end=" ")
        j += 1
    print()
    j = 0
    i += 1

x = [[2, 6], [6, 2], [8, 2], [5, 12]]
print(x[2])
print(x[2][1])


a = [1, 2, 3]
# b = [3, 4, 5]
# c = [(a[0]) * (b[0])]


"Given two lists of numbers of the same length, create a new list by multiplying "
"the pairs of numbers in corresponding positions in the two lists"

num = [1, 2, 3, 4, 5]
num2 = [2, 3, 4, 5, 6]
num3 = []

for i in range(0, len(num)):
    num3.append(num[i] + num2[i])
print(str(num3))

"Calculate the result of adding the two matrices. The number in each position in the resulting" \
    " matrix should be the sum of the numbers in the corresponding addend matrices."
list1 = [[2, 2, 4],
         [3, 5, 8]]
list2 = [[3, 4, 8],
         [4, 9, 5]]
list3 = []

for i in range(len(list1)):
    list4 = []
    print(" ")
    for j in range(len(list1[0])):

        sum1 = list1[i][j] + list2[i][j]
        list4.append(sum1)
        list3.append(list4)
print(list3)


set = [8, 9, 7, 6, 9, 9, 6]


original = [1, 2, 2, 3]
newlist = []

for item in original:
    if item in newlist:
        print("You don't need to add "+str(item)+" again.")
    else:
        newlist.append(item)
        print("Added "+str(item))

print(newlist)

sentence = input('Enter your sentence: ')
for letter in sentence:
    if letter in 'aeiou':
       letter = letter * 5
       sentence += letter
       print(sentence)

dict1 = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5,
         'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10,
         'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15,
         'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20,
         'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26}

dict2 = {0: 'Z', 1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E',
         6: 'F', 7: 'G', 8: 'H', 9: 'I', 10: 'J',
         11: 'K', 12: 'L', 13: 'M', 14: 'N', 15: 'O',
         16: 'P', 17: 'Q', 18: 'R', 19: 'S', 20: 'T',
         21: 'U', 22: 'V', 23: 'W', 24: 'X', 25: 'Y'}

message = "lbh zhfg hayrnea jung lbh unir yrnearq"
decipher = ''
shift = 13
for letter in message:

    if(letter != ' '):

        num = (dict1[letter] - shift + 26) % 26

        decipher += dict2[num]
    else:

        decipher += (' ')
print(decipher)


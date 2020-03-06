z  =0
b1 =1
b2 =2
b3 =4
b4 =8
b5 =16
b6 =32
b7 =64
b8 =128
x = int(input("enter number here between 1 and 255"))
while x <= 255:
    if x >= 1:
        z = x
        print(x)
        break
    else:


     print("try again")


     z = x
print(x)

x = (x - b8)

if x < 0:
    b8 = 0
    x = z
else:
    z = x
    b8 = 1
x = (x - b7)

if x < 0:
    b7 = 0
    x = z
else:
    z = x
    b7 = 1
x = (x - b6)

if x < 0:
    b6 = 0
    x = z
else:
    z = x
    b6 = 1
x = (x - b5)

if x < 0:
    b5 = 0
    x = z
else:
    z = x
    b5 = 1
x = (x - b4)

if x < 0:
    b4 = 0
    x = z
else:
    z = x
    b4 = 1
x = (x - b3)

if x < 0:
    b3 = 0
    x = z
else:
    z = x
    b3 = 1
x = (x - b2)

if x < 0:
    b2 = 0
    x = z
else:
    z = x
    b2 = 1
x = (x - b1)

if x < 0:
    b1 = 0
    x = z
else:
    z = x
    b1 = 1
print( b8, b7, b6, b5, b4, b3, b

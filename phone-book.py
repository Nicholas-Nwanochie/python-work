# phone book code

##############################
import pickle
import os.path
##############################
if os.path.isfile("data.pickle"):
    with open("data.pickle", "rb") as fh:
        phone_book = pickle.load(fh)
##############################
phone_book = [
    {
        "nick nwanochie": '678-123-2299',
        'joe blow': '837-494-1829',
        'john doe': '837-494-1234',
        'donald trump': '837-424-1234'
    }

]
###############################
key = phone_book
###############################

while True:
    print("")
    print("")
    print("")
    print(" Electronic Phone book")
    print("========================")
    print("1. look up entry")
    print("2. set an entry")
    print("3. delete an entry")
    print("4. list all entries")
    print("5. quit")
    print("What do you want to do(1-5)?")
    ###############################
    response = ""
    response = input("Enter in a response please.")
    ###############################
    if response == "1":
        name = input("Enter in name.")
        name = name.lower()
        find = phone_book[0].get(name)

        print(find)

        if phone_book[0].get(name) == None:
            print("Entry does not exist")


    ###############################
    elif response == "2":
        print("Enter in name/number to add.")
        info = input("Enter the name.")
        info2 = input("Enter in the number XXX-XXX-XXXX")
        phone_book[0][info] = info2
        print(key)
    ###############################
    elif response == "3":
        print("Enter in a number(XXX-XXX-XXXX) to get rid of.")
        num = input("Enter a name to get rid of.")
        del phone_book[0][num]
        print(key)
    ###############################
    elif response == "4":
        print("All entries will be listed.")
        print(key)
    ###############################
    elif response == "5":
        print("Good bye.")
        exit()
###################################
with open("data.pickle", "wb") as fh:
    pickle.dump(phone_book, fh)

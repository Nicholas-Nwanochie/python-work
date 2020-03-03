secret_word = "cat"
guess = ""
turn_count = 0
turn_limit = 3
out_of_turns = False

while guess != secret_word and not out_of_turns:
    if turn_count < turn_limit:
        guess = input("enter guess: ")
        turn_count += 1
    else:
        out_of_turns = True

if out_of_turns:
    print("out_of_turns")
else:
    print("good job!")

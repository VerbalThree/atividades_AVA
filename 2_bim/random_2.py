import random

random_number = random.randint(1, 50)
trie = False
tries = 0

while not trie:
    user_guess = int(input("Enter the number you think it is:\n"))

    if user_guess < random_number:
        tries += 1
        print("The secret number is higher.\n")
    elif user_guess > random_number:
        tries += 1
        print("The secret number is lower.\n")
    else:
        print("You are right. You tried ", tries, " times.\n")
        trie = True
    if tries == 5:
        print("The game is over. The secret number was: ", random_number)
        break
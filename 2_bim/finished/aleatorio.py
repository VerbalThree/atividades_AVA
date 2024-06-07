import random

random_num = random.randint(1, 100)

tries = 0
guessed = False


while not guessed:
    user_answer = int(input("Enter a number between 1 and 100\n"))
    tries += 1
    
    if user_answer < random_num:
        print("The secret num is higher.\n")
    elif user_answer > random_num:
        print("The secret number is lower.\n")
    else:
        print("You are correct. You tried ", tries, " times")
        guessed = True        

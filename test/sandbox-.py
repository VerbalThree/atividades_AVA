import random

words = ["apache", "c sharp", "java", "vim", "emacs", "ubuntu", "lisp", "goLang", "c++", "typeScript"]
secret_word = (random.choice(words))

tries = 0
verify = False

while not verify:
    user_answer = input("Enter your guess: ")
    if len(user_answer) != 1:
        print("You entered more than a single word.\n")
    else:
        if user_answer != secret_word[0]:
            print("You're wrong. Try again\n")
            tries += 1
        else:
            print(f"You're right. The secret word was: {secret_word.capitalize()}")
            verify = True
    if tries == 5:
        verify == True
        print(f"You lost. The secret word was: {secret_word.capitalize()}\n")
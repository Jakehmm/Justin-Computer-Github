import random

def hangman():
    print("\n Welcome to Hangman! \n")
    print("_____")
    print("|   |")
    print(f"|   {head}")
    print(f"|  {arm1}{body}{arm2}")
    print(f"|  {leg1} {leg2}")
    print("|____")
    print("|    |___")
    print("|_______ |")
    print(f"\n{display_blanks}")
    

file = open("words.txt", "r")
words = file.read().splitlines()
while True:
    correct_word = random.choice(words)
    display_blanks = "_" * len(correct_word)

    max_tries = 6
    head = " "
    body = " "
    arm1 = " "
    arm2 = " "
    leg1 = " "
    leg2 = " "

    while max_tries > -1 and display_blanks != correct_word:

        hangman()

        letter = ""
        while len(letter) != 1 or letter.isdigit():
            letter = input("\n Guess the correct word : ")

        if letter not in correct_word or letter == "":
            max_tries -= 1
            if max_tries == 5:
                head = "o"
            if max_tries == 4:
                body = "|"
            if max_tries == 3:
                arm1 = "/"
            if max_tries == 2:
                arm2 = "\\"
            if max_tries == 1:
                leg1 = "/"
            if max_tries == 0:
                leg2 = "\\"

        else:
            for i in range(0, len(correct_word)):
                if letter == correct_word[i]:
                    display_blanks = list(display_blanks)
                    display_blanks[i] = letter
                    display_blanks = "".join(display_blanks) 

    print(f"The word was : {correct_word} \n")

    if display_blanks == correct_word:
        print("You won")
    else:
        print("You've lost!")
        
    print("Play again? (y/n)")
    play_again = input("> ").strip().lower()
    if play_again[0] == "y":
        continue
    else:
        break
    
file.close()

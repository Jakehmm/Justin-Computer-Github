

# Create a new game
def new_game():

    guesses = []

    correct_guesses = 0

    # Starting Question
    question_num = 1

    # For each key in the dictionary
    for key in questions:
        print("\n") # Line break
        
        # Print each key
        print(key)

        # Nested for loop, for each list in options starting question -1
        for i in options[question_num-1]:
            print(i)

        # User's guess
        guess = input("Enter (A, B , C or D) \n> ").upper()

        # putting user's guess in the list
        guesses.append(guess)

        # Taking the key of the dictionary and the guess, the question and answer essentially
        correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1
    
    display_score(correct_guesses, guesses)

# Check if answer is correct
def check_answer(answer,guess):
    if answer == guess:
        print("Your correct!")
        return 1
    else:
        print("Wrong!")
        return 0


def display_score(correct_guesses, guesses):
    print(f"Results : \n> {correct_guesses }")
    for i in guesses:
        print(i, end = " ")

    score = int(correct_guesses/len(questions)*100)
    print("Your score is: " + str(score) + "%")

def play_again():
    response = input("Do you want to play again?: (y/n)").lower()

    if response == "yes":
        return True
    else:
        return False

questions = {
    "Who created Python?: ": "A",
    "What year was Python created?: ": "B",
    "Python is tributed to which comedy group?: ": "C",
    "Is the Earth round?: ": "A"
}

options = [["A. Guido van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Lord Bezos"],
            ["A. 1989", "B. 1991" , "C. 2000" , "D. 2016 "],
            ["A. Lonely Island", "B. Smosh" , "C. Monty Python" , "D. SNL"],
            ["A. True", "B. False", "C. sometimes", "D. What''s Earth?"]]


new_game()

while play_again():
    new_game()


print("Bye!")
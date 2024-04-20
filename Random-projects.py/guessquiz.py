def play_game():
    question_num = 1
    correct_guesses = 0 
    got_correct = 0


    for key in questions:
        print("--------------------------------")
        print(key)
        for i in options[question_num-1]:
            print(i)
        
        guess = input("What's your answer?: ")

        correct_guesses = check_answer(questions.get(key),guess)

        got_correct += correct_guesses
        question_num += 1

        display_score(got_correct)

def check_answer(answer,guess):
    if answer == guess:
        print("You've got it!")
        return 1
    else:
        print("Wrong!")
        return 0 

def display_score(correct_answers):
    print(f"You've got : {correct_answers} answers right!")

def play_again():
    ask = input("Do you want to play again?: (y/n) ")

    if ask == "y":
        return True
    else:
        return False


questions = { "Who is the president of Russia?:" : "A",
              "Who created Python?:" : "B",
              "The Rock's name:" : "C",
              "John Cena's favorite food?:" : "A",
}


options = [["A. Vladmir Putin" , "B. 毛泽东 ( Mao Ze Dong )" , "C. Xi Jin Ping" , "D. God"],
           ["A. Guido van Rossum", "B. Elon Musk", "C. Mark Zugbert", "D. Lord Bezos"],
           ["A. China", "B. Dwayne Johnson ", "C. Big Sus", "D. Your dad"],
           ["A. Bing Chilling ", "B. China ", "C. Lao Gan Ma " , "D. Hotpot"]]


play_game()

while play_again():
    play_game()

print("Sayonara")
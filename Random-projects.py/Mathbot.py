import random
import time
Operators = [ '+', '-', '/', '*' , '**']
min_integers = 5
max_integers = 20


def AskUser():
    user_input = input("Do you want to start? (Y / N) : ")
    if user_input[0].upper() == 'Y':
        start_game = True
    elif user_input[0].upper() == 'N':
        start_game = False

    if start_game == True:
        ask_user_time = input('''Type the amount of seconds you want to have: ( 1-60 )
> ''')
        print(f'''Alrighty, you have: {ask_user_time} seconds!''')
    else:
        print('Goodbye')

def printQuestions(amount_of_q):
    print(f'''You have {amount_of_q} questions. You have 20 seconds to get ready''')
    for seconds in range(20,0,-1):
        print(seconds)
        time.sleep(1)
    print("Here we go!")
    
    left = random.randint(min_integers)
    right = random.randint(max_integers)
    operand = random.choice(Operators)

    expr = str(left) + operand + str(right)
    answer = eval(expr)

    for i in range(amount_of_q):
        



while True:
    AskUser() 
    print("\n") # Line break
    amount_of_questions = int(input('''How many questions do you want?:
> '''))
    printQuestions(amount_of_questions)


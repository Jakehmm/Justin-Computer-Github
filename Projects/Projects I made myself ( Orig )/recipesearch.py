import random

def rules():
    print('''
Welcome to Recipe Search! 

Here's three dishes you can make! 

- Homemade Gravlax 
- Risotto alla Milanese 
- Sichuan Dumplings ''' "\n")


def main():
    print("\n") # Line Break
    print(""" *You've been transported to the Chef's Kitchen*
 
- Choose one of the three dishes to make """)
    
    dish_choices = [ "1 : Homemade Gravlax" , "2 : Risotto alla Milanese" , "3 : Sichuan Dumplings" ]
    
    for i in dish_choices:
        print(i)

    print("\n") # Line break

    user_input_dish = input("Enter the number of the dish : ")

    if user_input_dish == "1":
        return "Homemade Gravlax"
    elif user_input_dish == "2":
        return "Risotto alla Milanese"
    elif user_input_dish == "3":
        return "Sichuan Dumplings"
    else:
        return False
    

def Homemade_Gravlax():

    user_input = input("Your task is to make the 'Homemade Gravlax' , are you ready? (y / n) \n> ")
    while user_input == "":
        user_input = input("Your task is to make the 'Homemade Gravlax' , are you ready? (y / n) \n> ")
    
    if user_input in ["n" , "no"]:
        print("Goodbye, choose another dish")
        main()
    
    if user_input in ["y" , "ye" , "yes"]:

        print("----------------------------------------------------- \nAlrighty, these are the ingredients you need to make 'Homemade Gravlax' \nIngredients : Salmon fillets, Butter, Garlic, Lemon Juice, Salted Butter ", "\n")
        input("----------------------------------------------------- \n*Grabbing ingredients......* , ENTER to continue " "\n")
        print("System : It looks like we're missing a 'Salmon Fillet', you'll need to go to the seaside to catch it.", "\n")
        input("----------------------------------------------------- \n*Transporting to seaside....* ENTER to continue" "\n")
        print("Fisherman : 'How'dy? , I'm the best fisher in the world, I'll help support you on catching the 'Salmon Fillet' ")

        seaside = ['Salmon Fillet' , 'junk' , 'socks', 'bread']
        fisherman_words = ['Try a bit harder' , "Don't give up!" , "Almost there!"]

        ask_to_fish = input("Start fishing? (y / n)? \n> ")
        print("\n")
        if ask_to_fish in ["y" , "ye" , "yes"]:
            fishing = random.choice(seaside)
            while fishing != seaside[0]:
                print(f"You've got : {fishing}...' ", "\n" , "Fisherman : " + str(random.choice(fisherman_words)))
                print("\n") # Line break
                ask_again = input("Continue fishing?  (y/n) \n> ")
                print("\n") # Line break
                if ask_again in ["y" , "ye" , "yes"]:
                    fishing = random.choice(seaside)
                if fishing == seaside[0]:
                    print("You've got: 'Salmon' Fillet! \n *Transporting back to Chef's Kitchen* ")
        print("--------------------------------------------------")
        recipe = {"Homemade Gravlax" : ["salmon fillet", "butter" ,  "garlic", "lemon juice", "salted butter"]}
        print("\n")


        print("Ingredients : Salmon fillet, Butter, Garlic, Lemon Juice, Salted Butter" "\n")

        ingredients_list = []
        print("To start cooking, input the ingredients one by one...")
        ingredient_1 = input("Ingredient 1:  ").lower()
        print("--------------------------------------------------")
        ingredient_2 = input("Ingredient 2:  ").lower()
        print("--------------------------------------------------")
        ingredient_3 = input("Ingredient 3:  ").lower()
        print("--------------------------------------------------")
        ingredient_4 = input("Ingredient 4:  ").lower()
        print("--------------------------------------------------")
        ingredient_5 = input("Ingredient 5:  ").lower()

        ingredients_list.append(ingredient_1)
        ingredients_list.append(ingredient_2)
        ingredients_list.append(ingredient_3)
        ingredients_list.append(ingredient_4)
        ingredients_list.append(ingredient_5)

        for key,value in recipe.items():
            if ingredients_list == value:
                print("\n")
                print(f"You've successfully cooked an {key}")
                return key

        

def Risotto_alla_Milanese():
    user_input = input("Your task is to make the 'Risotto alla Milanese' , are you ready? (y / n) \n> ")
    while user_input == "":
        user_input = input("Your task is to make the 'Risotto alla Milanese' , are you ready? (y / n) \n> ")
    
    if user_input in ["n" , "no"]:
        print("Goodbye, choose another dish")
        main()
    
    if user_input in ["y" , "ye" , "yes"]:
        print("\n") # Line break
        print("Alrighty, these are the ingredients you need to make 'Risotto alla Milanese' \nIngredients : Rice, Unsalted Butter, Ground Pepper, Onion ")
        print("\n") # Line break
        input("*Grabbing ingredients......* , ENTER to continue ")

        print("\n") # Line break
        print("System : It looks like we're missing 'rice' , you'll need to go to the farm to get some.")

def Sichuan_Dumplings():
    user_input = input("Your task is to make the 'Sichuan Dumplings' , are you ready? (y / n) \n> ")
    while user_input == "":
        user_input = input("Your task is to make the 'Sichuan Dumplings' , are you ready? (y / n) \n> ")
    
    if user_input in ["n" , "no"]:
        print("Goodbye, choose another dish")
        main()
    
    if user_input in ["y" , "ye" , "yes"]:
        print("\n") # Line break
        print("Alrighty, these are the ingredients you need to make 'Sichuan Dumplings' \nIngredients : Napa cabbage, Ground Pork, Soy Sauce, Wonton / Gyoza wrappers ")
        print("\n") # Line break
        input("*Grabbing ingredients......* , ENTER to continue ")
        print("\n") # Line break
        print("System : It looks like we're missing some 'Gyoza wrappers' , you'll need to make to buy them.")

while True:
    rules()
    input("> Continue? ")
    print("---------------------------------------------")
    name_dish = main()

    if name_dish == "Homemade Gravlax":
        value = Homemade_Gravlax()
        if value == "Homemade Gravlax":
            break

    if name_dish == "Risotto alla Milanese":
        Risotto_alla_Milanese()

    if name_dish == "Sichuan Dumplings":
        Sichuan_Dumplings()

    if name_dish == False:
        print("Choose a dish...")
    

   
    



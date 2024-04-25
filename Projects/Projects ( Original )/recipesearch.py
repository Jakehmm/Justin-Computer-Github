import random

def rules():
    print('''
Welcome to Recipe Search! 

Here's a dish you can make

- Homemade Gravlax 
 ''' "\n")


def main():
    print("\n") # Line Break
    print(""" *You've been transported to the Chef's Kitchen*
 """)
    print("\n")
    
    dish_choices = [ "1 : Homemade Gravlax" ]
    
    for i in dish_choices:
        print(i)

    print("\n") # Line break

    user_input_dish = input("Enter the number of the dish : ")

    if user_input_dish == "1":
        return "Homemade Gravlax"
    else:
        return False
    

def Homemade_Gravlax():
    print("\n" "Welcome to Stage 1 : Easy" "\n")
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


        ask_to_fish = input("Start fishing? (y / n)? \n> ")
        fishing_Homemade_Gravlax(ask_to_fish)
        print("\n")
        
        print("--------------------------------------------------")
                    
def fishing_Homemade_Gravlax(answer):
    seaside = ['Salmon Fillet' , 'junk' , 'socks', 'bread']
    fisherman_words = ['Try a bit harder' , "Don't give up!" , "Almost there!"]    
    if answer in ["y" , "ye" , "yes"]:
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
                    

def cooking_Homemade_Gravlax():
            
            recipe = {"Homemade Gravlax" : ["salmon fillet", "butter" ,  "garlic", "lemon juice", "salted butter"]}
            print("\n")
            print("Ingredients : Salmon fillet, Butter, Garlic, Lemon Juice, Salted Butter" "\n")

            ingredients_list = []
            print("To start cooking, input the ingredients one by one...")
            print("--------------------------------------------------")
            ingredient_1 = input("Ingredient 1:  ").lower().strip()
            print("--------------------------------------------------")
            ingredient_2 = input("Ingredient 2:  ").lower().strip()
            print("--------------------------------------------------")
            ingredient_3 = input("Ingredient 3:  ").lower().strip()
            print("--------------------------------------------------")
            ingredient_4 = input("Ingredient 4:  ").lower().strip()
            print("--------------------------------------------------")
            ingredient_5 = input("Ingredient 5:  ").lower().strip()

            ingredients_list.append(ingredient_1)
            ingredients_list.append(ingredient_2)
            ingredients_list.append(ingredient_3)
            ingredients_list.append(ingredient_4)
            ingredients_list.append(ingredient_5)

            cook_again = ["Success" , "Fail"]
            fail_cook = ["You messed up!" , "You might be missing an ingredient?" , "Try again!" , "No worries" , "Your almost there!"]

            for key,value in recipe.items():
                    if ingredients_list == value:
                        cook = random.choice(cook_again)
                        while cook != "Success":
                            print("\n")
                            print(f"Chef : {random.choice(fail_cook)}" "\n")
                            ask_user_input = input("Try again? (y/n) \n> ")
                            if ask_user_input == "y":
                                cook = random.choice(cook_again)
                            elif ask_user_input == "n":
                                print("You've failed!")
                        if cook == "Success":
                            print("\n") # Line Break
                            print(f"You've successfully cooked an {key}")
                            return True

            while ingredients_list != recipe.values:
                ingredients_list.clear()
                print("\n")
                print("There was something wrong with your ingredients, please enter them again...")
                print("--------------------------------------------------")
                ingredient_1 = input("Ingredient 1:  ").lower().strip()
                print("--------------------------------------------------")
                ingredient_2 = input("Ingredient 2:  ").lower().strip()
                print("--------------------------------------------------")
                ingredient_3 = input("Ingredient 3:  ").lower().strip()
                print("--------------------------------------------------")
                ingredient_4 = input("Ingredient 4:  ").lower().strip()
                print("--------------------------------------------------")
                ingredient_5 = input("Ingredient 5:  ").lower().strip()
                ingredients_list.append(ingredient_1)
                ingredients_list.append(ingredient_2)
                ingredients_list.append(ingredient_3)
                ingredients_list.append(ingredient_4)
                ingredients_list.append(ingredient_5)

                cook_again = ["Success" , "Fail"]
                fail_cook = ["You messed up!" , "You might be missing an ingredient?" , "Try again!" , "No worries" , "Your almost there!"]

                for key,value in recipe.items():
                    if ingredients_list == value:
                        cook = random.choice(cook_again)
                        while cook != "Success":
                            print("\n")
                            print(f"Chef : {random.choice(fail_cook)}" "\n")
                            ask_user_input = input("Try again? (y/n) \n> ")
                            if ask_user_input == "y":
                                cook = random.choice(cook_again)
                            elif ask_user_input == "n":
                                print("You've failed!")
                        if cook == "Success":
                            print("\n") # Line Break
                            print(f"You've successfully cooked an {key}")
                            return True


while True:
    rules()
    input("> Continue? ")
    print("---------------------------------------------")
    name_dish = main()

    if name_dish == "Homemade Gravlax":
        Homemade_Gravlax()
        success = cooking_Homemade_Gravlax()
        if success: break

    if name_dish == False:
        print("Choose a dish...")
    

   
    



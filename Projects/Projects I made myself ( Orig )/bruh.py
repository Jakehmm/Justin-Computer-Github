import random
recipe = {"Homemade Gravlax" : ["salmon fillet", "butter" ,  "garlic", "lemon juice", "salted butter"]}
print("\n")


print("Ingredients : Salmon fillet, Butter, Garlic, Lemon Juice, Salted Butter" "\n")

ingredients_list = []
print("To start cooking, input the ingredients one by one...")
print("--------------------------------------------------")
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


while ingredients_list != recipe.values:
    ingredients_list.clear()
    print("\n")
    print("There was something wrong with your ingredients, please enter them again...")
    print("--------------------------------------------------")
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


    cook_again = ["Success" , "Fail"]

    for key,value in recipe.items():
            if ingredients_list == value:
                cook = random.choice(cook_again)
                while cook != "Success":
                    print("\n" "*The cook was unsuccessful!*" "\n")
                    ask_user_input = input("Try again? (y/n) \n> ")
                    if ask_user_input == "y":
                        cook = random.choice(cook_again)
                    elif ask_user_input == "n":
                        print("You've failed!")
                if cook == "Success":
                    print("\n") # Line Break
                    print(f"You've successfully cooked an {key}")
                    print(ingredients_list)
                    
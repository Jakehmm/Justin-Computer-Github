# The main idea is to count all the occurring characters in a string. If you have a string like aba, then the result should be {'a': 2, 'b': 1}.

# What if the string is empty? Then the result should be empty object literal, {}.

def count(s):
    # We're going to create a dictionary
    my_dict = {}
    

    # We're going to loop through each character first
    for character in s:
        
        # Make an if-else statement
        if character in my_dict:
            my_dict[character] = my_dict[character] + 1
        else:
            my_dict[character] = 1
    
    return my_dict

  


user_input = input("Input string here: ")
print(count(user_input) )

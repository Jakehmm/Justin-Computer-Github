# Takes argument "word"
def validate_word(word):
    # Makes a dictonary
    my_dict = {}
    
    # Makes a set
    my_set = set()

    # Make a loop that goes through each character
    for character in word.lower():

        # Don't have any character in my_dict, else + add, then go again
        if character in my_dict:
            my_dict[character] = my_dict[character] + 1
        else:
            my_dict[character] = 1
        print(my_dict)

    for val in my_dict.values():
        my_set.add(val)
    
    return len(my_set) == 1

print(validate_word(""))
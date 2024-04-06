# Longest word

def find_long(l):
    # Split the string into a list of words
    word_list = l.split()

    # Initialize length with negative infinity
    length = float("-inf")
    
    # Iterate through each word in the list
    for word in word_list:
        # If the length of the current word is greater than the current maximum length
        if len(word) > length:
            # Update the maximum length
            length = len(word)
    
    # Return the length of the longest word
    return length



print(find_long("Jamaican beer"))

'''
# Shortest word
def find_short(s):

    # Make words into list
    list = s.split()

    # Length = positive infinity int
    length = float("inf")
    for word in list:
        if(len(word)) < length:
            length = len(word)
    return length
    



print(find_short(input("Input a bunch of strings: ")))
'''
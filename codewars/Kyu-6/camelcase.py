def camel_case(s):

    # Create a new empty string
    newstring = ''

    # Loop through each character
    for characters in s:
    
    # If each character equal to small letter
        if characters == characters.lower():

    # Newstring + characters
            newstring += characters
         

    # If characters arent lower then make them into characters            
        else:
            newstring += characters

    # Capitalize first letter
    x = newstring.title()

    # Replace Spaces
    return x.replace(" ", "")


print(camel_case(input("Input text: ")))

'''
def camel_case(string):
    return string.title().replace(" ", "")
'''

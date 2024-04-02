vowels = ["a" , "e" , "i" , "o" , "u"]
text = input("Input a string without vowel: ")
newstring = ''


for characters in text:
    if characters.lower() not in vowels:
        newstring += characters
    else:
        print(newstring)

print(newstring) 

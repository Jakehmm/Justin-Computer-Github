'''
Write a function that takes an array of words and smashes them together into a sentence and returns the sentence.
You can ignore any need to sanitize words or add punctuation, but you should add spaces between each word. 
Be careful, there shouldn't be a space at the beginning or the end of the sentence!
'''

def smashing(words):
    return " ".join(words)


list_of_words = ['Johny', 'Yes', 'Papa']
print(smashing(list_of_words))


def smash(words):
    
    # Create a new variable with blank
    sentence = ''

    # Loop through each word
    for word in words:

        # If word in list
        if word in words:

            # Add
            sentence += word + " "
        else:
            sentence = sentence
    return sentence.strip()


list = ['hello', 'world', 'this', 'is', 'great']

print(smash(list))
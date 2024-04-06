

def to_camel_case(text):
    if text == '':
        return ''
    firstletter = text[0]
    text = text.replace("-" , " ").replace("_", " ")
    print(text)
    
    text = text.title()
    text = text.replace(" ", "")
    return firstletter + text[1:]


user_input = input("Input text: ")
print(to_camel_case(user_input))
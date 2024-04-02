text = input("camelCase: ")

newtext = ""
for letter in text:
    if letter == letter.upper():
        newtext += "_" + letter.lower()
    else:
        newtext += letter

print(f"snake_case: {newtext}")

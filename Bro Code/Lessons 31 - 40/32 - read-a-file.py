try:
    with open('C:\\Users\\Justin Wu\\OneDrive\\Desktop\\test.txt.txt') as file:
        print(file.read())
except FileNotFoundError as e:
    print(e)
    print("That file was not found :(")


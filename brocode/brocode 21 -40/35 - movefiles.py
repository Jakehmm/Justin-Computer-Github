import os

source = "new"
destination = "C:\\Users\\Justin Wu\\OneDrive\\Desktop"

try:
    if os.path.exists(destination):
        print("There is already a file there!")
    else:
        os.replace(source,destination)
        print(source+ "was moved")
except FileNotFoundError as e:
    print(e)
    print(source +" was not found")
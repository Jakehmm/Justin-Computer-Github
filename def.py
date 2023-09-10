#Define
# it will treat every line of code
# underneath this one as the meaning
# of this new function, hello
#Tab to indent 4 times auto

def hellomaster(to="world"):
    print("Hello Master,", to)

hellomaster()
name = input("What's your name? ")
hellomaster(name)

###########################
def main():
        name = input("What's your name ")
        hello(name)

def hello(to="world"):
      print("hello,", to)
    

main()
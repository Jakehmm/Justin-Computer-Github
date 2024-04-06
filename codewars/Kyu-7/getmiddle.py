def get_middle(s):
    length = len(s)
    if length % 2 == 0:
        return s[length//2 -1] + s[length//2]
    else:
        return s[length//2 -1]


print(get_middle(input("Input a string: ")))
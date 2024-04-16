# nested loops = The "inner loop" will finish all of its
# iterations before finishing on iteration of the "outer loop"

rows = int(input("How many rows?: "))
columns = int(input("How many columns?: "))
symbol = input("Enter a symbol to use: ")

for i in range(rows): # outer
    for j in range(columns): # inner
        print(symbol, end = "")
    print()
for r in range(7):
    for c in range(5):
        if r == 0 and c in {1,2,3,4,5,6}:
            print('#', end=" ")
        elif r in {0,1,2} and c in {1,2,3,4,5,6}:
            print('#', end=" ")
        elif r == 6:
            print('#', end= " ")
        else:
            print(' ', end=" ")
    print()


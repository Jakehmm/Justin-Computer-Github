
def get_sum(x,y):
    # We have to make x smaller, or else the range won't work
    if x > y:
        x, y = y, x
    new_num = 0
    for num in range(x,y+1):
        new_num += num
    return new_num


# Counting down
x = 10
y = 1

for num in range(x,y,-2):
    print(num)
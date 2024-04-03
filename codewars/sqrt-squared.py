import math
def find_next_square(sq):
# check whether value is 0 or not
    if sq > 0:
# Make value squareroot
        n = math.sqrt(sq)
# If value is an int : complete the function
        if n.is_integer():
            return int(n + 1)**2
        else:
            return -1

print(find_next_square(5))
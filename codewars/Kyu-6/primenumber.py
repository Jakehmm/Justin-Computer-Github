# Prime return True
# Not prime return False

def is_prime(num):
    
    is_prime = True

    if num > 0:
        for divisor in range(2,num):
            if num % divisor == 0:
                is_prime = False
                break
    if is_prime:
        return True
    else:
        return False
    

print(is_prime())

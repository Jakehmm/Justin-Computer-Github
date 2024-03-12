EXPECTED_BAKE_TIME = 40
def bake_time_remaining(elapsed_bake_time):
    return EXPECTED_BAKE_TIME - elapsed_bake_time

print(bake_time_remaining(30))

def preparation_time_in_minutes(number_of_layers):
    return number_of_layers * 2

print(preparation_time_in_minutes(2))


def elapsed_time_in_minutes(preparation_time_in_minutes, elapsed_bake_time):
    return preparation_time_in_minutes + elapsed_bake_time 
print(elapsed_time_in_minutes(3,20))


EXPECTED_BAKE_TIME = 40
def bake_time_remaining(elapsed_bake_time):
   
    return EXPECTED_BAKE_TIME - elapsed_bake_time
    
    
print(f"Bake time remaining:{bake_time_remaining(30)} minutes")
    
def preparation_time_in_minutes(number_of_layers):
    return number_of_layers *2

print(f"Preparing time: {preparation_time_in_minutes(2)} minutes")

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
   
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
    
print(f"Final cooking time: {elapsed_time_in_minutes(3,20)} minutes")
    
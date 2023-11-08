user_input = input("Enter 'true' or 'false': ")

# Convert user input to a boolean value
if user_input.lower() == 'true':
    result = True
elif user_input.lower() == 'false':
    result = False
else:
    print("Invalid input. Please enter 'true' or 'false.")
    result = None  # You can set the result to None or handle the error differently

print("The result is:", result)

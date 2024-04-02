# Variable
amount_due = 50

# Loop until amount_due is less than 0
while amount_due > 0:
    # Print the amount due
    print(f"Amount Due: {amount_due}")

    # Ask user to insert coin
    coin_amount = int(input("Insert coin:"))

    # Check if coin is 25, 10 or 5 cents
    if coin_amount in [25,10,5]:
        # Subtract value from amount_due
        amount_due -= coin_amount
    else:
        print("Choose these 3 [ 25 , 10 , 5 ]")

# Calculate change_owed
change_owed = abs(amount_due)

# Print the result
print(f"Change Owed: {change_owed}")

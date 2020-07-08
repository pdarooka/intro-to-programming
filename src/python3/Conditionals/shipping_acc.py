# Conditionals: Shipping Accounts Program

# Welcome message
print("Welcome!")

usernames = ['jsmith', 'pdar', 'naruto', 'uzumaki', 'sasuke']

username_input = input("Username: ")

if username_input.lower() in usernames:
    print(f"Welcome, {username_input}!")
    print("Current Shipping Prices are as follows:")
    print("Shipping orders 0 to 100:\t$5.10 each")
    print("Shipping orders 100 to 500:\t$5.00 each")
    print("Shipping orders 500 to 1000:\t$4.95 each")
    print("Shipping orders over 1000:\t$4.80 each")

    num_to_order = int(input("\nHow many items would you like to ship: "))

    if num_to_order < 100:
        print(
            f"To ship {num_to_order} items, it will cost you ${round(num_to_order*5.10,2)} at $5.10 per item.")
    elif num_to_order < 500:
        print(
            f"To ship {num_to_order} items, it will cost you ${round(num_to_order*5.00,2)} at $5.00 per item.")
    elif num_to_order < 1000:
        print(
            f"To ship {num_to_order} items, it will cost you ${round(num_to_order*4.95,2)} at $4.95 per item.")
    elif num_to_order > 1000:
        print(
            f"To ship {num_to_order} items, it will cost you ${round(num_to_order*4.80,2)} at $4.80 per item.")
    else:
        print("Invalid input")

    if input("Would you like to place this order? (y/n)\n") == 'y':
        print(f"Okay! Shipping your {num_to_order} items")
    else:
        print(f"Okay! Cancelling your order.")

else:
    print("Sorry, you seem to not have an account with us!")

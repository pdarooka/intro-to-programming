# Lists: Different Types of Lists
import datetime as dt

# Initializing the food list
to_buy = ["Meat", "Cheese"]

# Welcome Message
print("Welcome!")

# Initializing and printing current date and time
time = dt.datetime.now()
month = str(time.month)
day = str(time.day)
hour = str(time.hour)
minute = str(time.minute)

print(f"Current time is {day}/{month} {hour}:{minute}")

# Recap of grocery list
print(f"\nHere is your current grocery listwith {len(to_buy)} items:\n{to_buy}\n")

# Get user input
to_buy.append(input("What else do you want to buy?\n").title())

print(f"\nHere is your updated grocery list with {len(to_buy)} items:\n{to_buy}\n")

# Sorting the grocery list
to_buy.sort()
print(f"\nHere is your sorted grocery list with {len(to_buy)} items:\n{to_buy}\n")

# Updates grocery list
print(f"\nCurrent grocery list: {len(to_buy)} items")
to_buy.remove(input("What did you just buy?\n").title())

print(f"\nCurrent grocery list: {len(to_buy)} items")
to_buy.remove(input("What did you just buy?\n").title())

to_buy[0] = (input(f"\nSorry, {to_buy[0]} is currently out of stock.\nWould you like to buy something else?\n").title())
print(f"\nFinal grocery list has {len(to_buy)} item(s) left\n{to_buy}")

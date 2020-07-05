# Lists: Favourite Teacher

# Welcome message
print("Welcome!")

# Initialise fav_teachers with user input
fav_teachers = []
fav_teachers.append(input("Enter the name of your favourite teacher:\n").title())
fav_teachers.append(input("Enter the name of your favourite teacher:\n").title())
fav_teachers.append(input("Enter the name of your favourite teacher:\n").title())

# Prints the list
print(f"\nYour favourite teachers are {fav_teachers}\n")
print(f"Your favourite teachers in alphabetical order are {sorted(fav_teachers)}\n")
print(f"Your favourite teachers in reverse alphabetical order are {sorted(fav_teachers, reverse=True)}\n")
print(f"Your two most favourite teachers are {fav_teachers[0]} and {fav_teachers[1]}\n")
print(f"Your least favourite teacher is {fav_teachers[2]}\n")
print(f"You have {len(fav_teachers)} favourite teachers\n")

# Simulation
tmp = fav_teachers.pop(0)
fav_teachers.insert(0, input(f"Oops, {tmp} is no longer your first favorite teacher. Who is your new favorite teacher:\n").title())

print(f"\nYour favourite teachers are {fav_teachers}\n")
print(f"Your favourite teachers in alphabetical order are {sorted(fav_teachers)}\n")
print(f"Your favourite teachers in reverse alphabetical order are {sorted(fav_teachers, reverse=True)}\n")
print(f"Your two most favourite teachers are {fav_teachers[0]} and {fav_teachers[1]}\n")
print(f"Your least favourite teacher is {fav_teachers[2]}\n")
print(f"You have {len(fav_teachers)} favourite teachers\n")

dislike = input("\nYou've decided you no longer like a teacher. Which teacher would you like to remove from you list:\n").title()
fav_teachers.remove(dislike)

print(f"\nYour favourite teachers are {fav_teachers}\n")
print(f"Your favourite teachers in alphabetical order are {sorted(fav_teachers)}\n")
print(f"Your favourite teachers in reverse alphabetical order are {sorted(fav_teachers, reverse=True)}\n")
print(f"Your two most favourite teachers are {fav_teachers[0]} and {fav_teachers[1]}\n")
print(f"Your least favourite teacher is {fav_teachers[1]}\n")
print(f"You have {len(fav_teachers)} favourite teachers\n")

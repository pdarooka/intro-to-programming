# Lists: Different Types of Lists

# Defining all the lists
num_strings = ["15", "100", "55", "42"]
num_ints = [15, 100, 55, 42]
num_floats = [1.5, 1.00, 5.5, 4.2]
num_lists = [[1,2,3], [4,5,6], [7,8,9]]

# Prints summary of all the lists created above
print(f"The variable num_strings is a {type(num_strings)}")
print(f"It contains the elements {num_strings}")
print(f"The element {num_strings[0]} is a {type(num_strings[0])}")

print(f"\nThe variable num_ints is a {type(num_ints)}")
print(f"It contains the elements {num_ints}")
print(f"The element {num_ints[0]} is a {type(num_ints[0])}")

print(f"\nThe variable num_floats is a {type(num_floats)}")
print(f"It contains the elements {num_floats}")
print(f"The element {num_floats[0]} is a {type(num_floats[0])}")

print(f"\nThe variable num_lists is a {type(num_lists)}")
print(f"It contains the elements {num_lists}")
print(f"The element {num_lists[0]} is a {type(num_lists[0])}")

# Sorting the Lists
print("\nNow sorting num_strings and num_ints...")

num_strings.sort()
print(f"num_strings now contains the elements {num_strings}")

num_ints.sort()
print(f"num_ints now contains the elements {num_ints}")

# Message
print("\nStrings are sorted alphabetically while integers are sorted numerically!")

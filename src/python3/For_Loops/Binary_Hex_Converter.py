# For Loops: Binary to Hexadecimal Converter

# Welcome message
print("Welcome!")

# Gets user input
num_queries = int(
    input("How many values would you like to convert from binary to hexadecimal?\n"))
decimal = list(range(1, num_queries+1))
binary = [bin(x) for x in decimal]
hexadecimal = [hex(x) for x in decimal]

low_slice = int(input("What decimal number would you like to start at:\n"))
hi_slice = int(input("What decimal number would you like to stop at:\n"))

# Prints the lists
print(f"Decimal values from {low_slice} to {hi_slice}")
for y in decimal[low_slice:hi_slice+1]:
    print(str(y))

print(f"Binary values from {low_slice} to {hi_slice}")
for y in binary[low_slice:hi_slice+1]:
    print(str(y))

print(f"Hexadecimal values from {low_slice} to {hi_slice}")
for y in hexadecimal[low_slice:hi_slice+1]:
    print(str(y))

input(f"Press Enter to see all values from 1 to {num_queries}.\n")
print("Decimal----Binary----Hexadecimal\n----------------------------------------------------------")

# Prints all values
for d, b, h in zip(decimal, binary, hexadecimal):
    print(str(d) + "----" + str(b) + "----" + str(h))

# While loops: Even/Odd Sorter

# Welcome message
print("Welcome!")

flag = True

# Even/Odd Sorting
while flag:
    num = input("Enter numbers separated by a comma: ").strip().replace(' ', '')

    num_list = num.split(',')

    even = []
    odd = []

    for i in num_list:
        if int(i) % 2 == 0:
            even.append(int(i))
        else:
            odd.append(int(i))

    print("Summary:")
    for i in num_list:
        if int(i) in even:
            print(f"{i} is EVEN!")
        if int(i) in odd:
            print(f"{i} is ODD!")

    choice = input(
        "Would you like to continue the program? (y/n)\n").lower().strip()
    if choice == 'n':
        flag = False
        print("Thank you! Goodbye!")

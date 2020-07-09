# Dictionaries: Database Administrator

# Welcome message
print("Welcome!")

log_on_information = {
    'admin00': 'administrator',
    'admin01': 'administrator',
    'admin02': 'administrator',
    'admin03': 'administrator',
    'admin04': 'administrator'
        }

# Input for username
usr = input("Username: ")

# Checks password and processes the output
if usr in log_on_information.keys():
    pwd = input("Password: ")

    if pwd == log_on_information[usr]:
        if usr == 'admin00':
            for k, v in log_on_information.items():
                print(f"\tUsername: {k}\tPassword: {v}")
        else:
            change = input("Would you like to update your password? (y/n)").lower()
            if change == 'y':
                new_pwd = input("\tEnter New Password: ")
                if new_pwd.__len__() < 8:
                    print("Not a valid password. Goodbye!")
                else:
                    log_on_information[usr] = new_pwd
            else:
                print("Goodbye!")
else:
    print("You do not have an account with us. Goodbye!")


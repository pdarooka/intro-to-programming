# Lists: Basketball Roster

# Welcome Message
print("Welcome!")

roster = []

# Gets user input
roster.append(input("Who is your point guard?\n").title())
roster.append(input("Who is your shooting guard?\n").title())
roster.append(input("Who is your small forward?\n").title())
roster.append(input("Who is your power forward?\n").title())
roster.append(input("Who is your center?\n").title())

# Prints starting Roster
print("\n\tYour starting 5 for the upcoming basketball season")
print("\t\tPoint Guard:\t\t" + roster[0])
print("\t\tShooting Guard:\t\t" + roster[1])
print("\t\tSmall Forward:\t\t" + roster[2])
print("\t\tPower Forward:\t\t" + roster[3])
print("\t\tCenter:\t\t\t" + roster[4])

# Injury simulation
injured_player = roster.pop(2)
print(f"{injured_player} is, unfortunately, injured.\nYour current roster has {len(roster)} players.")

roster.insert(2, input("Who do you want to take the injured player's spot?\n").title())

# Prints updated roster
print("\n\tYour starting 5 for the upcoming basketball season")
print("\t\tPoint Guard:\t\t" + roster[0])
print("\t\tShooting Guard:\t\t" + roster[1])
print("\t\tSmall Forward:\t\t" + roster[2])
print("\t\tPower Forward:\t\t" + roster[3])
print("\t\tCenter:\t\t\t" + roster[4])

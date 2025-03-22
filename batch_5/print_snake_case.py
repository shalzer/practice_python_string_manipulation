# Prog10: Create a program that ask the user to input their fullname in incorrect casing. Print the input in snake case.

#Ask user to enter full name in incorrect casing
#Print it in snake case

name = input("Enter your full name in incorrect casing: ")
print(name.title().replace(" ", "_"))
# Prog09: Create a program that ask the user to input their fullname in incorrect casing. Print the input in pascal case.

#Ask user to entr their full name in incorrect casing
#Print full name in pascal case

name = input("Enter your full name: ")
print(name.title().replace(" ", ""))
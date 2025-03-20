#Prog01: Create a program that ask the user to input their fullname with several space characters at the beginning. Print the input without the spaces in the beginning.

#Ask the user to enter their full name with extra space at beginning
#Print their full name without space

name = input("Enter your full name with space at the front: ")
NAME = name.strip()
print(NAME)
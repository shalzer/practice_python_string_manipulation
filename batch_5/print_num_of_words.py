#Prog07: Create a program that ask the user to input a complete statement. Print the number of words in the input.

#Ask user to put a complete statement
#Print number of words entered

statement = input("Enter a statement: ")
print(len(statement.split()))
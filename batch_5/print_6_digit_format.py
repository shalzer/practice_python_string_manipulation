#Prog02: Create a program that ask the user to input a number (0-1000). Print the number in 6 digit format. Add zeros at the beginning to complete the 6 digit.

#Ask user to enter a number from 0-1000
#Using f-string, change the format of entered number into 6-digit format adding zeros to complete it.
#print the number in correct format

num = int(input("Enter a number (0-1000): "))
six_digit_num = f"{num:06}"
print(six_digit_num)
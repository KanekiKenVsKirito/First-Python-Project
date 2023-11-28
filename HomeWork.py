
#! 1. Character Input
#*   Create a program that asks the user to enter their name and their age.

# your_name = input("Enter your name: ")
# your_age = input("Enter your age: ")
# print(f'Name: {your_name}')
# print(f'Age: {your_age}')

#? =================================================================================================================

#! 2. Odd Or Even
#*    Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.

enter_number = int(input("Enter a number: "))
if enter_number%2 == 0:
    print(f"It's a EVEN number: {enter_number}")
else:
    print(f"It's a Odd number: {enter_number}")
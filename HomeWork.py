
#! 1. Character Input
#*   Create a program that asks the user to enter their name and their age.

# your_name = input("Enter your name: ")
# your_age = input("Enter your age: ")
# print(f'Name: {your_name}')
# print(f'Age: {your_age}')

#? =================================================================================================================

#! 2. Odd Or Even
#*    Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.

# enter_number = int(input("Enter a number: "))
# if enter_number%2 == 0:
#     print(f"It's a EVEN number: {enter_number}")
# else:
#     print(f"It's a Odd number: {enter_number}")

#? =================================================================================================================

#! 3. List Less Than Ten
#*    Take a list, say for example this one:
#*    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#*    and write a program that prints out all the elements of the list that are less than 5.

# a = [1, 1, 2, 3, 5, 8, 13, 4, 21, 34, 55, 89]
# for i in a:
#     if i < 5:
#         print(i)

#? =================================================================================================================

#! 4. Divisors
#*    Create a program that asks the user for a number and then prints out a list of all the divisors of that number.

num = int(input("Number: "))

number = []

for i in range(1, num + 1):
    if num % i == 0:
        number.append(i)
print(f"The number: {num}, and divisors: {number}")
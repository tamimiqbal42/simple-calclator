print("Welcome to simple calculator project ")
print("Select the operation you wish to perform:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

option = int(input("Please choose an option : "))

if option == 1:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    result = num1 + num2
    print("The result is:", result)
elif option == 2:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    result = num1 - num2
    print("The result is:", result)
elif option == 3:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    result = num1 * num2
    print("The result is:", result)
elif option == 4:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    if num2 != 0:
        result = num1 / num2
        print("The result is:", result)
    else:
        print("Division by zero is not allowed.")
else:
    print("Invalid input. Please select a valid option.")
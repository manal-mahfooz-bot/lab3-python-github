#Function for addition
def addition(a, b):
    return a + b

#Function for subtraction
def subtraction(a, b):
    return a - b

#Function for multiplication
def multiplication(a, b):
    return a * b

#Function for division
def division(a, b):
    #Check if the second number is zero
    if b == 0:
        return "Error: Cannot divide by zero."

    return a / b

#Function to check whether a number is even or odd
def even_odd(number):
    #If the remainder after division by 2 is zero
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

#Function to calculate percentage
def percentage(part, whole):
    #The whole number cannot be zero
    if whole == 0:
        return "Error: The second number cannot be zero."

    return (part / whole) * 100

#The loop allows the user to perform multiple calculations
while True:

    #Display the calculator menu
    print("\nPYTHON CALCULATOR")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Check Even/Odd")
    print("6. Calculate Percentage")
    print("7. Exit")

    #Take the user's menu choice
    choice = input("Enter your choice (1-7): ")

    #Exit the program
    if choice == "7":
        print("Thank you for using the calculator!")
        break

    #Addition
    elif choice == "1":
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        result = addition(num1, num2)
        print("Result:", result)

    #Subtraction
    elif choice == "2":
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        result = subtraction(num1, num2)
        print("Result:", result)

    # Multiplication
    elif choice == "3":
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        result = multiplication(num1, num2)
        print("Result:", result)

    #Division
    elif choice == "4":
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        result = division(num1, num2)
        print("Result:", result)

    #Check whether a number is even or odd
    elif choice == "5":
        num = int(input("Enter a whole number: "))

        result = even_odd(num)
        print("The number is", result)

    #Calculate percentage
    elif choice == "6":
        num1 = float(input("Enter the number whose percentage you want: "))
        num2 = float(input("Enter the total number: "))

        result = percentage(num1, num2)
        print("Percentage:", result, "%")

    #Handle an invalid menu choice
    else:
        print("Invalid choice. Please enter a number from 1 to 7.")
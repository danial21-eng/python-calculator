import math

def advanced_calculator():
    print("Welcome to the Advanced Python Calculator!")
    while True:
        print("\nPlease choose an operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Exponentiation (^)")
        print("6. Modulus (%)")
        print("7. Square Root (√)")
        print("8. Exit")
        
        choice = input("Enter your choice (1-8): ")

        if choice == '8':
            print("Exiting the calculator. Goodbye!")
            break

        if choice in ['1', '2', '3', '4', '5', '6']:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input! Please enter numeric values.")
                continue

            if choice == '1':
                result = num1 + num2
                operator = '+'
            elif choice == '2':
                result = num1 - num2
                operator = '-'
            elif choice == '3':
                result = num1 * num2
                operator = '*'
            elif choice == '4':
                if num2 == 0:
                    print("Error! Cannot divide by zero.")
                    continue
                result = num1 / num2
                operator = '/'
            elif choice == '5':
                result = num1 ** num2
                operator = '^'
            elif choice == '6':
                if num2 == 0:
                    print("Error! Cannot modulus by zero.")
                    continue
                result = num1 % num2
                operator = '%'

            print(f"\nResult: {num1} {operator} {num2} = {result}")

        elif choice == '7':

            try:
                num = float(input("Enter the number: "))
            except ValueError:
                print("Invalid input , please enter numeric value ")
                continue
            if num < 0:
                print("Error , cannot compute square root in negative number you nigger")
                continue
            result = math.sqrt(num)
            print (f"\nResult: /{num} = {result}")

        else:
            print("Invalid choice, Please select valid option")

if __name__ == "__main__":
    advanced_calculator()
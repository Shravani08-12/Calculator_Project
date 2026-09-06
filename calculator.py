while True:
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Error: Please enter valid numbers.")

    else:
        operator = input("Enter operator(+,-,*,/): ")
        if operator == "+":
            result = num1 + num2
            print("Result: ",result)
 
        elif operator == "-":
            result = num1 - num2
            print("Result: ",result)

        elif operator == "*":
            result = num1 * num2
            print("Result: ",result)

        elif operator == "/":
            if num2 == 0:
                print("Error: Cannot divide by zero.")
            else:
                result = num1/num2
                print("Result: ",result)

        else:
            print("Error: Invalid Operator")

        choice = input("Do you wish to calculate again? (yes/no): ").lower()
        if choice == "no" or choice == "n":
            break



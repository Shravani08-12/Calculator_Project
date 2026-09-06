num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

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



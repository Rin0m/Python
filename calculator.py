#calculator
operator = input("Enter an operator (+ - * / ): ")
num1 = float(input("Enter the 1st number: "))
num2 = float(input("Enter the 2nd number: "))

if operator == "+":
    print(f"Result: {num1 + num2}")
elif operator == "-":
    print(f"Result: {num1 - num2}")
elif operator == "*":
    print(f"Result: {num1 * num2}")
elif operator == "/":
    print(f"Result: {num1 / num2}" if num2 != 0 else "Error: Division by zero!")
else:
    print("Invalid operator!")
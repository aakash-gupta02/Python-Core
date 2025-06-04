num1 = int(input("Enter 1st Number: "))
num2 = int(input("Enter 2nd Number: "))

operator = input(
    "Enter an Operator:\n"
    "+  for Addition\n"
    "-  for Subtraction\n"
    "*  for Multiplication\n"
    "/  for Division\n"
    "%  for Percentage (num1 / num2 * 100)\n"
    "Your choice: "
)


if operator == "+":
    print(f"Addition of {num1} + {num2}: {num1 + num2}")

elif operator == "-":
    print(f"Subtraction of {num1} - {num2}: {num1 - num2}")

elif operator == "*":
    print(f"Multiplication of {num1} * {num2}: {num1 * num2}")

elif operator == "/":
    print(f"Division of {num1} / {num2}: {num1 / num2}")

elif operator == "%":
    percentage = (num1 / num2) * 100
    print(f"Percentage of {num1} / {num2}: {percentage}%")

else:
    print("Invalid Operator")

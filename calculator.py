num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2

if num2 != 0:
    division = num1 / num2
else:
    division = "Error: division by zero is not allowed"

# Print the results
print("Addition of", num1, "and", num2, "is:", addition)
print("Subtraction of", num1, "and", num2, "is:", subtraction)
print("Multiplication of", num1, "and", num2, "is:", multiplication)
print("Division of", num1, "and", num2, "is:", division)

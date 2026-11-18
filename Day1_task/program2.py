"""
Question 2: Simple Calculator
Write a Python program to accept two numbers from the user and perform the following operations:
- Addition
- Subtraction
- Multiplication
- Division
- Modulus
- Floor Division
- Exponentiation

"""


num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))


addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2
modulus = num1 % num2
floor_division = num1 // num2
exponentiation = num1 ** num2

print("\n--------- Simple Calculator ---------")

print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)
print("Modulus:", modulus)
print("Floor Division:", floor_division)
print("Exponentiation:", exponentiation)
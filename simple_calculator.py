def addition(num1, num2):
    return num1 + num2


def subtraction(num1, num2):
    return num1 - num2


def multiplication(num1, num2):
    return num1 * num2


def division(num1, num2):
    return num1 / num2


def modulus(num1, num2):
    return num1 % num2


num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
print("Enter 1 for addition")
print("Enter 2 for subtraction")
print("Enter 3 for multiplication")
print("Enter 4 for division")
print("Enter 5 for modulus")
choice = int(input("Enter your choice: "))
if choice == 1:
    print(addition(num1, num2))
elif choice == 2:
    print(subtraction(num1, num2))
elif choice == 3:
    print(multiplication(num1, num2))
elif choice == 4:
    print(division(num1, num2))
elif choice == 5:
    print(modulus(num1, num2))
else:
    print("Invalid choice")

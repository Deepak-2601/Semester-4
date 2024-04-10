def factorial_num(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact


num = int(input("Enter an integer: "))
print(factorial_num(num))

num = int(input("Enter the number: "))
fact = 1
if num == 1 or 0 == num:
    print(1)
else:
    for i in range(1, num + 1):
        fact *= i
print(fact)
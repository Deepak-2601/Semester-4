n = int(input("Enter the number: "))
x = False
for i in range(2, n):
    if n % i == 0:
        x = True
        break
if x:
    print(f"{n} is not a prime number!!")
else:
    print(f"{n} is a prime number!!")


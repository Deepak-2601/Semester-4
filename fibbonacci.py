terms = int(input("enter the number: "))
counts = 0
n0 = 0
n1 = 1
if terms < 0:
    print("Enter a positive number")
elif terms == 0:
    print(0)
elif terms == 1:
    print(1)
else:
    while counts < terms:
        print(n0)
        nth = n0 + n1
        n1 = n0
        n0 = nth
        counts += 1
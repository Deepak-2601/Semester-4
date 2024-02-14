start = int(input("Enter the lower limit: "))
end = int(input("Enter the upper limit: "))
for j in range(start, end):
    n = j
    x = False
    for i in range(2, n):
        if n % i == 0:
            x = True
            break
    if not x:
        print(j)

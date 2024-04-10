def bs(a):
    for i in range(len(a)):
        for j in range(0, len(a) - i - 1):
            if a[j] > a[j + 1]:
                temp = a[j]
                a[j] = a[j + 1]
                a[j + 1] = temp


arr = [- 2, 45, 0, 11, 9]
bs(arr)
print(arr)

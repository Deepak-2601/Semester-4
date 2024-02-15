l = [1, 5, 8, 8, 9, 15, 66, 8, 9, 12, 8]
x = int(input("Enter the number to check: "))
count = 0
for i in l:
    if i == x:
        count += 1
print(f"{x} occurred", count, "times")

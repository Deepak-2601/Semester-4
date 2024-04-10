def linearsearch(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return f"Found at index {i}"
    return "not found"


a = [1, 3, 99, 0, 87, 76, 12, 35, 67, 100]
x = int(input("enter the number: "))
print(linearsearch(a, x))

def binary_search(arr, target, high, low):
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


a = [10, 20, 30, 40, 50]
x = 40
r = binary_search(a, x, len(a)-1, 0)
if r != -1:
    print("Found")
else:
    print("Not found!!")

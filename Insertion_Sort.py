def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i
        while arr[j-1] > arr[j] and j > 0:
            arr[j-1],arr[j] = arr[j], arr[j-1]
            j -= 1


a = [2, 6, 10, 5, 12, 15, 9, 19, 11]
insertion_sort(a)
print(a)

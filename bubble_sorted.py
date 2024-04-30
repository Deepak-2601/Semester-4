def bubble_sort(arr):
    x = False
    while not x:
        x = True
        for i in range(0,len(arr)-1):
            if arr[i] > arr[i+1]:
                x = False
                arr[i], arr[i+1] = arr[i+1], arr[i]
    return arr


a = [8, 6, 0, 9, 5, 2, 1, 3, 7, 4]
print(bubble_sort(a))
def quicksort(arr, left, right):
    if left < right:
        prt_pos = partition(arr, left, right)
        quicksort(arr, left, prt_pos - 1)
        quicksort(arr, prt_pos + 1, right)


def partition(arr, left, right):
    i = left
    j = right
    pivot = arr[right]
    while i < j:
        while i < right and arr[i] < pivot:
            i += 1
        while j > left and arr[j] >= pivot:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    if arr[i] > pivot:
        arr[i], arr[right] = arr[right], arr[i]
    return i


a = [22, 11, 88, 66, 55, 77, 44, 0, 33, -2]
quicksort(a, 0, len(a) - 1)
print(a)

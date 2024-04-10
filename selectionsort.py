def Selection_sort(arrays):
    for i in range(0, len(arrays)-1):
        minimum = i
        for j in  range(i+1, len(arrays)):
            if arrays[j] < arrays[minimum]:
                minimum = j
        if minimum != 1:
            arrays[minimum], arrays[i] = arrays[i], arrays[minimum]
    return arrays


ae = [6, 8, 1, 2, 7, 3, 5, 0, 9, 19, 21, -5, 66]
print(Selection_sort(ae))

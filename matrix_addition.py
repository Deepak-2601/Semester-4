a = [[1, 2, 3],
     [2, 3, 5],
     [9, 0, 9]]
b = [[0, 6, 9],
     [9, 0, 2],
     [41, 90, 99]]
R = [[0, 0, 0],
     [0, 0, 0],
     [0, 0, 0]]
for i in range(len(a)):
    for j in range(len(a[0])):
        R[i][j] = a[i][j] + b[i][j]
for k in R:
    print(k)

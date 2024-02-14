a = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
r = [[0, 0, 0],
     [0, 0, 0],
     [0, 0, 0]]
for i in range(len(a)):
    for j in range(len(a[0])):
        r[j][i] = a[i][j]
for x in r:
    print(x)

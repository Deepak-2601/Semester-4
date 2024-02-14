s = input("Enter the word: ")
x = {}
for i in s:
    if i in x:
        x[i] += 1
    else:
        x[i] = 1
result = max(x,key=x.get)
print(result)

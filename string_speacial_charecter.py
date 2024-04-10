s = input("Enter the word: ")
l = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "-", "+"]
x = False
for i in s:
    for j in l:
        if i == j:
            x = True
if x:
    print("Found")
else:
    print("Not found")

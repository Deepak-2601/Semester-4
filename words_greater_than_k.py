def length_check(string_length, string_inp):
    x = []
    w = string_inp.split(" ")

    for i in w:
        if len(i) > string_length:
            x.append(i)
    return x


a = input("Enter the string: ")
l = int(input("Enter the length: "))
print(length_check(l, a))


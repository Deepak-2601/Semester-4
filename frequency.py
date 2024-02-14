# Python 3 code to demonstrate
# Maximum frequency character in String
# naive method

# initializing string
test_str = "Deepak"

# printing original string
print("The original string is : " + test_str)

# using naive method to get
# Maximum frequency character in String
all_freq = {}
for i in test_str:
    print(i)
    if i in all_freq:
        print("1", all_freq)
        all_freq[i] += 1
        print("2", all_freq)
    else:
        print("3", all_freq)
        all_freq[i] = 1
        print("4", all_freq[i])
res = max(all_freq, key=all_freq.get)

# printing result
print("The maximum of all characters in GeeksforGeeks is : " + str(res))

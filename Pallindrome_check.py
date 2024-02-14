w = input("Enter the words: ")
words = w[::-1]
if w.casefold() == words.casefold():
    print("Palindrome!!")
else:
    print("Not a palindrome!!")

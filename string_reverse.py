def reverse_string(string_input):
    words = string_input.split(" ")
    result = words[::-1]
    return result


s = input("Enter the string: ")
print(reverse_string(s))

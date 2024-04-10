def recursive_sum(number):
    if number == 1:
        return 1
    else:
        return number + recursive_sum(number-1)


num = 10
print(recursive_sum(num))

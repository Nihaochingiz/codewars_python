def multiply_numbers_from_range(start,end):
    i = start
    mult = 1
    while i <= end:
        mult = mult * i
        i = i + 1
    return mult


print(multiply_numbers_from_range(1,10))
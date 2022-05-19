def join_numbers_from_range(start,end):
    result = ''
    i = start
    while i <= end:
        result = result + str(i)
        i = i + 1

    return result
print(join_numbers_from_range(1,10))

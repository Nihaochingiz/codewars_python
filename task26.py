def multiply_numbers_from_range(start,end):

    i = start
    while i <= end:  
        sum = sum + i 
        i = i + 1     
    return sum


print(multiply_numbers_from_range(4,10))
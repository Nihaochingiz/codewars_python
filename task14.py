def truncate(string,num):
    new_string = string[0:num]
    return (new_string + '...')


print(truncate('text',2))
#string = 'If I look back I am lost'
#print(my_substr(string, 1)) # => 'I'
#print(my_substr(string, 7)) # => 'If I lo'

def my_substr(string,length):
    index = 0
    new_string = ''
    while index < length:
        current_char = string[index]
        new_string = new_string + current_char 
        index = index + 1 
    return new_string 

print((my_substr('hello',2)))
    

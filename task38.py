def filter_string(string,symbol):
    new_string = string.replace(symbol,'')
    return new_string
text = 'If I look back I am lost'
print(filter_string(text, 'I'))
    

def capitalize(string,num=0):
    return(string[num].upper()+string[1:])


print(capitalize('text'))

def capitalize(text):
    return f"{text[0].upper()}{text[1:]}"
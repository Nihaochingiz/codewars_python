def is_arguments_for_substr_correct(string,index,length):
    if length < 0:
        return False
    elif index < 0:
        return False
    elif index > len(string) - 1:
        return False
    elif index + length > len(string):
        return False
    else:
        return True
    
    
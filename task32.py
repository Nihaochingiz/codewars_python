def count_chars(string,char):
    index = 0
    count = 0
    newString = string.lower()
    while index < len(newString):
        if string[index] == char:
            count = count + 1
        index = index + 1
    return count

print(count_chars('Ilya','I'))


def count_chars(string, char):
    index = 0
    count = 0
    while index < len(string):
        if string[index].upper() == char.upper():
            count = count + 1
        index = index + 1
    return count
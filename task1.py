"""
Your task is to make a function that can take any non-negative integer as an argument and return it with its digits in descending order. Essentially, rearrange the digits to create the highest possible number.

Examples:
Input: 42145 Output: 54421

Input: 145263 Output: 654321

Input: 123456789 Output: 987654321
Списки в Python - упорядоченные изменяемые коллекции объектов произвольных типов (почти как массив, но типы могут отличаться).
list - как array в js
"""
def Descending_Order(num):
    num_list = list(map(int,str(num)))
    num_list = sorted(num_list,reverse = True)
    output =  ''.join(map(str, num_list))
    return int(output)  

print(Descending_Order(598))
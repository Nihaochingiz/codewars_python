'''
Задание
На электронной карте Вестероса, которую реализовал Сэм, союзники Старков отображены зелёным кружком, враги — красным, а нейтральные семьи — серым.

Напишите для Сэма функцию who_is_this_house_to_starks(), которая принимает на вход фамилию семьи и возвращает одно из трёх значений: 'friend', 'enemy', 'neutral'.

Правила определения:

Друзья ('friend'): 'Karstark', 'Tully'
Враги ('enemy'): 'Lannister', 'Frey'
Любые другие семьи считаются нейтральными ('neutral')
Примеры вызова:

print(who_is_this_house_to_starks('Karstark'))  # => 'friend'
print(who_is_this_house_to_starks('Frey'))      # => 'enemy'
print(who_is_this_house_to_starks('Joar'))      # => 'neutral'
print(who_is_this_house_to_starks('Ivanov'))    # => 'neutr

'''

def who_is_this_house_to_starks(last_name):
    
    if last_name == 'Karstark' or last_name == 'Tully':
        return 'friend'
    elif last_name == 'Lannister' or last_name == 'Frey':
        return 'enemy'
    else:
        return 'neutral'

print(who_is_this_house_to_starks('Karstark')) 
print(who_is_this_house_to_starks('Ivanov'))      

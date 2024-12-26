print('Работа со словарями:') # Работа со словарями:
my_dict = {'Igor': 1988, 'Диана': 2008} # Создание словаря
print(my_dict)
print(my_dict['Igor'])
my_dict.update({'Masha': 1983, 'Sacha': 1981}) # Добавление двух произвольных пар
print(my_dict)
a = my_dict.pop('Sacha') # Удаление пары в словаре по существующему ключу из словаря, сохранение в переменной
print(my_dict)
print(a) # печать значения удаленной пары
print(my_dict.get('Vasya', 'Такого ключа нет')) # печать значения из несуществующей пары и сообщение в этом случае
print(type(my_dict))
# Работа с множествами:
print('Работа с множествами:') # Работа с множествами:
my_set = {1, 1, 1, "Персик", 3.141577} # Создание множества с разными типами посторяющихся данных
print(my_set)
print(my_set.discard(1), '"1" Удалился')
print(my_set)
print(my_set.add(5), "Добавление '5'")
print(my_set)
print(my_set.add(5), ', Уже есть такой')
print(my_set)
print(type(my_set))
# immutable_var = [1, 2], True, '567' # кортеж
# print(immutable_var)
# print(type(immutable_var))
# immutable_var[0][0] = 7 # изменение списка внутри кортежа
# print(immutable_var)
# print(immutable_var.__sizeof__()) # размер занимаемог места в памяти
# immutable_var[1] = 77  # неудачная попытка изменения элемента кортежа
# second path
mutable_list = [[1, 2], True, '567'] # list
print(mutable_list)
print(mutable_list.__sizeof__()) # размер занимаемог места в памяти
print(type(mutable_list[1])) # тип элемента списка
print(type(mutable_list))
mutable_list[1] = 7 # изменение элемента списка
print(mutable_list) # вывод измененного списка
mutable_list = mutable_list + [1] * 3 # Конкотенация + повторение последнего элемента 3 раза
print((mutable_list)) # вывод 1-го элемента кортежа

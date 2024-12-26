# my_string = input("Введите строку: ")
# print(my_string)
# print(my_string.upper())
# print(my_string.lower())
# print(my_string.replace(' ',''))
# print(my_string[0 : 2].upper())
# print(my_string[ 5 :  : -1])
# from os import remove
food = ['яблоко' , 'персик' , "банан" , "вишня"]
# print(food[1])
food[0] = 'груша'
food.extend(["черешня", 2.47])
# my_string = input("Введите строку: ")
# food[0] = my_string
print(food)
# print(type(food[5]))
food.remove(2.47)
# print("банан" not in food)
food.append("excellent!!!".upper())
print(food[5])
my_string = food[5]
print(my_string[12 : 8 :-1].upper())

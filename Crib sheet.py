# Средний балл
print('Средний балл')
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
print('Список оценок:', grades) # Вывод списка оценок
students = {'Johnny','Bilbo','Steve','Khendrik','Aaron'}
print('Множество неупорядоченных имён:', students) # Вывод множества студентов
students = list(students) # преобразование множества в список
print('Список неупорядоченных имён:', students)  # Вывод списка студентов
students = sorted(students) # Сортировка имен студентов в алфавитном порядке
print('Список упорядоченных имён:', students)  # Вывод списка студентов в алфавитном пороядке
average_score = {}
print('''Объявление словаря и 
поэлементное зополнение:''')
average_score[students[0]] = sum(grades[0]) / len(grades[0])
average_score[students[1]] = sum(grades[1]) / len(grades[1])
average_score[students[2]] = sum(grades[2]) / len(grades[2])
average_score[students[3]] = sum(grades[3]) / len(grades[3])
average_score[students[4]] = sum(grades[4]) / len(grades[4])
print(average_score)

quantity_hw = 12  # Количество выполненных ДЗ
number_of_hours = 1.5  # Количество затраченных часов
course_name = "Python"  # Название курса
time_for_one_task = number_of_hours / quantity_hw
print('Курс:', course_name, ',', 'всего задач:', quantity_hw,
      ', затрачено часов: ', number_of_hours, ', среднее время выполнения:'
      , time_for_one_task, 'часа, или в минутах:'
      , time_for_one_task * 60)  # чуть дополнил

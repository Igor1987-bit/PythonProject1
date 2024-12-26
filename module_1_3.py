name = "Igor"
print(name, id(name))
age = 36
print("age:", age, id(age))
New_age = age + 12
print(New_age, id(New_age), type(New_age))
Very_new_age = age + 12.2
print(Very_new_age, id(Very_new_age), type(Very_new_age))
is_student = True
print(is_student, type(is_student), id(is_student))
print(id(age) == id(New_age))
print(id(age) != id(New_age))
print(id(age) < id(New_age))
print(age + New_age)
# Кортежи.
# Кортеж - это последовательность элементов, похожая на список. 
# Кортеж является неизменяемым типом.
# Нельзя изменять, удалять или добовлять элементы в кортеже.
# Пример:
user = ("Alexander", 25)
print(user)

# Для определения кортежа, можно перечислить его значения через запятую, не применяя скобки.
# Пример:
user = "Alexandr", 25
print(user)

# Если кортеж состоит хотя бы из одного элемента, то нужно после единственного элемента ставить запятую.
# Пример:
user = ("Alexander",)

# Для создания кортежа из списка можно передать список в функцию <tuple()>, которая возвратит кортеж.
# Пример:
users_list = ["Alexandr", "Sam", "Nikol"]
users_tuple = tuple(users_list)
print(users_tuple)

# К кортежу можно обращаться по элементам, так же как и по индексу в списках.
# Индексация начинается с нуля, а сели индексировать с конца элементов, то -1.
# Пример:
users = ("Alexandr", "Sam", "Nikol")
print(users[0])  
print(users[2])   
print(users[-1])
 
# получим часть кортежа со 2 по 4 элемент.
print(users[1:4]) 

# При необходимости кортеж можно разложить на отдельные переменные.
# Пример:
user = ("Sam", 35, False)
name, age, isMarried = user
print(name)             # Sam
print(age)              # 35
print(isMarried)        # False

# Картежи удобно использовать в случае, когда нужно возвратить несколько значений из функции.
# Когда функция возвращает несколько значений, фактически она возвращает в кортеж.
# Пример:
def get_user():
    name = "Sam"
    age = 35
    is_married = False
    return name, age, is_married
 
user = get_user()
print(user[0])              # Sam
print(user[1])              # 35
print(user[2])              # False

# Функция <len()> позволит получить длину кортежа.
# Пример:
user = ("Sam", 35, False)
print(len(user))        # 3

# Так-же можно для перебора кортежа использовать стандартные циклы <for> и <while>
# Пример:
user = ("Sam", 35, False)
for item in user:
    print(item)

# Используем цикл <while>.
# Пример:
user = ("Sam", 35, False)
 
i = 0
while i < len(user):
    print(user[i])
    i += 1


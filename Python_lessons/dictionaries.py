# Словари / Dictionaries
# Содержат набор элементов в формате (ключ : значение)
# Выбрать элемент можно по названию "ключа"
# Нельзя рассчитывать на последовательность элементов, в которой их положили
product = {
    "name": "iPhone X",
    "stock": "50",
    "price": "65000.0"
}
print(product)

# Кол-во элементов словоря подсчитываем функцией <len()>
product = {
    "name": "iPhone X",
    "stock": "50",
    "price": "65000.0"
}
print(len(product))

# Добовление элемента ключа, можно изменять элементы по названию ключа
# Если такой ключ есть, значение будет обновленно
# Если ключа нет, он будет создан
product = {
    "name": "iPhone X",
    "stock": "50",
    "price": "65000.0"
}
product["memory"] = 64

# Значение элемента можно получить указав ключ в квадратных скобках
product = {
    "name": "iPhone X",
    "stock": "50",
    "price": "65000.0"
}
print(product["price"])

# Можно выводить значение для данного ключа
# Если он не доступен с помощью метода <get()>
# Если ключ не доступен, он возврощает значение NONE
product = {
    "name": "iPhone X",
    "stock": "50",
    "price": "65000.0"
}
print(product.get("CPU"))

# Можно задать значение о умолчанию: например <0>
print(product.get("CPU", 0))

# Удаление ключа
product = {
    "name": "iPhone X",
    "stock": "50",
    "price": "65000.0"
}
print(product)
del product["price"]
print(product)

# Списки и словари можно вкладывать друг в друга
# Получим структуры данных, которые отображают нашу предметную область
operating_systems = ['Mac OS', 'Windows', 'Ubuntu', 'Fedora', 'Kali linux']
product = {
    "name": "Thinkpad",
    "stock": "50",
    "price": "65000.0"
}
print(product)
product["recomend"] = operating_systems
print(product)

# Вложенные списки ничем не отличаются от обычных
# Создали ключ "recomend" для работы с списком
operating_systems = ['Mac OS', 'Windows', 'Ubuntu', 'Fedora', 'Kali linux']
product = {
    "name": "Thinkpad",
    "stock": "50",
    "price": "65000.0",
    "recomend": operating_systems,
}
print(product["recomend"])
print(product["recomend"][4])

# С помощью метода <.append> добовляем элементы
operating_systems = ['Mac OS', 'Windows', 'Ubuntu', 'Fedora', 'Kali linux']
product = {
    "name": "Thinkpad",
    "stock": "50",
    "price": "65000.0",
    "recomend": operating_systems,
}
print(product["recomend"])
print(product["recomend"][4])
product["recomend"].append("CentOS")
print(product)

# Список словарей часто используется в разработке. Это может быть список товаров
# Создал список словарей
# <[]> скобки списка
# <{}> в эти скобки заключены элементы словаря
# Внутри списка, вложены словари. Так же, в словаре сеть вложение списка
stock = [
    {'name': 'Lenovo Thinkpad', 'stock': 35, 'price': 73000.0, 'recomended': ['Asus ZenBook', 'HP Pavilion']},
    {'name': 'Aser Predator', 'stock': 28, 'price': 71900.0, 'discount': '4500'},
    {'name': 'Apple MakBook Air', 'stock': 26, 'price': 80000.0}
]
# Выдает первый словарь
print(stock[0])
# Выдает значение словоря
print(stock[0]["name"])
# Увеличили значение словоря на 5000
stock[0]["price"] = stock[0]["price"] + 5000
print(stock)
# Более простой способ увеличить или прибавить значение
stock[0]["price"] += 5000
print(stock)

# Получение данных. Обращаемся к словарям по ключам/индексам
stock = [
    {'name': 'Lenovo Thinkpad', 'stock': 35, 'price': 73000.0, 'recomended': ['Asus ZenBook', 'HP Pavilion']},
    {'name': 'Aser Predator', 'stock': 28, 'price': 71900.0, 'discount': '4500'},
    {'name': 'Apple MakBook Air', 'stock': 26, 'price': 80000.0}
]
print(stock[0]["recomended"][1])
# С помощью метода <type()> возврощаем тип
# Тип является "списком"
print(type(stock))
# Тип является "словарем"
print(type(stock[0]))











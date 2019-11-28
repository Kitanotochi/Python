# Вывод строки
operating_systems = ['Mac OS', 'Windows', 'Ubuntu', 'Fedora', 'Kali linux']
print(operating_systems)

# <len> - функция показывает колличество символов (длину строки)
operating_systems_count = len(operating_systems)
print(operating_systems_count)

# <.append> - метод, который добовляет элемент в конец списка
operating_systems.append('Linux Mint')
print(operating_systems)

# <.count> - метод, с помощью которого можно подсчитать кол-во интересующих элементов. Элемент 'Debian' отсутствует в списке: поэтому приравнивается в нулю.
print(operating_systems.count('Mac OS'))
print(operating_systems.count('Windows'))
print(operating_systems.count('Ubuntu'))
print(operating_systems.count('Fedora'))
print(operating_systems.count('Debian'))
print(operating_systems.count('Kali linux'))
print(operating_systems.count('Linux Mint'))

# Обрщение к элементам списка по индексу
print(operating_systems[0])
print(operating_systems[1])
print(operating_systems[2])
print(operating_systems[3])
print(operating_systems[4])
print(operating_systems[5])

# Срезы - часть списка
# Возвращает указанные значения "от и до"
print(operating_systems[0:4])
print(operating_systems[:5])

# Возвращает элемент с конца списка
print(operating_systems[-1])

# Поиск элементов по индексу
print(operating_systems.index('Ubuntu'))
print(operating_systems.index('Mac OS'))

# Сортировка списка элементов
# Не может сравнивать "string" и "int"
operating_systems = ['Kali linux','Mac OS', 'Fedora', 'Ubuntu', 'Windows']
operating_systems.sort()

# Оператор <in>
# Проверка на нахождения элемента в списке
operating_systems = ['Mac OS', 'Windows', 'Ubuntu', 'Fedora', 'Kali linux']
print('Ubuntu' in operating_systems)

# Удаление элементов в списке
operating_systems = ['Mac OS', 'Windows', 'Ubuntu', 'Fedora', 'Kali linux']
print(operating_systems)
del operating_systems[1]
print(operating_systems)

# Удаление элементов по названию
operating_systems = ['Mac OS', 'Windows', 'Ubuntu', 'Fedora', 'Kali linux']
print(operating_systems)
operating_systems.remove('Fedora')
print(operating_systems)


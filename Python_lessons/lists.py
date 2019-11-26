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



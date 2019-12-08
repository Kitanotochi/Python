# Функции
# Создаем функцию для подсчета скидок
def discounted_1(price, discount):
    price_with_discount = price - price * discount / 100
    print(price_with_discount)
# Вызываем функцию с разными значениями
discounted_1(100, 50)
discounted_1(90, 40)
discounted_1(55, 30)

# Усложняем функцию, добавив проверку
# Если скидка больше цены, входные даннные не верны
def discounted_2(price, discount):
    if discount >= 100:
        price_with_discount = price
    else:
        price_with_discount = price - price * discount / 100
    print(price_with_discount)
discounted_2(100, 50)
discounted_2(90, 40)
discounted_2(55, 30)

# Используем функцию <abs()>, которая возврощает обсолютное значение, положетельные числа
def discounted_3(price, discount):
    price = abs(float(price))
    discount = abs(float(discount))
    if discount >= 100:
        price_with_discount = price
    else:
        price_with_discount = price - price * discount / 100
    print(price_with_discount)
discounted_3(-100, 50)
discounted_3(90, 40)
discounted_3(55, -30)

# С помощью оператора <return> возврощаем значение функции в основную программу
def discounted_4(price, discount):
    price = abs(float(price))
    discount = abs(float(discount))
    if discount >= 100:
        price_with_discount = price
    else:
        price_with_discount = price - price * discount / 100
    return price_with_discount
# Положим результат в переменную, так как функция возврощает результат своей работы
x = discounted_4(100, 50)
print(x)

# Выводим функцию с помощью оператора <return>
def discounted_5(price, discount):
    price = abs(float(price))
    discount = abs(float(discount))
    if discount >= 100:
        price_with_discount = price
    else:
        price_with_discount = price - price * discount / 100
    return price_with_discount
# Создаем словарь
product = {
    "name": "iPhone X",
    "stock": "50",
    "price": "65000.0",
    "discount": "50"
}
# Добовляем новый ключ
product['with_discount'] = discounted_5(product['price'], product['discount'])
print(product)

# Используем именованные аргументы в функции со значением по умолчанию
def discounted_6(price, discount, max_discount = 50):
    price = abs(float(price))
    discount = abs(float(discount))
    if discount >= max_discount:
        price_with_discount = price
    else:
        price_with_discount = price - price * discount / 100
    return price_with_discount
product = {
    "name": "iPhone X",
    "stock": "50",
    "price": "65000.0",
    "discount": "70"
}
product['with_discount'] = discounted_5(product['price'], product['discount'])
print(product)

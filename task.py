# Просит пользователя ввести сумму сбережений
savings = int(input())

# Сбережения растут через 1 год под 5% годовой процентной ставкой
balance = savings * 1.05 

# Преобразует баланс в строку и обновляет переменную
balance = str(balance)

# Объединяет 2 строки, чтобы получить сообщение
message = "Amount in 1 year: " + balance

# Отобразите сообщение
print(message)
=====================
# Преобразование значений в числа
wins = int(input())
ties = int(input())

# 1 победа = 3 очка
# 1 ничья = 1 очко
# Вычисление количества очков
score = wins * 3 + ties 

# Соединение двух строк для создания сообщения
message = "Score: " + str(score)


# Вывод сообщения
print(message )
=============================

# Программа принимает количество очков в качестве ввода
score = int(input())

# Добавьте операцию сравнения внутри скобок
print(score > 100 )
========≈=======================
# Принимаем количество шагов и минут в качестве ввода
steps = int(input())
active_minutes = int(input())

# Сохраняем результат операций в переменной
goal_achieved = steps > 10000 or active_minutes > 30

# Выводим результат на экран
print(goal_achieved )
==================================
# Баллы на физическом тесте
physic_test = int(input())

# Баллы на тесте по симуляции полета
flight_test = int(input())

# Комбинируем операции, чтобы получить конечный результат
combi_ball = physic_test > 90 and flight_test  > 85

# Выводим результат на экран
print(combi_ball )
======================================

for i in range(3):
    print('Fasten your seat belt')

===========≈===========================
# Принимаем число в качестве ввода
number = int(input())

# Используем цикл while для обратного отсчета
while number >=0:
    print(number)
    number = number - 1
=======================================

# Принять начальную популяцию клеток в качестве ввода
cells = int(input())

# Принять количество дней в качестве ввода
days = int(input())

# Вывести популяцию клеток в конце каждого дня
for day in range(1, days + 1):
    cells *= 2  # Популяция удваивается
    print(f"Day {day}: {cells}")
============================================
# Принять начальную популяцию клеток в качестве ввода
cells = int(input("Enter initial cell population: "))

# Принять количество дней в качестве ввода
days = int(input("Enter number of days: "))

# Вывести популяцию клеток в конце каждого дня
day = 1
while day <= days:
    cells *= 2  # Популяция удваивается
    print(f"Day {day}: {cells}")
    day += 1
==============================================
# Принять количество доступных мест в качестве ввода
spaces = int(input())

# Вывести сообщение, если есть свободные места
if spaces > 0:
    print("Available spaces")
else:

# Вывести другое сообщение, если мест нет

    print("Sorry, the parking lot is full")
================================================
# установленные игры
games = [
  'Soccer', 'Tic Tac Toe', 'Snake',
  'Puzzle', 'Rally']

# принимаем выбор игрока в виде числа
choice = int(input())

# вывод соответствующей игры
print (games[choice] )
===========================≈===≈==≈≈===≈====≈

# список с завтраками
breakfasts = [
  'Donuts', 'Waffles', 'Yogurt', 
  'Burrito', 'Toast']

# индекс элемента, который нужно заменить
item = int(input())

# заменить этот элемент на "Pancakes"
breakfasts[item] = "Pancakes"

# отобразить обновленный список
print (breakfasts )
=====================================≈=========

players = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank"]

# Создайте 3 списка с 2 игроками в каждом
# Используйте срезы для создания списка для Group 1
g1 = players [0:2]

# Используйте срезы для создания списка для Group 2
g2 = players [2:4]

# Используйте срезы для создания списка для Group 3
g3 = players [4:6]

print("Group 1:\n"+str(g1))
# отобразить 1-ю группу


print("Group 2:\n"+str(g2))
# отобразить 2-ю группу


print("Group 3:\n"+str(g3))
# отобразить 3-ю группу
=≈=≈≈==================================≈=============
#Количество шагов за последнюю неделю
steps = [1513, 5035, 7891, 1212, 2534, 4648, 3785]

#Создать срез для последних 3 дней
last_3 = steps [-3:]

#Вывести срез
print(last_3 )
====================================================
weight = int(input())

def shipping_cost(weight):
    order = weight * 5
    return order

shipping_cost(weight)
print(shipping_cost(weight))
=================================================
def bmi(weight, height):  # Определяем функцию bmi для вычисления индекса массы тела (BMI)
    index = weight / (height * height)  # Рассчитываем BMI по формуле: вес делённый на квадрат роста
    return index  # Возвращаем вычисленный индекс массы тела

pacient = bmi(61, 1.83)  # Вызываем функцию bmi для пациента с весом 61 кг и ростом 1.83 м
print('parametr:', pacient < 18.5)  # Проверяем, меньше ли BMI пациента 18.5, и выводим результат

pacient_1 = bmi(75, 1.74)  # Вызываем функцию bmi для второго пациента с весом 75 кг и ростом 1.74 м
print('parametr:', pacient_1 < 18.5)  # Проверяем, меньше ли BMI второго пациента 18.5, и выводим результат
==============================================================
def agent(length, width):  # Определяем функцию agent, которая вычисляет площадь и периметр прямоугольника
    area = length * width  # Вычисляем площадь прямоугольника: длина * ширина
    perimeter = 2 * length + 2 * width  # Вычисляем периметр прямоугольника: 2 * длина + 2 * ширина
    return area, perimeter  # Возвращаем оба значения: площадь и периметр

area, perimeter = agent(50, 100)  # Вызываем функцию agent с длиной 50 и шириной 100, сохраняем результаты в переменные x и y
print(area, perimeter)  # Выводим значения площади (x) и периметра (y)
=============================================================

def agent(d1, d2):  # Определяем функцию agent, которая вычисляет площадь, периметр и стоимость прямоугольника
    area = d1 * d2  # Вычисляем площадь прямоугольника: длина * ширина
    perimeter = 2 * d1 + 2 * d2  # Вычисляем периметр прямоугольника: 2 * длина + 2 * ширина
    price = 1000 * area  # Рассчитываем стоимость, исходя из площади, где 1 кв. единица стоит 1000
    return area, perimeter, price  # Возвращаем три значения: площадь, периметр и стоимость

area, perimeter, price = agent(20, 15)  # Вызываем функцию agent с длиной 20 и шириной 15, сохраняем результаты в переменные
print('Area:',area)
print('Perimetr:', perimeter)# Выводим значения площади, периметра и стоимости
print('Price:', price)
===================================================================
def actual(d1, d2):
    area = d1 * d2
    invest = area > 700
    return invest

buy = actual(90, 100)
print(buy)
========================================================================
def agent(dlina, shirina):  # Определяем функцию agent, которая рассчитывает площадь и периметр прямоугольника
    area = dlina * shirina  # Вычисляем площадь: длина * ширина
    perimeter = 2 * dlina + 2 * shirina  # Вычисляем периметр: 2 * длина + 2 * ширина
    return area, perimeter  # Возвращаем два значения: площадь и периметр

area, perimeter = agent(5, 10)  # Вызываем функцию с длиной 5 и шириной 10, сохраняем результаты в переменные
print(area, perimeter)  # Выводим значения площади и периметра

=======================================================================
word = input()

def hashtag(word):
    info = '#'+ word
    return info

info = hashtag(word)
print(info)
=================================================================
def discounted(price, discount):
    return price * (1 - discount / 100)

result = discounted(300, 7)
print(result)

==========================================
def tax_nalog(doxod, nalog):  # Определяем функцию tax, которая вычисляет налог
    return doxod * nalog / 100  # Возвращаем рассчитанный налог: доход * ставка / 100

result = tax_nalog(100, 28)  # Вызываем функцию с доходом 100 и ставкой 28%, сохраняем результат в переменную result
print(result)  # Выводим рассчитанный налог
===================================================
molec = int(input())
input_days = int(input())
day = 1
while day <= input_days:
    molec *= 2
    print("Day " + str(day) + ": " + str(molec))
    day += 1
=====================================================

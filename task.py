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
games = [
  'Soccer', 'Tic Tac Toe', 'Snake',
  'Puzzle', 'Rally']
choice = int(input())
print(games[choice])
========================================
fasts = [
  'Donuts', 'Waffles', 'Yogurt',
  'Burrito', 'Toast']
item = int(input())
fasts[item] = 'Pancakes'
print(fasts)
======================================
days = ['Monday', 'Wednesday', 'Wednesday']
tasks = ['Gym', 'Homework', 'Pool']
for day in days:
    print(day + ':')
    for task in tasks:
        print(task)
=========================================
#Возвращает числа от 1 до 3, не включая 3
for i in range(1,3):# Внешний цикл: i = 1, Внутренний цикл: j = 2, вывод: 1 2, Внутренний цикл: j = 3, вывод: 1 3
    #Возвращает числа от 2 до 4, не включая 4
    for j in range(2,4):# Внешний цикл: i = 2, Внутренний цикл: j = 2, вывод: 2 2, Внутренний цикл: j = 3, вывод: 2 3
        print(i, j)
========================================
scores = [45, 67, 89, 34, 56, 77, 49, 91, 52]
for score in scores:
    if score >= 67:
        print(score)
===========================================
counter = 0
devices = ['PC', 'TV', 'PS', 'TV', 'PS', 'Xbox', 'TV']
for device in devices:
    # Если текущее устройство - 'TV', увеличиваем счетчик
    if device == 'TV':
        counter += 1
print('Number of TVs:', counter)
==========================================================
count = 0
message = "You have a new message"
for i in message:# Перебор каждого символа в строке
    if i == 'e': # Если текущий символ - 'e', увеличиваем счетчик
        count += 1
print(count)
=====================================================
scores = [7, 5, 8, 10, 8]
total = 0
for i in scores: # Перебор каждого элемента в списке
    total += i # Добавляем текущий элемент к общей сумме
    print("total:", total)
======================================================
songs = ["Hello", "Yesterday", "Happy", "Hallelujah"]
for song in songs:
    print('Searching')
    if song == 'Hallelujah':# Проверяем, является ли текущая песня "Hallelujah"
        print("Playing " + song)# Если песня найдена, выводим сообщение и прерываем цикл
        break
==========================================================
prices = [35, 80, 90, 89, 95, 76]
for price in prices:
  if price >= 90:
     break
print(price)
==========================================================
prices = [10, 54, 9, 44, 6, 26, 15]
total = 0
for price in prices:
    total += price # Добавляем текущую цену к общей сумме
    print(total)
    if total > 100:
        print("Limit exceeded")
        break
============================================================
x = 1
while x < 10:
    print(x)
    if x == 7:
        print('Stop')
        break
    x += 1
====================================================
while True:
    text = input()
    print(text)
    if text == 'Stop':
        break
===========================================================
ages = [10, 20, 30, 40, 75, 50, 60, 70]
for age in ages:
    if age < 40: # не печатает меньше или больше этого условия
        continue
    print(age)
===========================================================
animals = ["cat", "giraffe", "lion", "leopard", "mouse"]
for animal in animals:
  if animal[0] == "l": # не печатает элементы имеющие это условие
    continue
  print(animal)
============================================================
day_num = 4
while day_num <= 9:# Цикл работает, пока день не превысит 9
    if day_num == 4:
        day_num += 1# Переходим к следующему дню
        continue
    print("Turn on the lights!")
    day_num += 1 # Увеличиваем день, чтобы не зациклиться
===============================================================
new_menu = []# Создаем пустой список для нового меню
dish1 = "Pasta"# Определяем блюда для нового меню
dish2 = "Pizza"
dish3 = "Salad"
# Определяем функцию для добавления блюда в меню
def add_to_menu(menu, dish):
    menu.append(dish)  # Добавляем блюдо в список
# Добавляем первое блюдо и печатаем меню
add_to_menu(new_menu, dish1)
print(new_menu)  # Вывод: ['Pasta']
# Добавляем второе блюдо и печатаем меню
add_to_menu(new_menu, dish2)
print(new_menu)  # Вывод: ['Pasta', 'Pizza']
# Добавляем третье блюдо и печатаем меню
add_to_menu(new_menu, dish3)
print(new_menu)  # Вывод: ['Pasta', 'Pizza', 'Salad']
==============================================================
delivery = True # Указываем, что доставка активна
def to_deliver(delivery):
    if delivery == True:# Если доставка активна, выводим запрос на ввод адреса
        print('Enter your address')
to_deliver(delivery)
=============================================================
score = 697
def cl(score):
    if score >= 70:
        return True
    else:
        return False

print(cl(score))
#=========================================
books = ['1984', 'War and Peace', 'The Great Gatsby', 'Animal Farm']
book = 'Animal Farm' # название книги, которое нужно найти.

def book_in_library(books, book):
    return book in books

print(book_in_library(books, book))
#=================================================
group = ['1984', 'War and Peace', 'The Great Gatsby', 'Animal Farm']
def check_count(group):
    if len(group) >= 3:
        return True
    else:
        return False
print(check_count(group))

==================================================
prices = [33, 49, 55, 14]
#Функция sum принимает список возвращает сумму всех его элементов.
total = sum(prices)
print(total)
=================================================
prices = [20, 30, 40, 50, 60]
# Функция sum(prices) возвращает сумму всех элементов списка
total = sum(prices)
print("Total Price:", total)
# Функция len(prices) возвращает количество элементов в списке
number = len(prices)
print("Count:", number)
# Средняя цена рассчитывается общая сумма делённая на количество
avg_price = total/number
print("Average Price:", avg_price)
================================================
prices = [33, 49, 55, 14]
min_price = min(prices)
print(min_price)
prices = [33, 49, 55, 14]
min_price = max(prices)
print(min_price)
prices = [33, 49, 55, 14]
min_price = len(prices)
print(min_price)
prices = [33, 49, 55, 14]
min_price = sorted(prices)
print(min_price)
===============================================================
players = ["Zoe", "Liam", "Emma", "Noah", "Olivia"]
sort_players = sorted(players)# сортировка по алфавиту
print(sort_players)
players = ["Zoe", "Liam", "Emma", "Noah", "Olivia"]
sort_players = sorted(players, reverse=True)
print(sort_players)
==================================================================
ages = [25, 36, 33, 19, 56]
sort_ages = sorted(ages, reverse=True)
print(sort_ages[0:3])
================================================================
points = (12, 14, 9, 10, 9)
for point in points:
    if point > 10:
        print(point, 'passed')
=============================================================
scores = (98, 96, 91, 88, 64)
winner, *rest = scores# в распаковке с кортежами неизвестной длины.
print(winner)
print(rest)
======================================================================
guests = {'Anna', 'Mery', 'Jonathan'}
guests.add('Robert')#add добавляет новый элемент 'Robert' в множество.
#В отличие от remove, discard не вызывает ошибку, если элемента нет в множестве.
guests.remove('Mery')
print(guests)
=====================================================================
guests = {'Anna', 'Mery', 'Jonathan'}
guests.clear()
print(guests)
====================================================================
set1 = {'apple', 'banana'}
set2 = {'banana', 'cherry'}
#Метод union возвращает новое множество,
#содержащее все уникальные элементы из обоих множеств.
combi = set1.union(set2)
print(combi)
====================================================================
set1 = {'apple', 'banana', 'cherry'}
set2 = {'banana', 'orange'}
#difference() возвращает которые присутствуют только в первом наборе
combi = set1.difference(set2)
print(combi)
==================================================================
car = {
  "brand": "Audi",
  "model": "Q5",
  "year": "2008"
}
print(car['brand'])
print(car['model'])
print(car['year'])
======================================================
contact = {
  "name": "John",
  "company": "Google",
}
print(contact["company"])# Получение значения по ключу 'company'
=================================================================
contact = {
    "name": "vlad",
    "age": "62",
}
name = contact.get("name")# Получение значения по ключу 'name'
print(name)
age = contact.get("age")# Попытка получить значение по по ключу 'age'
print(age)
==================================================================
contact = {
    "name": "vlad",
    "age": 45
}
info_keys = contact.keys()
info_values = contact.values()
info = car.items()
print(info)
print(info_keys)
print(info_values)
==================================================================
user1 = {
    "Name": "Albert",
    "Age": 29
}
user1["Age"] = 30# значение по ключу "Age" в словаре обновляется на 30
print(user1["Age"])
print(user1.items())
======================================================================
user = {
    'name': 'albert',
    'age': 29
}
user.update({'age': 35}) # значение по ключу "Age" обновляется на 35
print(user['age'])
print(user.items())
=====================================================================
user = {
    'name': 'albert',
    'company': 'google'
}
user.update({"Age": 30, "Surname": "Johnson"})# значение обновляется на "Age": 30, "Surname": "Johnson"
print(user.items())
=======================================================================
car = {
  "Brand": "Ford",
  "Model": "Mustang",
  "Color": "red"
}
car.pop('Color')# удаление
print(car)
==========================================================================
car = {
  "Brand": "Ford",
  "Model": "Mustang",
  "Color": "red"
}
print('Color' in car)
========================================================================
car = {
  "Brand": "Ford",
  "Model": "Mustang",
  "Color": "red"
}
for i in car: # итерация по ключам
    print(i)
for i in car.values(): # итерация по значениям
    print(i)
======================================================================== 
nums = []
for x in range(1, 51):
    nums.append(x)
print(nums)
nums = [ x for x in range(1,51)]
print(nums)
============================================================================
nums = [x*2 for x in range(11)]
print(nums)
#========================================================
tags = ["travel", "vacation", "journey"]
hash = ['#' + x for x in tags]
print(hash)
===========================================================================
users = ["Brandon", "Emma", "Brian",
"Sophia", "Bella", "Ethan",
"Ava", "Benjamin", "Mia", "Chloe"]
#перебирает каждый элемент x из списка users.
group = [x for x in users if x[0] == 'B']
print(group)
#======================================================
sports = ["Football", "Basketball", "Tennis", "Golf", "Volleyball"]
#перебирает каждый элемент x из списка sports
group = [x for x in sports if "ball" in x]
print(group)
#=============================================================
scores = [68, 74, 89, 64, 85, 93]
#перебирает каждый элемент x из списка scores.
#добавляет в новый список только те элементы x,
#которые удовлетворяют условию (то есть больше или равны 74)
winner = [x for x in scores if x >= 74]
print(winner)
==================================================
words = ["tree", "button", "cat", "window", "defenestrate"]
#перебирает каждый элемент x из списка words
# который включает только слова длиннее 4 букв
result = [x for x in words if len(x) > 4]
print(result)
=============================================================
citys = ['moscow', 'yerevan,', 'kiev']
result = [x.capitalize() for x in citys]
print(result)
============================================================
tags = ['moscow', 'yerevan,', 'kiev']
result = ['##$' + x for x in tags]
print(result)
==============================================================
points = [3, 77, 22, 11, 7, 9]
result = [x for x in points if x >= 8]
print(result)
==============================================================
points = (12, 14, 9, 10, 9)
result = [x for x in points if x >= 10]
print(result, 'passed')
==============================================================
print([x for x in (12, 14, 9, 10, 9) if x >= 10], 'passed')
==============================================================
scores = [45, 67, 89, 34, 56, 77, 49, 91, 52]
result = [x for x in scores if x >= 67]
print(result)
==============================================================
data = ["anna", "bob", "mery"]
names = [x.capitalize() for x  in data]
print(names)
=========================================================
#==========================================================
prices = [250, 300, '777', 400]
try:
  total = sum(prices)
  print(total)
except TypeError:
  print("Invalid data type")
print("Happy Shopping")
#==========================================================
color = "Green"
try:
  print(color)
except NameError:
  print("Check the variable name")
  #===================================================
colors = ["Red", "Yellow", "Green"]
try:
  print(colors[10])
except:
  print("Error")
#======================================================
price = input()
try:
    price_value = int(price)
except ValueError:
    print("Please enter a number")
==========================================================
products = ["Water", "Chocolate", "Chips", "Soda", "Sandwich"]
choice_index = int(input())
try:
    print(products[choice_index])
except:
    print('wrong index')
==================================================================
prices = [559, 879, "N/A", 349]
try:
  print(sum(prices))
except TypeError:
  print("Check the prices")
finally:
  print("Need help? Contact us")
=========================================================
books = ['Harry Potter', 'Dune', 'Emma']
try:
  choice = books[1]
except IndexError:
  print("Out of range")
else:
  print(choice + " Привет как дела!")
#=============================================================
products = ['ball', 'toy', 'paper']
try:
    count = len(products)
except:
    print("Error")
else:
    print("Count of products:", count)
#==================================================================
products = ['ball', 'toy', 'paper']
try:
    count = len(products)
except:
    print("Error")
finally:
    print("Count of products:", count)
#==========================================================
try:
  print(len(3745))
except:
  print("Error")
finally:
  print("Save")
==========================================================
print('Rate from 0 to 10')
rating = 15
if rating > 10 or rating < 10:
    raise ValueError ("Rate from 0 to 10") #Пользовательские исключения
=========================================================
price = 995
if price > 500:
  raise ValueError ("Rate > 500")#Пользовательские исключения
========================================================
temp = -15
if temp > 50 or temp < -10:
    raise ValueError('invalid range') #Пользовательские исключения
=====================================================
try:
  print(3 + "3")
except ValueError:
  print("Cannot add different types")
except TypeError:
  print("Не соответствие типов") # Не соответствие типов
========================================================
def welcome(name):
    return 'welcome,' + name
greet('bob')
======================================================
#=======================================================
def welcome(name):
    return 'helllo,' + name
greet = welcome
print(greet('bob'))
#=======================================================
def shout(text):
    return text.upper()
yell = shout
print(yell('helllo'))
#====================================================
def one(name):
    return 'welcome,' + name
def two(name, func):
    return func(name)
print(two('Alice', one))
=====================================================
def welc(name):
  return "Welcome, " + name

def bye(name):
  return "Goodbye, " + name

def process_user(name, func):# Функция высшего порядка
  return func(name)

print(welc("Vlad"))
print(bye("Miqael"))
print(process_user("Vlad", welc))
print(process_user("Miqael", bye))
======================================================
def book_title(title):
    return 'Название книги: ' + title
def info(title, func):
    return func(title)
print(info('Великий Гэтсби', book_title))
=======================================================
     LAMBDA
greet = lambda name: 'Welcome, ' + name # лямбда называются анонимными функциями
# ^ lambda argument ^    ^ выражение ^
print(greet('bob'))
================================
x = (lambda price, count : price * count) (2,10)
print(x)
=================================
res = (lambda x, y: x + y) (2, 3)
print(res)
====================================
def mult(n):
  return lambda a : a * n

doubler = mult(2)
tripler = mult(3)
print(doubler(5))
print(tripler(5))
=======================================
names = ["alice", "bob", "CHARLIE", "dEborah"]
def capitalize(name):
    return name.capitalize()
capitalized = map(capitalize, names)#  map — это итерируемый объект,
# который преобразует элементы "на лету"
capitalized = list(capitalized)# list(capitalized) преобразует итерируемый объект,
# возвращенный map, в список.
print(capitalized)
#=========================================
names = ["alice", "bob", "CHARLIE", "dEborah"]
capitalized = list(map(lambda name: name.capitalize(), names))
print(capitalized)
================================================================
 prices = [20, 30, 10, 40]
def discount(price):
    discounted_price = price * 0.5
    return discounted_price
discounted_prices = list(map(discount, prices))
                          # ^функция^ ^итерируемый^
print(discounted_prices)
============================================   
count_scores = [80, 60, 70, 40, 90]
def passing(score):
    return score >= 70
status = list(map(passing, count_scores))
               # ^функция^ ^итерируемый^
print(status)
#=============================================
numbers = [1, 2, 3]
doubled = list(map(lambda x: x*2, numbers))
print(doubled)
#=============================================
numbers = (1, 2, 3)
doubled = tuple(map(lambda x: x*2, numbers))
print(doubled)
#=============================================
numbers = {1, 2, 3}
doubled = set(map(lambda x: x*2, numbers))
print(doubled)
=========================================
products = ("Table", "Sofa", "Cushion", "Bookshelf", "Vase")
filtered_prod = tuple(filter(lambda name: len(name) == 4, products))
# filter удобна для отбора (for + if) элементов, удовлетворяющих определенным критериям.
# len(name) проверяет, имеет ли строка длину ровно 4 символа.
print(filtered_prod)
=============================================
products = {'Table': 110, 'book': 120, 'car': 45, 'Lamp': 70}
filtered_products = dict(filter(lambda item: item[1] < 90, products.items()))
# filter обрабатывает каждую пару (ключ, значение) из products.items(),
# применяя условие из lambda.
# item[1] — доступ к значению (цена продукта)
# item[1] < 90 — условие: выбрать только те элементы где (цена) меньше 90.
print(filtered_products)
================================================
names = ["John", "Emma", "Jake", "Rachel", "James"]
filtered = list(filter(lambda name: name[0] == 'J', names))
# filter берет функцию и итерируемый объект
# name[0] — это первая буква имени
# name[0] == 'J' возвращает True, если имя начинается с буквы 'J'
print(filtered)
==================================================
user_answers = ["Yes", "", "No", "", "Maybe", "", "Yes"]
filtred = list(filter(lambda answer: answer != '', user_answers))
# фильтрация где ответ не пуст
print(filtred)
===================================================
                 *ARGS
def total(numbers):
  result = 0
  for i in numbers:
    result+=i
  return result
nums = [1,2,3,4,5]
print(total(nums))
============================================
def total(*prices): # * позволяет передавать в функцию
    # любое количество аргументов. собирает аргументы в кортеж
    result = 0
    for price in prices:# В цикле for каждый элемент из prices суммируется
        result += price
    return result
print(total(1, 2, 3, 4, 5))
print(total(1, 2, 3, 4, 5, 6, 7))
print(total(1, 2, 3))
=====================================================
def show(category, *counts): # * собирает аргументы в кортеж
    # category — обязательный позиционный аргумент
    # *counts позволяет передать произвольное количество аргументов
    # "Electronics" передается как значение аргумента category
    # "Laptop", "Smartphone", и "Tablet" собираются в кортеж counts.
  print("Category: " + category)
  for count in counts:
    print(count)
show("Electronics", "Laptop", "Smartphone", "Tablet")
=====================================================
                    # ** kwargs
def display_info(**json): # **kwargs принимает аргументы в виде словаря,
    # состоящего из пар ключ:значение. группирует их в словарь с парой ключ:значение
    for key, value in json.items():
        print(key, ':', value)
display_info(name='Vlad', age=46, city="New York")
======================================================
def outer_function():
    print("Hello from the outer function")
    def inner_function():
        print("Hello from the inner function")
    # inner_function выводит строку "Hello from the inner function"
    inner_function()
# outer_function выводится строка "Hello from the outer function"
outer_function()
#================================================
def greet(name):
    print("Hey", name)
    def account():
        return "Your account is created!"
    message = account() #  account вызывается, и её результат сохраняется в переменной message
    return message # Функция greet возвращает значение переменной message,
    # то есть строку "Your account is created!"
print(greet("Bob"))
=============================================
def order():
  def prepare():
    return "Your meal is being prepared!"
  status = prepare() # prepare вызывается,
  # и её возвращаемое значение сохраняется в переменной status.
  return status
print(order())
============================================≈===========
def мигающие_фары(функция):
    def обертка():
        print("Включаем мигающие фары!")
        функция()
        print("Выключаем мигающие фары!")
    return обертка

@мигающие_фары
def машинка_едет():
    print("Машинка едет!")

машинка_едет()
===================================================================









    


    





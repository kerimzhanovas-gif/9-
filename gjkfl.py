# name = 'Сезим'
# age = '18'
# print(f'Привет, меня {name} зовут , мне {age} лет.')

# num_1 = int(input('Введите число: '))
# num_2 = int(input('Введите число: ')) 
# print(num_1 + num_2)

# length = int(input('Введите длину прямоугольника: '))
# width = int(input('Введите ширину прямоугольника: '))
# print((length + width) * 2)
# print(length * width)

# name = str(input('Введите своё имя: '))
# birth_year = int(input('Введите год своего рождения: '))
# age = 2025 - birth_year
# print(f'Привет, {name}! В 2025 году тебе {age} лет!')

# price = int(input('Введите цену товара: '))
# discount = int(input('Введите скидку на товар в %: '))
# final = price - price * discount / 100
# print(f'Цена товара: {final}')

# number = int(input('Введите любое число: '))
# if number > 0:
#     print('Число положительное.')
# elif number < 0:
#     print('Число отрицательное.')
# else:
#     print('Число нулевое.')

# age = int(input('Введите свой возраст: '))
# if age < 18:
#     print('Вы несовершеннолетний.')
# elif age <= 60:
#     print('Вы взрослый.')
# else:
#     print('Вы пенсионер.')

# pin = int(input('Введите пароль: '))
# if pin == 12345:
#     print('Пароль верный.')
# else:
#     print('Пароль неверный. ')

# num = int(input('Введите число: '))
# if num % 2 == 0:
#     print('Число четное.')
# else:
#     print('Число нечетное.')

# year = int(input("Введите год: "))
# if (year % 4 == 0 and year % 100 != 0):
#     print("Високосный")
# else:
#     print("Обычный")

# for i in range(1, 11):
#     print(i)

# n = int(input('Введите число: '))
# for i in range(1, 11):
#     print(f'{n} * {i} == {n*i}')

# n = int(input('Введите число: '))
# total = 0
# for i in range(1, n + 1):
#     total += i
#     print(total)

# str = input('Введите строку: ')
# for char in str:
#     print(char)

# while True:
#     pin = input('Введите пароль: ')
#     if pin == 'python':
#         print('Пароль верный.')
#         break
#     else:
#         print('Пароль неверный.')
#         continue

# nums = {1, 2, 3, 4, 5}
# print(sum(nums))
# print(sum(nums) / 5)

# words = []
# for i in range(1, 6):
#     word = input("Введите слово: ")
#     words.append(word)
# print("Обратный порядок:", words[::-1])

fruits = ["яблоко", "банан", "киви"]
fruits.append("клубника")
fruits.remove("киви")
print(fruits)
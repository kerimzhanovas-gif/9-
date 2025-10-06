num_1 = int('1234')
num_2 = 4321
num_3 = 2314
print (num_1+num_2)
print (f'{num_1}+{num_2}+{num_3}={num_1+num_2+num_3}')

num_1_1=3241
num_2_1=3231
print(num_1_1+num_2_1)

var_1=True
var_2=8363
print(var_1+var_2)


print('hello world')
name=input('Как вас зовут?')
#1 вариант
print('Меня зовут', name.capitalize())
#2 вариант
print(f'Меня зовут {name.upper()}')
#3 вариант
print('Меня зовут {}' .format(name.lower()))

person_1 = 182
person_2 = 194
person_3 = 175
person_4 = 168
person_5 = 155
average = (person_1 + person_2 + person_3 + person_4 + person_5) / 5
print(f'Средний рост всех людей - {round(average, 1)} см')


person_1 = float(input('введите рост 1: '))
person_2 = float(input('введите рост 2: '))
person_3 = float(input('введите рост 3: '))
person_4 = float(input('введите рост 4: '))
person_5 = float(input('введите рост 5: '))

average = (person_1 + person_2 + person_3 + person_4 + person_5) / 5

print(f'Средний рост всех людей - {round(average, 1)} см')
print('Привет, я бот Айос')

name = "Сезим"          # ← впиши сюда своё ФИО
age = 18                # ← свой возраст
place = "Бишкек"        # ← место жительства
gender = "ж"            # ← свой пол

print(f'Вас зовут - {name.title()}')
print(f'Вам {age} лет')
print(f'Вы живёте - {place.capitalize()}')
print(f'Ваш пол - {gender}')




print('Привет, я бот Айос!')
name = str(input('укажите ваше ФИО '))
age = int(input('укажите ваш возраст '))
place = str(input('укажите место жительства '))
gender = str(input('укажите ваш пол м/ж '))
print(f'Вас зовут - {name.title()}\nВам {age}лет\nВы живете - {place.capitalize()}\nВаш пол - {gender}')
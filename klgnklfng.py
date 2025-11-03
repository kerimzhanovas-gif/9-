# nums = []
# for i in range(3):
#     num = input("Введите число: ")
#     nums.append(num)
# smallest = nums[0]
# for num in nums:
#     if num < smallest:
#         smallest = num
# print(smallest)
# smallest = nums[0] — начальное значение.
# Цикл проверяет каждое число, и если находит меньшее, обновляет smallest.


# for i in range(1, 6):
#     print(i)

# age = int(input('Введите свой возраст: '))
# year = 1 + age
# print(f'Через год Вам будет {year} лет!')

# name = str(input('Введите своё имя: '))
# print(f'Привет, {name.capitalize()}!')

# class BankAccount:
#     def __init__(self, balance=0):
#         self.balance = balance
#     def deposit(self, amount):
#         self.balance += amount
#     def withdraw(self, amount):
#         if amount <= self.balance:
#             self.balance -= amount
#         else:
#             print('Недостаточно средств.')
#     def show_balance():
#          print(f"Текущий баланс: {self.balance}сом")
# acc = BankAccount('12345678')
# acc.deposit = 1500
# acc.withdrow = 200
# acc.show_balance()


# class BankAccount:
#     def __init__(self, balance=0):
#         self.balance = balance
#     def deposit(self, amount):
#         self.balance += amount
#     def withdraw(self, amount):
#         if amount <= self.balance:
#             self.balance -= amount
#         else:
#             print('Недостаточно средств.')
#     def show_balance(self):
#         print(f"Текущий баланс: {self.balance} сом")
# acc = BankAccount()
# acc.deposit(1500)
# acc.withdraw(200)
# acc.show_balance()

# grades = {
#     "Стелла": 85,
#     "Сезим": 92,
#     "Айгуль": 74
# }
# average = sum(grades.values()) / len(grades)
# print(f"Средняя оценка: {average}")
# print("Студенты с оценкой выше средней:")
# for name, grade in grades.items():
#     if grade > average:
#         print(f"{name}: {grade}")

data = [1, 2, 3, 2, 4, 1, 5, 3]
unique_data = list(set(data))
print(unique_data)
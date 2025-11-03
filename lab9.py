from abc import ABC, abstractmethod
class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass
    def refund(self, amount):
        pass
class CreditCardPayment(Payment):
    def pay(self, amount):
        print(f'Оплата суммой в {amount} сом была произведена кредитной картой.')
    def refund(self, amount):
        print(f'Возврат в сумму {amount} сом на кредитную карту выполнен.')
class CryptoPayment(Payment):
    def pay(self, amount):
        print(f'Оплата суммой в {amount} сом была произведена криптовалютой.')
    def refund(self, amount):
        print(f'Возврат в сумму {amount} сом в криптовалюте выполнен.')
payments = [CreditCardPayment(), CryptoPayment()]
for method in payments:
    method.pay(11037)
    method.refund(52)


from abc import ABC, abstractmethod
class Course(ABC):
    @abstractmethod
    def start(self):
        pass
    def get_materials(self):
        pass
    def end(self):
        pass
class PythonCourse(Course):
    def start(self): print('Курс Python запущен!')
    def get_materials(self): print('Материалы:основы синтаксиса, функции, классы, модули.')
    def end(self): print('Курс Python завершён!')
class MathCourse(Course):
    def start(self): print('Курс математики запущен!')
    def get_materials(self): print('Материалы:алгебра, геометрия, тригонометрия.')
    def end(self): print('Курс математики заверщён!')
python = PythonCourse()
math = MathCourse()
courses = [PythonCourse(), MathCourse()]
for c in courses:
    c.start()
    c.get_materials()
    c.end()
print(f"Пройдено курсов: {len(courses)}")

from abc import ABC, abstractmethod
class Delivery(ABC):
    @abstractmethod
    def calculate_cost(self, distance):
        pass
    def deliver(self):
        pass
class AirDelivery(Delivery):
    def calculate_cost(self, distance):
        return distance * 10
    def deliver(self):
        print("Доставка по воздуху выполнена.")
class GroundDelivery(Delivery):
    def calculate_cost(self, distance):
        return distance * 5
    def deliver(self):
        print("Наземная доставка выполнена.")
class SeaDelivery(Delivery):
    def calculate_cost(self, distance):
        return distance * 3
    def deliver(self):
        print("Морская доставка выполнена.")
deliveries = [AirDelivery(), GroundDelivery(), SeaDelivery()]
for d in deliveries:
    print(f"Стоимость: {d.calculate_cost(120)} сом")
    d.deliver()


class BankAccount:
    def __init__(self, owner, balance, pin):
        self.__owner = owner
        self.__balance = balance
        self.__pin = pin
    def deposit(self, amount, pin):
        if pin == self.__pin and amount > 0:
            self.__balance += amount
            print("Счёт пополнен на", amount)
        else:
            print("Ошибка: неверный PIN или сумма.")
    def withdraw(self, amount, pin):
        if pin == self.__pin and 0 < amount <= self.__balance:
            self.__balance -= amount
            print("Снято", amount)
        else:
            print("Ошибка: неверный PIN или недостаточно средств.")
    def change_pin(self, old_pin, new_pin):
        if old_pin == self.__pin:
            self.__pin = new_pin
            print("PIN успешно изменён.")
        else:
            print("Ошибка: старый PIN неверен.")
    def get_balance(self, pin):
        if pin == self.__pin:
            return self.__balance
        else:
            print("Ошибка: неверный PIN.")
owner = input("Введите имя владельца счёта: ")
balance = float(input("Введите начальный баланс: "))
pin = int(input("Создайте PIN-код: "))
acc = BankAccount(owner, balance, pin)
print("\nПополнение счёта.")
amount = float(input("Введите сумму для пополнения: "))
entered_pin = int(input("Введите PIN: "))
acc.deposit(amount, entered_pin)
print("\nСнятие денег.")
amount = float(input("Введите сумму для снятия: "))
entered_pin = int(input("Введите PIN: "))
acc.withdraw(amount, entered_pin)
print("\nПроверка баланса.")
entered_pin = int(input("Введите PIN: "))
print("Баланс:", acc.get_balance(entered_pin))
print("\n--- Смена PIN ---")
old_pin = int(input("Введите старый PIN: "))
new_pin = int(input("Введите новый PIN: "))
acc.change_pin(old_pin, new_pin)
print("\nПроверка баланса с новым PIN.")
entered_pin = int(input("Введите новый PIN: "))
print("Баланс:", acc.get_balance(entered_pin))


class UserProfile:
    def __init__(self, email, password, status="free"):
        self.__email = email
        self.__password = password
        self._status = status
        self.__logged_in = False
    def login(self, email, password):
        if email == self.__email and password == self.__password:
            self.__logged_in = True
            print("Вход выполнен успешно.")
        else:
            print("Ошибка: неверный логин или пароль.")
    def upgrade_to_premium(self):
        if self.__logged_in:
            self._status = "premium"
            print("Аккаунт обновлён до премиум.")
        else:
            print("Ошибка: выполните вход перед обновлением.")
    def get_info(self):
        if self.__logged_in:
            print(f"Email: {self.__email}, Статус: {self._status}")
        else:
            print("Ошибка: доступ запрещён (вход не выполнен).")
user = UserProfile("user@example.com", "12345")
user.get_info()
user.login("user@example.com", "12345")
user.upgrade_to_premium()
user.get_info()


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.__discount = 0
    def set_discount(self, discount, is_admin=False):
        if is_admin and 0 <= discount <= 100:
            self.__discount = discount
            print(f"Скидка {discount}% установлена.")
        else:
            print("Ошибка: нет прав администратора или неверная скидка.")
    def get_price(self):
        return self.price * (1 - self.__discount / 100)
p = Product("Телефон", 1000)
print("Цена без скидки:", p.get_price())
p.set_discount(20, is_admin=True)
print("Цена со скидкой:", p.get_price())


class TextFile:
    def open(self):
        print("Открыт текстовый файл. Отображение содержимого...")
class ImageFile:
    def open(self):
        print("Открыт файл изображения. Показ картинки...")
class AudioFile:
    def open(self):
        print("Открыт аудиофайл. Воспроизведение звука...")
def open_all(files):
    for f in files:
        f.open()
files = [TextFile(), ImageFile(), AudioFile()]
open_all(files)


class Car:
    def move(self, distance):
        speed = 100
        time = distance / speed
        print(f"Машина проедет {distance} км за {time:.2f} ч.")
class Truck:
    def move(self, distance):
        speed = 60
        time = distance / speed
        print(f"Грузовик проедет {distance} км за {time:.2f} ч.")
class Bicycle:
    def move(self, distance):
        speed = 20
        time = distance / speed
        print(f"Велосипед проедет {distance} км за {time:.2f} ч.")
def simulate_transport(transport_list, distance):
    for t in transport_list:
        t.move(distance)
transport_list = [Car(), Truck(), Bicycle()]
simulate_transport(transport_list, 120)


class Student:
    def access_portal(self):
        print("Студент: доступ к расписанию и оценкам.")
class Teacher:
    def access_portal(self):
        print("Преподаватель: доступ к выставлению оценок.")
class Administrator:
    def access_portal(self):
        print("Администратор: доступ к управлению пользователями.")
users = [Student(), Teacher(), Administrator()]
for u in users:
    u.access_portal()
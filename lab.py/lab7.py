class Animal:
    def __init__(self, name, age, habitat):
        self.name = name
        self.age = age
        self.habitat = habitat
    def info(self):
        return f"{self.name}, {self.age}, проживает в {self.habitat}"
class mammal(Animal):
    def __init__(self, name, age, habitat, fur_color):
        super().__init__(name, age, habitat)
        self.fur_color = fur_color
    def feed_milk(self):
        return f"{self.name} кормит молоком."
    def info(self):
        return f"{super().info()}, цвет щерсти: {self.fur_color}"
class reptile(Animal):
    def __init__(self, name, age, habitat, scales):
        super().__init__(name, age, habitat)
        self.scales = scales
    def lays_eggs(self):
        return f"{self.name} откладывает яйца"
    def info(self):
        return f"{super().info()} чешуя: {self.scales}:"
lion = mammal("Льыица", "5", "Саванна", "золотистая")
crocodile = reptile("Крокодил", "10", "река Амазонка", "грубая")
print(lion.info())
print(crocodile.info())


# Дополнительное задание

class ZooShow:
    def __init__(self):
        self.schedule = {
            "понедельник": {
                "name": "Шоу львов",
                "description": "Захватывающее шоу с участием львов, огненных колец и акробатов.",
                "price": 1000,
                "how_it_goes": "Львы прыгают через горящие кольца, сопровождаются выступлениями дрессировщиков и акробатов."
            },
            "среда": {
                "name": "Шоу крокодилов",
                "description": "Уникальная возможность увидеть крокодилов в команде с другими рептилиями.",
                "price": 2000,
                "how_it_goes": "Кормление крокодилов, демонстрация их силы и трюки с ящерицами и змеями."
            },
            "пятница": {
                "name": "Шоу обезьян",
                "description": "Обезьяны покажут интересные трюки, которые вы больше нигде не увидите.",
                "price": 1500,
                "how_it_goes": "Сценки, езда на мини-велосипедах и интерактив с детьми."
            }
        }
    def display_schedule(self):
        print("Расписание шоу в зоопарке:")
        for day, details in self.schedule.items():
            print(f"{day.capitalize()}: {details['name']} - {details['description']} (Цена: {details['price']} сом)")
    def get_show_details(self, day):
        day = day.lower()
        if day in self.schedule:
            details = self.schedule[day]
            return (
                f"\nДетали шоу в {day.capitalize()}:\n"
                f"Название: {details['name']}\n"
                f"Описание: {details['description']}\n"
                f"Цена: {details['price']} сом\n"
                f"Как проходит: {details['how_it_goes']}"
            )
        else:
            return "В этот день шоу не проводится."
day = input("Введите день недели (Понедельник, Среда, Пятница): ")
zoo = ZooShow()
zoo.display_schedule()
print(zoo.get_show_details(day))
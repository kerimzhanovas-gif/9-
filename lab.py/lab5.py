flags = {
    'ru': {'red', 'blue', 'white'},
    'kg': {'red', 'yellow'},
    'ua': {'red', 'blue'},
    'uk': {'yellow', 'blue'},
    'kz': {'blue', 'yellow'},
    'jp': {'white', 'red'},
    'kr': {'white', 'red', 'blue', 'black'},
    'cn': {'red', 'yellow'}
}
while True:
    colors = input("Введите цвета флагов или напишите 'выход':")
    if colors == "выход":
        print("Конец программы.")
        break
    colors_set = set(colors.split())
    print("Подходящие флаги:")
    for key, value in flags.items():
        if colors_set.issubset(value):
            print(key)
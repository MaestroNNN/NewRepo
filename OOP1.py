class Invention:
    def __init__(self, name, scientist, year):
        self.name = name
        self.scientist = scientist
        self.year = year

    def print_to_file(self, file):
        file.write(f"{self.name:<30} {self.scientist:<30} {self.year:<4d}\n")

inventions = []
inventions.append(Invention("Телефон", "Александр Грэм Белл", 1876))
inventions.append(Invention("Электрическая лампа", "Томас Эдисон", 1879))
inventions.append(Invention("Радио", "Гуглиельмо Маркони", 1895))
inventions.append(Invention("Телевидение", "Джон Логи Бэрд", 1927))
inventions.append(Invention("Компьютер", "Конрад Цузе", 1941))
inventions.append(Invention("Микросхема", "Джек Килби", 1958))
inventions.append(Invention("Интернет", "Винтон Серф", 1969))
inventions.append(Invention("Мобильный телефон", "Мартин Купер", 1973))
inventions.append(Invention("Персональный компьютер", "Стивен Джобс", 1976))
inventions.append(Invention("Глобальная позиционная система (GPS)", "Роджер Л. Истон", 1978))
inventions.append(Invention("Интернет-браузер", "Тим Бернерс-Ли", 1990))
inventions.append(Invention("Социальная сеть", "Марк Цукерберг", 2004))

# Сортировка массива по полю year
inventions.sort(key=lambda x: x.year)

# Запись в файл
try:
    with open("OOP1 sortirovka.txt", "w") as file:
        file.write("Name                          Scientist                      Year\n")
        file.write("--------------------------------------------------------------\n")
        for invention in inventions:
            invention.print_to_file(file)

        file.write("\n")

        # Сортировка массива по полю name
        inventions.sort(key=lambda x: x.name)

        for invention in inventions:
            invention.print_to_file(file)
except FileNotFoundError as e:
    print(e)
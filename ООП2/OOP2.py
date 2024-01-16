import tkinter as tk

class CoffeeCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Coffee Cost Calculator")

        # Настройка переменных для хранения значений
        self.coffee_type = tk.StringVar()
        self.sugar = tk.IntVar()
        self.cream = tk.IntVar()
        self.cups = tk.IntVar()
        self.total_cost = tk.StringVar()

        # Создание элементов интерфейса
        tk.Label(root, text="Выберите тип кофе:").pack()
        self.coffee_combo = tk.OptionMenu(root, self.coffee_type, "Эспрессо", "Латте", "Капучино")
        self.coffee_combo.pack()

        tk.Label(root, text="Количество чашек:").pack()
        tk.Entry(root, textvariable=self.cups).pack()

        tk.Label(root, text="Сахар (количество ложек):").pack()
        tk.Entry(root, textvariable=self.sugar).pack()

        tk.Label(root, text="Сливки (мл):").pack()
        tk.Entry(root, textvariable=self.cream).pack()

        tk.Button(root, text="Рассчитать", command=self.calculate_cost).pack()

        tk.Label(root, text="Итоговая стоимость:").pack()
        tk.Label(root, textvariable=self.total_cost).pack()

    def calculate_cost(self):
        # Выполнение расчетов
        coffee_price = {"Эспрессо": 2, "Латте": 3, "Капучино": 3.5}
        sugar_cost = 0.1 * self.sugar.get()
        cream_cost = 0.15 * self.cream.get()
        total = (coffee_price[self.coffee_type.get()] * self.cups.get()) + sugar_cost + cream_cost

        # Обновление текста для отображения итоговой стоимости
        self.total_cost.set("${:.2f}".format(total))

if __name__ == "__main__":
    root = tk.Tk()
    app = CoffeeCalculator(root)
    root.mainloop()

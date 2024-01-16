class Calculator:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.result = 0

    def calculate(self):
        try:
            if not (isinstance(self.a, (int, float)) and isinstance(self.b, (int, float))):
                raise ValueError("Ошибка - введите корректные числа")
                
            if self.c not in ['+', '-', '*', '/']:
                raise ValueError("Ошибка - неверный оператор")

            if self.c == '+':
                self.result = self.a + self.b
            elif self.c == '-':
                self.result = self.a - self.b
            elif self.c == '*':
                self.result = self.a * self.b
            elif self.c == '/':
                if self.b == 0:
                    raise ZeroDivisionError("Ошибка - деление на ноль")
                self.result = self.a / self.b

        except (ValueError, ZeroDivisionError) as e:
            print(e)
            return None

        return self.result


def main():
    try:
        a = float(input("Введите первое число: "))
        b = float(input("Введите второе число: "))
        c = input("Введите оператор (+, -, *, /): ")

        calculator = Calculator(a, b, c)
        result = calculator.calculate()

        if result is not None:
            print(f"Результат: {result}")
            
    except ValueError:
        print("Ошибка - введите числа в правильном формате")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


if __name__ == "__main__":
    main()
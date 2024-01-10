class IOperation:
    def get_sign(self):
        pass

    def get_name(self):
        pass

    def estimate(self, a, b):
        pass


class Division(IOperation):
    def get_sign(self):
        return "DIV"

    def get_name(self):
        return "Целочисленное деление"

    def estimate(self, a, b):
        return a // b


class Modulo(IOperation):
    def get_sign(self):
        return "MOD"

    def get_name(self):
        return "Целочисленный остаток"

    def estimate(self, a, b):
        return a % b


class GCD(IOperation):
    def get_sign(self):
        return "НОД"

    def get_name(self):
        return "Наибольший общий делитель"

    def estimate(self, a, b):
        while b:
            a, b = b, a % b
        return a


class LCM(IOperation):
    def get_sign(self):
        return "НОК"

    def get_name(self):
        return "Наименьшее общее кратное"

    def estimate(self, a, b):
        gcd = self.calculate_gcd(a, b)
        return abs(a * b) // gcd

    def calculate_gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a


operations = [Division(), Modulo(), GCD(), LCM()]
a = 120
b = 24

for op in operations:
    print(op.get_name())
    print(f"{a} {op.get_sign()} {b} = {op.estimate(a, b)}")

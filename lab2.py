class RationalNumber:
    def __init__(self, numerator, denominator):
        self.numerator = numerator  # числитель
        self.denominator = denominator  # знаменатель

    def simplify(self):
        # Находим наибольший общий делитель числителя и знаменателя
        gcd = self.gcd(self.numerator, self.denominator)
        # Упрощаем дробь, деля числитель и знаменатель на их НОД
        self.numerator = self.numerator // gcd
        self.denominator = self.denominator // gcd

    @staticmethod
    def gcd(a, b):  #НОД
        while b != 0:
            a, b = b, a % b
        return a

    def __add__(self, other):
        # a/b + c/d = (a * d + b * c) / (b * d)
        numerator = self.numerator * other.denominator + self.denominator * other.numerator
        denominator = self.denominator * other.denominator
        result = RationalNumber(numerator, denominator)
        result.simplify()
        return result

    def __sub__(self, other):
        # a/b - c/d = (a * d - b * c) / (b * d)
        numerator = self.numerator * other.denominator - self.denominator * other.numerator
        denominator = self.denominator * other.denominator
        result = RationalNumber(numerator, denominator)
        result.simplify()
        return result

    def __mul__(self, other):
        # (a/b) * (c/d) = (a * c) / (b * d)
        numerator = self.numerator * other.numerator
        denominator = self.denominator * other.denominator
        result = RationalNumber(numerator, denominator)
        result.simplify()
        return result

    def __truediv__(self, other):
        numerator = self.numerator * other.denominator
        denominator = self.denominator * other.numerator
        result = RationalNumber(numerator, denominator)
        result.simplify()
        return result

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"


fraction1 = RationalNumber(2, 4)
fraction2 = RationalNumber(3, 6)


# Упрощение:
fraction1.simplify()
print(f"Упрощение: {fraction1}")

# Сложение:
result_sum = fraction1 + fraction2
print(f"Сумма: {result_sum}")

# Вычитание:
result_diff = fraction1 - fraction2
print(f"Разность: {result_diff}")

# Умножение:
result_mul = fraction1 * fraction2
print(f"Умножение: {result_mul}")

# Деление:
result_div = fraction1 / fraction2
print(f"Деление: {result_div}")

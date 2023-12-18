class RationalNumber:
    def __init__(self, numerator, denominator):
        self.__numerator = numerator
        self.__denominator = denominator

    def simplify(self):
        gcd = self.__gcd(self.__numerator, self.__denominator)
        self.__numerator //= gcd
        self.__denominator //= gcd

    @staticmethod
    def __gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    def get_numerator(self):
        return self.__numerator

    def set_numerator(self, numerator):
        if isinstance(numerator, int):
            self.__numerator = numerator
        else:
            print("Numerator must be an integer.")

    def get_denominator(self):
        return self.__denominator

    def set_denominator(self, denominator):
        if isinstance(denominator, int) and denominator != 0:
            self.__denominator = denominator
        else:
            print("Denominator must be a non-zero integer.")

    def __add__(self, other):
        numerator = self.__numerator * other.get_denominator() + self.__denominator * other.get_numerator()
        denominator = self.__denominator * other.get_denominator()
        result = RationalNumber(numerator, denominator)
        result.simplify()
        return result

    def __sub__(self, other):
        numerator = self.__numerator * other.get_denominator() - self.__denominator * other.get_numerator()
        denominator = self.__denominator * other.get_denominator()
        result = RationalNumber(numerator, denominator)
        result.simplify()
        return result

    def __mul__(self, other):
        numerator = self.__numerator * other.get_numerator()
        denominator = self.__denominator * other.get_denominator()
        result = RationalNumber(numerator, denominator)
        result.simplify()
        return result

    def __truediv__(self, other):
        numerator = self.__numerator * other.get_denominator()
        denominator = self.__denominator * other.get_numerator()
        result = RationalNumber(numerator, denominator)
        result.simplify()
        return result

    def __str__(self):
        return f"{self.__numerator}/{self.__denominator}"


fraction1 = RationalNumber(2, 4)
fraction2 = RationalNumber(3, 6)

fraction1.simplify()
print(f"Упрощение: {fraction1}")

# Примеры с корректными и некорректными данными
fraction1.set_numerator(5)
fraction1.set_denominator(2)
fraction1.set_denominator(0)  # Некорректное значение, будет выведено сообщение

result_sum = fraction1 + fraction2
print(f"Сумма: {result_sum}")

result_diff = fraction1 - fraction2
print(f"Разность: {result_diff}")

result_mul = fraction1 * fraction2
print(f"Умножение: {result_mul}")

result_div = fraction1 / fraction2
print(f"Деление: {result_div}")

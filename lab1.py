class Base:
    def __init__(self, point, step):
        self.__point = point  # инкапсулированный атрибут
        self.__step = step    # инкапсулированный атрибут

    def calc(self):
        pass

    # методы для доступа к закрытым атрибутам
    def get_point(self):
        return self.__point

    def get_step(self):
        return self.__step


class LeftDiff(Base):
    def calc(self, function):
        result = (function(self.get_point() + self.get_step()) - function(self.get_point())) / self.get_step()
        return result


class RightDiff(Base):
    def calc(self, function):
        result = (function(self.get_point()) - function(self.get_point() - self.get_step())) / self.get_step()
        return result


class MidDiff(Base):
    def calc(self, function):
        result = (function(self.get_point() + self.get_step()) - function(self.get_point() - self.get_step())) / (
                2 * self.get_step())
        return result


def power_function(x):
    return x ** 2


left = LeftDiff(1, 0.001)
right = RightDiff(1, 0.001)
mid = MidDiff(1, 0.001)
print(left.calc(power_function))
print(right.calc(power_function))
print(mid.calc(power_function))

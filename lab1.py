class Base:
    def __init__(self, point, step):
        self.point = point
        self.step = step

    def calc(self):
        pass


class LeftDiff(Base):
    def calc(self, function):
        result = (function(self.point + self.step) - function(self.point)) / self.step
        return result


class RightDiff(Base):
    def calc(self, function):
        result = (function(self.point) - function(self.point - self.step)) / self.step
        return result


class MidDiff(Base):
    def calc(self, function):
        result = (function(self.point + self.step) - function(self.point - self.step)) / (2 * self.step)
        return result


def power_function(x):
    return x ** 2


left = LeftDiff(1, 0.001)
right = RightDiff(1, 0.001)
mid = MidDiff(1, 0.001)
print(left.calc(power_function))
print(right.calc(power_function))
print(mid.calc(power_function))

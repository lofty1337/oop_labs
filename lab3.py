class Array3d:
    def __init__(self, dim0, dim1, dim2, default_value=0):
        self._dim0 = dim0
        self._dim1 = dim1
        self._dim2 = dim2
        self.array = [default_value] * (dim0 * dim1 * dim2)

    @property
    def dim0(self):
        return self._dim0

    @property
    def dim1(self):
        return self._dim1

    @property
    def dim2(self):
        return self._dim2

    def get_index(self, i, j, k):
        return i * (self.dim1 * self.dim2) + j * self.dim2 + k

    def __getitem__(self, indices):
        i, j, k = indices
        return self.array[self.get_index(i, j, k)]

    def __setitem__(self, indices, value):
        i, j, k = indices
        self.array[self.get_index(i, j, k)] = value

    def print_array(self):
        for i in range(self.dim0):
            for j in range(self.dim1):
                for k in range(self.dim2):
                    print(self[i, j, k], end=" ")
                print()
            print()

    def zeroes(self):
        self.array = [0] * (self.dim0 * self.dim1 * self.dim2)

    def fill(self, value):
        self.array = [value] * (self.dim0 * self.dim1 * self.dim2)

    def ones(self):
        self.array = [1] * (self.dim0 * self.dim1 * self.dim2)

    def get_values_0(self, i):
        if 0 <= i < self.dim0:
            return [self[i, j, k] for j in range(self.dim1) for k in range(self.dim2)]
        else:
            print("wrong index")

    def get_values_1(self, j):
        if 0 <= j < self.dim1:
            return [self[i, j, k] for i in range(self.dim0) for k in range(self.dim2)]
        else:
            print("wrong index")

    def get_values_2(self, k):
        if 0 <= k < self.dim2:
            return [self[i, j, k] for i in range(self.dim0) for j in range(self.dim1)]
        else:
            print("wrong index")

    def get_values_01(self, i, j):
        if 0 <= i < self.dim0 and 0 <= j < self.dim1:
            return [self[i, j, k] for k in range(self.dim2)]
        else:
            print("wrong index")

    def get_values_02(self, i, k):
        if 0 <= i < self.dim0 and 0 <= k < self.dim2:
            return [self[i, j, k] for j in range(self.dim1)]
        else:
            print("wrong index")

    def get_values_12(self, j, k):
        if 0 <= j < self.dim1 and 0 <= k < self.dim2:
            return [self[i, j, k] for i in range(self.dim0)]
        else:
            print("wrong index")

    def set_values_0(self, i, values):
        if 0 <= i < self.dim0:
            if len(values) == self.dim1 * self.dim2:
                count = 0
                for j in range(self.dim1):
                    for k in range(self.dim2):
                        self[i, j, k] = values[count]
                        count += 1
            else:
                print("wrong array size")
        else:
            print("wrong index")

    def set_values_1(self, j, values):
        if 0 <= j < self.dim1:
            if len(values) == self.dim0 * self.dim2:
                count = 0
                for i in range(self.dim0):
                    for k in range(self.dim2):
                        self[i, j, k] = values[count]
                        count += 1
            else:
                print("wrong array size")
        else:
            print("wrong index")

    def set_values_2(self, k, values):
        if 0 <= k < self.dim2:
            if len(values) == self.dim0 * self.dim1:
                count = 0
                for i in range(self.dim0):
                    for j in range(self.dim1):
                        self[i, j, k] = values[count]
                        count += 1
            else:
                print("wrong array size")
        else:
            print("wrong index")

    def set_values_01(self, i, j, values):
        if 0 <= i < self.dim0 and 0 <= j < self.dim1:
            if len(values) == self.dim2:
                count = 0
                for k in range(self.dim2):
                    self[i, j, k] = values[count]
                    count += 1
            else:
                print("wrong array size")
        else:
            print("wrong index")

    def set_values_02(self, i, k, values):
        if 0 <= i < self.dim0 and 0 <= k < self.dim2:
            if len(values) == self.dim1:
                count = 0
                for j in range(self.dim1):
                    self[i, j, k] = values[count]
                    count += 1
            else:
                print("wrong array size")
        else:
            print("wrong index")

    def set_values_12(self, j, k, values):
        if 0 <= j < self.dim1 and 0 <= k < self.dim2:
            if len(values) == self.dim0:
                count = 0
                for i in range(self.dim0):
                    self[i, j, k] = values[count]
                    count += 1
            else:
                print("wrong array size")
        else:
            print("wrong index")

# Пример использования:
array3d = Array3d(2, 3, 4)

count = 0
for i in range(2):
    for j in range(3):
        for k in range(4):
            array3d[i, j, k] = count
            count += 1
# Вывод всего массива
array3d.print_array()

print(array3d.get_values_0(0))
print(array3d.get_values_0(1))
print(array3d.get_values_1(0))
print(array3d.get_values_1(1))
print(array3d.get_values_1(2))
print(array3d.get_values_2(0))
print(array3d.get_values_2(1))
print(array3d.get_values_2(2))
print(array3d.get_values_2(3))
print(array3d.get_values_01(0, 0))
print(array3d.get_values_02(0, 0))
print(array3d.get_values_12(0, 0))
arr_0=[66+i for i in range(12)]
array3d.set_values_0(0, arr_0)
print(array3d.get_values_0(0))
arr_12=[13, 37]
array3d.set_values_12(0, 0, arr_12)
print(array3d.get_values_12(0, 0))
wrong_array = [0 for i in range(100)]
array3d.set_values_12(0, 0, wrong_array)
array3d.fill(1337)
array3d.print_array()
array3d.zeroes()
array3d.print_array()

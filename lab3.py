import numpy as np


class Array3d:
    def __init__(self, dim0, dim1, dim2):
        self.__dim0 = dim0
        self.__dim1 = dim1
        self.__dim2 = dim2
        self.__data = np.zeros(dim0 * dim1 * dim2)

    def __getitem__(self, indices):
        i, j, k = indices
        idx = i * self.__dim1 * self.__dim2 + j * self.__dim2 + k
        return self.__data[idx]

    def __setitem__(self, indices, value):
        i, j, k = indices
        idx = i * self.__dim1 * self.__dim2 + j * self.__dim2 + k
        self.__data[idx] = value

    def get_values_0(self, i):
        return [self.__data[i * self.__dim1 * self.__dim2 + j * self.__dim2 + k]
                for j in range(self.__dim1)
                for k in range(self.__dim2)]

    def get_values_1(self, j):
        return [self.__data[i * self.__dim1 * self.__dim2 + j * self.__dim2 + k]
                for i in range(self.__dim0)
                for k in range(self.__dim2)]

    def get_values_2(self, k):
        return [self.__data[i * self.__dim1 * self.__dim2 + j * self.__dim2 + k]
                for i in range(self.__dim0)
                for j in range(self.__dim1)]

    def get_values_01(self, i, j):
        return [self.__data[i * self.__dim1 * self.__dim2 + j * self.__dim2 + k]
                for k in range(self.__dim2)]

    def get_values_02(self, i, k):
        return [self.__data[i * self.__dim1 * self.__dim2 + j * self.__dim2 + k]
                for j in range(self.__dim2)]

    def get_values_12(self, j, k):
        return [self.__data[i * self.__dim1 * self.__dim2 + j * self.__dim2 + k]
                for i in range(self.__dim0)]

    def set_values_0(self, i, values):
        for j in range(self.__dim1):
            for k in range(self.__dim2):
                self.__data[i * self.__dim1 * self.__dim2 + j * self.__dim2 + k] = values[j * self.__dim2 + k]

    def set_values_1(self, j, values):
        for i in range(self.__dim1):
            for k in range(self.__dim2):
                self.__data[i * self.__dim1 * self.__dim2 + j * self.__dim2 + k] = values[j * self.__dim2 + k]

    def set_values_2(self, k, values):
        for i in range(self.__dim0):
            for j in range(self.__dim1):
                self.__data[i * self.__dim1 * self.__dim2 + j * self.__dim2 + k] = values[j * self.__dim1 + j]

    def set_values_01(self, i, j, values):
        for k in range(self.__dim2):
            self.__data[i * self.__dim1 * self.__dim2 + j * self.__dim2 + k] = values[k]

    def set_values_02(self, i, k, values):
        for j in range(self.__dim1):
            self.__data[i * self.__dim1 * self.__dim2 + j * self.__dim2 + k] = values[j]

    def set_values_12(self, j, k, values):
        for i in range(self.__dim0):
            self.__data[i * self.__dim1 * self.__dim2 + j * self.__dim2 + k] = values[i]


def create_array_with_same_elements(dim0, dim1, dim2, value):
    return np.full((dim0, dim1, dim2), value)


def create_array_with_zeroes(dim0, dim1, dim2):
    return np.zeros((dim0, dim1, dim2))


def create_array_with_ones(dim0, dim1, dim2):
    return np.ones((dim0, dim1, dim2))


arr = Array3d(3, 4, 2)
arr[0, 1, 1] = 5
print(f"arr[0, 1, 1]: {arr[0, 1, 1]}")

values0 = arr.get_values_0(1)
print(f"values0: {values0}")

values1 = arr.get_values_1(2)
print(f"values1: {values1}")

values2 = arr.get_values_2(0)
print(f"values2: {values2}")

values01 = arr.get_values_01(0, 1)
print(f"values01: {values01}")

values02 = arr.get_values_02(0, 0)
print(f"values02: {values02}")

values12 = arr.get_values_12(1, 1)
print(f"values12: {values12}")

arr.set_values_0(1, [1, 2, 3, 4, 5, 6, 7, 8])
print(f"arr[1, 0, 0]: {arr[1, 0, 0]}")
print(f"arr[1, 1, 1]: {arr[1, 1, 1]}")

array_same_elements = create_array_with_same_elements(2, 3, 4, 0.5)
print(f"same elements array:\n{array_same_elements}")

from random import randint

array = [i for i in range(1990)]
array[673] = 672


def binarySearch(
    array: list[int], element: int, start: int = 0, end: int = len(array) - 1
):
    if start > end:
        return -1

    mid = (start + end) // 2

    if array[mid] == element:
        return mid

    if array[mid] > element:
        return binarySearch(array, element, start, mid - 1)
    elif array[mid] < element:
        return binarySearch(array, element, mid + 1, end)


def interpolationSearch(
    array: list[int], element: int, start: int = 0, end: int = len(array) - 1
):
    if start > end:
        return -1

    mid = start + ((element - array[start]) * (end - start)) // (
        array[end] - array[start]
    )

    if array[mid] == element:
        return mid
    if array[mid] > element:
        return interpolationSearch(array, element, start, mid - 1)
    if array[mid] < element:
        return interpolationSearch(array, element, mid + 1, end)


def fibonacciSearch(array: list[int], element: int):
    offset = 0
    fibMm2 = 0
    fibMm1 = 1
    fibM = fibMm2 + fibMm1

    while fibM < len(array):
        fibMm2 = fibMm1
        fibMm1 = fibM
        fibM = fibMm2 + fibMm1

    while fibM >= 0:
        index = fibMm2 + offset

        if index < len(array) and array[index] == element:
            return fibMm2 + offset
        if index >= len(array) or array[index] < element:
            if index < len(array):  # do NOT change offset when edge case (right corner)
                offset = offset + fibMm2
            fibM = fibMm1
            fibMm1 = fibMm2
            fibMm2 = fibM - fibMm1
            continue
        if array[fibMm2 + offset] > element:
            if fibMm1 == fibMm2:  # edge case (left corner)
                fibM = 1
                fibMm1 = 1
                fibMm2 = 0
            else:
                fibMm1 = fibMm1 - fibMm2
                fibMm2 = fibMm2 - fibMm1
                fibM = fibMm1 + fibMm2
            continue
    return -1


class BTSNode:
    def __init__(self, value: int, index: int | set[int] = None) -> None:
        self.left = None
        self.right = None
        self.value = value
        if type(index) is set:
            self.index = index
        elif type(index) is int:
            self.index = {index}

    def insert(self, other):
        if self == other:
            self.index.update(other.index)
            return
        if other < self:
            if self.left is not None:
                self.left.insert(other)
                return
            self.left = other
        else:
            if self.right is not None:
                self.right.insert(other)
                return
            self.right = other

    def __eq__(self, other):
        if type(other) is BTSNode:
            return self.value == other.value
        return False

    def __lt__(self, other):
        if type(other) is BTSNode:
            return self.value < other.value
        return False

    def __gt__(self, other):
        if type(other) is BTSNode:
            return self.value > other.value
        return False

    def search(self, other):
        if self == other:
            return self
        if self.right is not None and other > self:
            return self.right.search(other)
        if self.left is not None and other < self:
            return self.left.search(other)
        return None


class BTS:
    def __init__(self, array: list[int | float]) -> None:
        self.array = sorted(array)
        self.middle = len(self.array) // 2
        self.tree = BTSNode(self.array[self.middle], self.middle)

        for index, element in enumerate(self.array):
            self.tree.insert(BTSNode(element, index))

    def search(self, value: int | float):
        search_result = self.tree.search(BTSNode(value, 0))
        if search_result is not None:
            return search_result.index
        return None


searchIndex = 672

print(binarySearch(array, array[searchIndex]))
print(interpolationSearch(array, array[searchIndex]))
print(fibonacciSearch(array, 1000000))
print(fibonacciSearch(array, 999999))
print(fibonacciSearch(array, 999998))
print(fibonacciSearch(array, array[searchIndex]))
print(fibonacciSearch(array, 0))
print(fibonacciSearch(array, 1))
print(fibonacciSearch(array, -1))
bts = BTS(array)
print(bts.search(array[searchIndex]))

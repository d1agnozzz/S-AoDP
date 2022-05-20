from asyncio import current_task
from random import randint
import math
import time
import os


def generateMatrix(m=50, n=50, min_limit=-250, max_limit=1000):
    matrix = [[randint(min_limit, max_limit) for i in range(n)] for j in range(m)]
    return matrix


b = generateMatrix(10, 10)
# b = [[13, 6, 46, 13, 2, 15, 26, 34, 31]]


def matrix2str(matrix):
    rows = ""
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            rows += "\t" + str(matrix[i][j])
        rows += "\n"
    return rows


def selectionSort(array):
    size = len(array)
    for i in range(size):
        minInd = i
        for j in range(i + 1, size):
            if array[j] < array[minInd]:
                minInd = j
        array[i], array[minInd] = array[minInd], array[i]
    return array


def insertionSort(array):
    size = len(array)

    for iter in range(2, size):
        currentInd = iter
        currentVal = array[iter]
        while currentInd > 0 and currentVal < array[currentInd - 1]:
            array[currentInd], array[currentInd - 1] = (
                array[currentInd - 1],
                array[currentInd],
            )
            currentInd -= 1
    return array


def bubbleSort(array):
    size = len(array)
    for iter in range(size):
        for i in range(0, size - iter - 1):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
    return array


def shellSort(array):
    size = len(array)
    step = size // 2
    while step > 0:
        for iter in range(step, size):
            currentInd = iter
            delta = currentInd - step
            while delta >= 0 and array[delta] > array[currentInd]:
                array[delta], array[currentInd] = array[currentInd], array[delta]
                currentInd = step
                delta = currentInd - step
        step //= 2
    return array


def quickSort(array):
    if len(array) <= 1:
        return array

    less = []
    equal = []
    more = []
    size = len(array)
    pivot = array[size // 2]
    for num in array:
        if num < pivot:
            less.append(num)
        elif num == pivot:
            equal.append(num)
        else:
            more.append(num)
    less = quickSort(less)
    more = quickSort(more)
    return less + equal + more


def heapify(array, length, i):
    maxInd = i
    l = 2 * i + 1  # left = 2*i + 1
    r = 2 * i + 2  # right = 2*i + 2

    if l < length and array[maxInd] < array[l]:
        maxInd = l
    if r < length and array[maxInd] < array[r]:
        maxInd = r
    if array[maxInd] > array[i]:
        array[i], array[maxInd] = array[maxInd], array[i]
        heapify(array, length, maxInd)
    return array


def heapSort(array):
    size = len(array)
    for i in range(size - 1, -1, -1):
        heapify(array, size, i)

    for i in range(size - 1, 0, -1):
        array[i], array[0] = array[0], array[i]
        heapify(array, i, 0)
    return array


def build(array, bracket, level, l, r):
    if l == r:
        bracket[level] = (array[l], level)
    else:
        mid = (l + r) // 2
        build(array, bracket, 2 * level, l, mid)
        build(array, bracket, (2 * level) + 1, mid + 1, r)
        if bracket[(2 * level) + 1][0] < bracket[2 * level][0]:
            bracket[level] = bracket[(2 * level) + 1]
        else:
            bracket[level] = bracket[2 * level]


def pop(bracket):
    result = bracket[1][0]
    index = bracket[1][1]
    bracket[index] = None
    while index > 1:
        index = index // 2
        if bracket[index * 2] is None:
            minimum = bracket[(index * 2) + 1]
        elif bracket[(index * 2) + 1] is None:
            minimum = bracket[index * 2]
        else:
            minimum = min(bracket[index * 2], bracket[(index * 2) + 1])
        if minimum == bracket[index]:
            break
        bracket[index] = minimum
    return result


def tournamentSort(array):
    size = len(array)
    rang = 2 ** (math.ceil(math.log2(size)) + 1)
    bracket = [None] * rang
    build(array, bracket, 1, 0, size - 1)
    sorted_array = [pop(bracket) for _ in range(size)]
    return sorted_array


# print(matrix2str(b))

for i in range(len(b)):
    b[i] = tournamentSort(b[i])

for i, s in enumerate(b):
    print("i: ", i, " s: ", s)


print(matrix2str(b))

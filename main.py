import resource, sys

resource.setrlimit(resource.RLIMIT_STACK, (2**29,-1))
sys.setrecursionlimit(10**6)


def buble_sort(data:list):
    """Сортировка пузырьком"""
    for i in range(len(data) - 1):
        for j in range(len(data) - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]

def shaker_sort(data):
    """Шейкерная сортировка"""
    up = range(len(data) - 1)
    while True:
        for indices in (up, reversed(up)):
            swapped = False
            for i in indices:
                if data[i] > data[i+1]:
                    data[i], data[i+1] =  data[i+1], data[i]
                    swapped = True
            if not swapped:
                return data

def selection_sort(data:list):
    """Сортировка выбором"""
    for i in range(len(data) - 1):
        smallest = i
        for j in range(i + 1, len(data)):
            if data[j] < data[smallest]:
                smallest = j
        data[i], data[smallest] = data[smallest], data[i]

def insertion_sort(data:list):
    """Сортировка вставкой"""
    for i in range(len(data)):
        temp = data[i]
        j = i - 1
        while (j >= 0 and temp < data[j]):
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = temp

def partition(data, start, end):
    pivot = data[start]
    i = start + 1
    j = end - 1

    while True:
        while (i <= j and data[i] <= pivot):
            i = i + 1
        while (i <= j and data[j] >= pivot):
            j = j - 1

        if i <= j:
            data[i], data[j] = data[j], data[i]
        else:
            data[start], data[j] = data[j], data[start]
            return j

def quick_sort(data:list, start, end):
    """Быстрая сортировка"""
    if end - start > 1:
        p = partition(data, start, end)
        quick_sort(data, start, p)
        quick_sort(data, p + 1, end)

def comb_sort(data:list):
    """Сортировка расческой"""
    gap = len(data)
    swaps = True
    while gap > 1 or swaps:
        gap = max(1, int(gap / 1.25))  # minimum gap is 1
        swaps = False
        for i in range(len(data) - gap):
            j = i + gap
            if data[i] > data[j]:
                data[i], data[j] = data[j], data[i]
                swaps = True


def write(d, num):
    names = 'buble_sort', 'shaker_sort', 'selection_sort', 'insertion_sort', 'quick_sort', 'comb_sort'
    for idx, sort_data in d.items():
        with open(f'logs/{names[idx]}', 'a') as txt:
            txt.write(f'{num}: {sort_data[1][-1]}')


from random import randint
from time import time

sorts = buble_sort, shaker_sort, selection_sort, insertion_sort, quick_sort, comb_sort
d = {i: ([], []) for i in range(len(sorts))}

for num_of_elem in range(10, 100, 1):
    data = [randint(1, 99999) for _ in range(num_of_elem)]

    for idx, sort in enumerate(sorts):
        args = (data[:], ) if sort != quick_sort else (data[:], 0, len(data))

        start = time()
        sort(*args)
        t = time() - start

        d[idx][0].append(num_of_elem)
        d[idx][1].append(t)
    write(d, num_of_elem)

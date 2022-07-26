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
    alg = ('', 'buble_sort', 'shaker_sort', 'selection_sort', 'insertion_sort', 'quick_sort', 'comb_sort')
    for i in range(1, 6+1):
        with open(f'res\\{alg[i]}.txt', 'a') as txt:
            txt.write(f'{num}: {str(d[i][1][-1])} \n')


from random import randint
from time import time
import numpy as np
from matplotlib import pyplot as plt

dict1 = {1: [[], []],
         2: [[], []],
         3: [[], []],
         4: [[], []],
         5: [[], []],
         6: [[], []]}

for num_of_elem in range(800000000, 800000000+1):
    data = [randint(1, 999999) for i in range(num_of_elem)]
    # a = data.copy()
    # b = data.copy()
    # c = data.copy()
    # d = data.copy()
    # e = data.copy()
    # f = data.copy()
    print(num_of_elem)
    for num_of_alg in range(5, 5+1):
        start = time()
        match num_of_alg:
            case 1:
                buble_sort(a)
            case 2:
                shaker_sort(b)
            case 3:
                selection_sort(c)
            case 4:
                insertion_sort(d)
            case 5:
                quick_sort(data, 0, len(data))
            case 6:
                comb_sort(f)
        stop = time()
        t = stop - start

        dict1[num_of_alg][0].append(num_of_elem)
        dict1[num_of_alg][1].append(t)
    # print(dict1)

    write(dict1, num_of_elem)

    # if num_of_elem % 10000 == 0:
        # plt.plot(dict1[1][0], dict1[1][1])
        # plt.plot(dict1[2][0], dict1[2][1])
        # plt.plot(dict1[3][0], dict1[3][1])
        # plt.plot(dict1[4][0], dict1[4][1])
        # plt.plot(dict1[5][0], dict1[5][1])
        # plt.plot(dict1[6][0], dict1[6][1])

        # plt.legend(('buble_sort', 'shaker_sort', 'selection_sort', 'insertion_sort', 'quick_sort', 'comb_sort'))
        # plt.savefig(f'res\\all_sort{num_of_elem}.png')
        # plt.close()

        # plt.plot(dict1[5][0], dict1[5][1])
        # plt.plot(dict1[6][0], dict1[6][1])
        # plt.legend(('quick_sort', 'comb_sort'))
        # plt.savefig(f'res\\2_sort{num_of_elem}.png')
        # plt.close()

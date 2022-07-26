import resource, sys
resource.setrlimit(resource.RLIMIT_STACK, (2**29,-1))
sys.setrecursionlimit(10**6)
def quick_sort(data:list, start, end):
    """Быстрая сортировка"""
    if end - start > 1:
        p = partition(data, start, end)
        quick_sort(data, start, p)
        quick_sort(data, p + 1, end)
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


from random import randint
import time
elem = 100000000
data = [randint(1, 9999999) for i in range(elem)]
start = time.time()
comb_sort(data)
stop = time.time()
print(f'time: {stop-start}')

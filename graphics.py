with open('buble_sort.txt') as file:
    buble_sort = file.readlines()
with open('comb_sort.txt') as file:
    comb_sort = file.readlines()
with open('insertion_sort.txt') as file:
    insertion_sort = file.readlines()
with open('quick_sort.txt') as file:
    quick_sort = file.readlines()
with open('selection_sort.txt') as file:
    selection_sort = file.readlines()
with open('shaker_sort.txt') as file:
    shaker_sort = file.readlines()


dict1 = {1: [[], []],
         2: [[], []],
         3: [[], []],
         4: [[], []],
         5: [[], []],
         6: [[], []]}

algs = [buble_sort, comb_sort, insertion_sort, quick_sort, selection_sort, shaker_sort]
for alg in range(6):
    for i in algs[alg]:
        element, time = i.split()
        dict1[alg+1][0].append(int(element[:-1]))
        dict1[alg+1][1].append(float(time))


from matplotlib import pyplot as plt
plt.plot(dict1[1][0], dict1[1][1])
plt.plot(dict1[2][0], dict1[2][1])
plt.plot(dict1[3][0], dict1[3][1])
plt.plot(dict1[4][0], dict1[4][1])
plt.plot(dict1[5][0], dict1[5][1])
plt.plot(dict1[6][0], dict1[6][1])
plt.legend(('buble_sort', 'comb_sort', 'insertion_sort', 'quick_sort', 'selection_sort', 'shaker_sort'))
plt.savefig('all_sort.png')
plt.close()

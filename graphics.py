names = ('buble_sort', 'comb_sort', 'insertion_sort',
         'quick_sort', 'selection_sort', 'shaker_sort')
files = (f'logs/{file}.txt' for file in names)
algs = [open(filename).readlines() for filename in files]

sortes_data = []
for alg in algs:
    sort_data = [], []
    for vals in alg:
        elem, time = vals.split()
        elem = int(elem[:-1])
        time = float(time)
        sort_data[0].append(elem)
        sort_data[1].append(time)
    sortes_data.append(sort_data)


from matplotlib import pyplot as plt

for sort_data in sortes_data:
    plt.plot(*sort_data)

plt.legend(names)
plt.show()
plt.savefig('graphics/all.png')
plt.close()

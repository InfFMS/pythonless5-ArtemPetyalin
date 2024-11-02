# При анализе данных, собранных в рамках научного эксперимента,
# бывает полезно удалить самое большое и самое маленькое значение.
# Сымитруем данные списком длины N со случайными числами в диапазоне от 0 до 1000
# Удалите из этого списка все значения, которые на 30 % отличаются
# от среднего значения списка

N = int(input())

def deleter(a):
    import random
    listus = [random.randint(0, 1000) for i in range(a)]
    sum = 0

    for t in range(len(listus)):
        sum += listus[t]

    sum = sum / len(listus)

    doubler_list = listus[::1]
    for k in range(len(listus)):

        if listus[k] / sum > 1.3 or listus[k] / sum < 0.7:
            doubler_list.remove(listus[k])

    return doubler_list

print(deleter(N))
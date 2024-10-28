# Заполнить массив длины N случайными числами в интервале [-100,100] и
# переставить элементы так, чтобы все положительные элементы
# стояли в начала массива, а все отрицательные и нули в конце.
# Пример: ввод N = 6
# [20, -90, 15, -34, 10, 0]
# Вывод: [20, 15, 10, -90, -34, 0]

N = int(input())

def poryadok(a):
    import random
    listus = []

    for i in range(a):
        p = random.randint(0,1)

        if p == 0:
            listus.append(random.randint(0,100) * (-1))

        else:
            listus.append(random.randint(0,100))

    result = []

    for t in range(a):

        if listus[t] > 0:
            result.append(listus[t])

    for k in range(a):

        if listus[k] < 0:
            result.append(listus[k])

    for s in range(a):

        if listus[s] == 0:
            result.append(listus[s])

    return result

print(poryadok(N))
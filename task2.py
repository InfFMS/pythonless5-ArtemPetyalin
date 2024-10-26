# Заполните массив длины N случайными числами в интервале [0,5].
# Определить, есть ли в нем элементы с одинаковыми значениями, стоящие рядом.
# Если есть, то выведете значение и индекс повторяющихся элементов
# Если нет, то написать "Нет"
# Пример: ввод N = 7
# [1, 2, 3, 3, 2, 2, 1]
# Вывод:
# значение:3 индексы 2 и 3
# значение:2 индексы 4 и 5

N = int(input())

def lister(a):
    import random
    list = []
    similars = []

    for i in range(a):
        list.append(random.randint(1, 5))

    for t in range(1, a):
        pair = []

        if list[t] == list[t - 1]:
            pair.append(t - 1)
            pair.append(t)
            pair.append(list[t])
            similars.append(pair)

    similars_of_similars = []

    for j in range(len(similars)):
        print('Значение: ' + str((similars[j])[2]) + ', индексы ' + str((similars[j])[0]) + ' и ' + str((similars[j])[1]))

lister(N)


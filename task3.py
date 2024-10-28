# Заполните массив длины N случайными числами в интервале [0,100].
# Определить, есть ли в нем элементы с одинаковыми значениями,
# не обязательно стоящие рядом.
# Если есть, то выведете значение и индекс повторяющихся элементов
# Если нет, то написать "Нет"
# Пример: ввод N = 6
# [1, 2, 3, 2, 5, 10]
# Вывод:
# значение:2 индексы 1 и 3
N = int(input())

def spisek(a):
    import random
    listium = [random.randint(0, 100) for i in range(a)]
    print('list:', listium)
    similars = []

    for t in range(101):
        sims = []

        for j in range(len(listium)):

            if listium[j] == t:
                sims.append(j)

        if len(sims) > 1:
            sims.append(t)
            similars.append(sims)

    for f in range(len(similars)):
        s = ''
        for k in range(len(similars[f]) - 1):
            s = s + str(similars[f][k]) + ', '

        s = s[:-2]
        print('Значение: ' + str(similars[f][-1]) + ', индексы: ' + s)


spisek(N)

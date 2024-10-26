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
    listium = [random.randint(0, 3) for i in range(a)]
    print(listium)
    similars = []

    doubler_list = listium[::-1]
    for n in range(len(listium) - 1):

        for t in range(n + 1, len(doubler_list)):
            sim_index = [n]

            if listium[n] == doubler_list[t]:
                sim_index.append(t)

            if t == len(doubler_list) - 1 and len(sim_index) != 1:
                sim_index.append(listium[n])
                similars.append(sim_index)

    print (similars)

    if len(similars) > 0:

        for m in range(len(similars)):
            a = [str((similars[m])[k]) for k in range(len((similars[m])) - 1)]
            print('Значение: ' + str((similars[m])[-1]) + ', индексы:', a)

    else:
        print('no equal nums')

spisek(N)

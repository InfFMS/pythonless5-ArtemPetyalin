# Напишите программу, которая удаляет дубликаты из списка длины N.
# Пример работы:
# Пример: ввод N = 8
# [10, 20, 10, 20, 30, 40, 30, 50]
# После удаления дублей:  [10, 20, 30, 40, 50]
from multiprocessing.connection import answer_challenge

N = int(input())

def no_sims(a):
    listus = [int(input()) for i in range(a)]
    black_list = []

    for t in range(len(listus)):
        counter = 0

        for k in range(t, len(listus)):

            if listus[t] == listus[k] and counter == 0:
                counter += 1

            elif listus[t] == listus[k] and counter != 0:
                black_list.append(listus[k])

    for p in range(len(black_list)):
        listus.remove(black_list[p])

    return listus

print(no_sims(N))
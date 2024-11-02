# Массив имеет четное число элементов N.
# Заполнить массив случайными числами и
# выполнить реверс отдельно в первой половине и второй половине.
# Пример: ввод N = 6
# [1,2,3,4,5,6]
# Вывод: [3,2,1,6,5,4]

N = int(input())

def reverser(a):
    import random
    listus = [random.randint(0,1000) for i in range(a)]
    print(listus)

#    list_1 = listus[:len(listus) // 2]
 #   print(list_1)
  #  list_2 = listus[len(listus) // 2: len(listus)]
    result = []

    for t in range(a // 2):
        result.append(listus[a // 2 - t - 1])

    for t in range(a // 2):
        result.append(listus[-1 - t])
    return result

print(reverser(N))
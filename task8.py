# Заполнить массив длины N случайными числами в диапазоне от 10 до 100000 и
# отобрать в другой массив все числа, которые состоят из одинаковых цифр.
# Используйте для этого логическую функцию.
# Пример: ввод N = 4
# [12, 77, 5555, 97]
# Вывод: [77, 5555]

N = int(input())

def sim_nums(a):
    import random
    listium = [random.randint(10, 100000) for i in range(a)]
    answer = []
    print(listium)

    def similarius(b):

        for k in range(len(str(b))):

            if b % 10 == b // 10 % 10:
                b = b // 10
                similarius(b)

            elif b // 10 == 0:
                return True

            else:
                return False

    for t in range(a):
        c = listium[t]

        if similarius(c) == True:
            answer.append(c)

    return answer

print('Result:', sim_nums(N))



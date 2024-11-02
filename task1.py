# Заполните список длины N случайными числами в диапазоне от 0 до 1000
# Выведите:
# 1.длину списка;
# 2.последний элемент списка;
# 3.список в обратном порядке (вспоминаем срезы);
# 4.YES, если список содержит трехзначное число, состоящее из одинаковых цифр
# NO в противном случае;
# 5.список с удаленными первым и последним элементами.

N  = int(input())

def rand_list(a):
    import random
    list = []

    for i in range(a):
        list.append(random.randint(0, 1000))

    bool = ''

    for t in range(len(list)):
        if list[t] // 100 == list[t] // 10 - 10 * list[t] // 100 == list[t] % 10:
            bool = 'YES'
            break

    else:
        bool = 'NO'


    return len(list), list[-1], list[::-1], bool, list[1:-1]

print(rand_list(N))



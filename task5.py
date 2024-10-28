# Введите массив длины N с клавиатуры и найдите (за один проход)
# количество элементов, имеющих максимальное значение.

N = int(input())

def maxer(a):
    listium = []
    max_num = 0
    amount = 1

    for i in range(a):
        listium.append(int(input()))

        if listium[i] > max_num:
            max_num = listium[i]
            amount = 1

        elif listium[i] == max_num and max_num != 0:
            amount += 1

    return amount

print(maxer(N))

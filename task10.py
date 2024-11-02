# Посчитайте угол между двумя векторами размерности N.
# Примечание: Вспомните определение скалярного произведения.
# Изначально вектор заполните рандомными числами.
# Пример: N =3
# вектор a = [0, 1, 0]
# вектор b = [1, 0, 0]
# Угол = 90
import random
import math
N = int(input())

def vecs(n):

    vec_a = []
    vec_b = []
    scalar_vec_mult = 0
    len_a = 0
    len_b = 0

    for k in range(n):
        ai = random.randint(0, 100)
        bi = random.randint(0, 100)
        vec_a.append(ai)
        vec_b.append(bi)
        scalar_vec_mult += ai * bi
        len_a += ai ** 2
        len_b += bi ** 2

    len_a = len_a ** 0.5
    len_b = len_b ** 0.5
    ans = scalar_vec_mult / len_a / len_b
    ans = math.acos(ans)

    return vec_a, vec_b, ans

print(vecs(N))
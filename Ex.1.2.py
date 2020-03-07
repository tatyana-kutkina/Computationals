import math
import numpy as np
from scipy.misc import derivative

print('Даны функция: f(x) = sin(x)', '\n', 'отрезок: [0.5 , 1.5]', '\n', 'точка х: х = 1.05')
x = 1.05
a, b = 0.5, 1.5
print('Шаг интерполяции h = 0.1')
h = 0.1
print('Порядок интерполирования n = 4 ')
n = 4


def f(x):
    return round(math.sin(x), 5)


def delta(n, arr):
    diffs = [arr]
    for k in range(1, n + 1):
        arr1 = []
        for i in range(len(arr) - k):
            arr1.append(round(diffs[k - 1][i + 1] - diffs[k - 1][i], 5))
        diffs.append(arr1)
    return diffs


# считаем и печатаем таблицу разделенных разностей и таблицу значений
def table(n):
    arr = []
    print('{0:<4} {1:>11} {2:>11} {3:>11} {4:>11} {5:>11}'.format('x', 'f(x)', '\u0394y', '\u03942y', '\u03943y',
                                                                  '\u03944y'))
    for i in range(int((b - a) / h + 1)):
        arr.append(f(a + i * h))

    diffs = delta(n, arr)
    for j in range(len(arr)):
        print(round(a + j * h, 1), end=' ')
        # print('\t', arr[j], end=' ')
        for i in range(len(diffs)):
            if j < len(diffs[i]):
                print('\t', diffs[i][j], end=' ')
        print('')
    return diffs


def coefficient(n, t):
    coefs = [0] * (n + 2)
    coefs[0] = 1
    for i in range(1, n + 2):
        y = 1
        for j in range(1, i + 1):
            y *= (t - ((-1) ** j) * (j // 2)) / j
        coefs[i] = round(y, 5)
    return coefs


# считаем полином 4 порядка в узле из середины таблицы и печатаем результат
def polynomial(n, t, coefs):
    values = [0] * (n + 1)
    arr = []
    for i in range(7):
        arr.append(f(a + h * (i - 3)))

    diffs = delta(n, arr)

    '''for i in range(n + 1):
        print(diffs[i])'''

    values[0] = diffs[0][len(diffs[0]) // 2]
    for i in range(1, n + 1):
        y = coefs[i]
        y *= diffs[i][(len(diffs[0]) // 2) - (i // 2)]
        y = round(y, 5)
        values[i] = values[i - 1] + y

    for j in range(n + 1):
        print('{0:<9}  '.format(diffs[j][(len(diffs[0]) // 2) - (j // 2)]), end=" ")  # используемые разделенные разности
    print('используемые разделенные разности ')
    for j in range(n + 1):
        print('{0:<9} '.format(round(coefs[j] * diffs[j][(len(diffs[0]) // 2) - (j // 2)], 5)), end=" ")
    print('N_k * \u0394k(y0) ')
    return values


# оценка модуля производной
def estimate_mod_der(n):
    modules = [0] * (n + 1)
    modules[0] = abs(derivative(f,a, dx=1.0, n=1, order=n + 3))
    for i in range(1, n + 1):
        c = a
        d = a + i * h
        step = abs(c - d) / 50
        for k in np.arange(c + step, d, step):
            modules[i] = max(abs(derivative(f, k, dx=1.0, n=i + 1, order=n + 3)),
                             abs(derivative(f, k - step, dx=1.0, n=i + 1, order=n + 3)))
    return modules


def estimate_err(modules, coefs):
    est_errors = [0] * (n + 1)
    for i in range(n + 1):
        est_errors[i] = round(modules[i] * abs(coefs[i+1]) * h**(i+1),5)
    return est_errors


# main
t = (x - a) / h
print('{0:<9} {1:<9} {2:<9} {3:<9} {4:<9}'.format('0', '1', '2', '3', '4'))

coefs = coefficient(n, t)
for i in range(n + 1):
    print('{0:<9} '.format(coefs[i]), end=' ')  # печать коэффициентов полинома
print('')
# print('коэффициенты N_k полинома')
values = polynomial(n, t, coefs)

for j in range(n + 1):
    print('{0:<9}'.format(values[j]), end=' ')  # печать значений полинома
print('значения полинома')

for j in range(n + 1):
    print('{0:<9}'.format(round(f(x) - values[j], 5)), end=' ')  # печать фактической погрешности
print('фактическая погрешность')

modules = estimate_mod_der(n)
est_errors = estimate_err(modules, coefs)
for i in range(n + 1):
    print('{0:<9} '.format(est_errors[i]), end=' ')  # печать оценки погрешности
print( 'оценка погрешности')

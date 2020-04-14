import math


# вычисляем значение функции в точке х
def f(x):
    return round(math.e**(3*x), 5)


# вычисляем производную k порядка в точке х
def der(x, k):
    return round((3**k)*f(x), 5)


# числ. дифф. 1 порядка, погрешность O(h)
def num_diff_1_1(arr, h):
    values_1_1 = []
    for i in range(len(arr)):
        if i == len(arr) - 1:
            values_1_1.append(' ')
        else:
            values_1_1.append(round((arr[i + 1] - arr[i]) / h, 5))
    return values_1_1


# числ. дифф. 1 порядка, погрешность O(h^2)
def num_diff_1_2(arr, h):
    values_1_2 = []
    for i in range(len(arr)):
        if i == 0 or i == len(arr) - 1:
            values_1_2.append(' ')
        else:
            values_1_2.append(round((arr[i + 1] - arr[i - 1]) / 2 * h, 5))
    return values_1_2


# числ. дифф. 2 порядка, погрешность O(h^2)
def num_diff_2(arr, h):
    values_2 = []
    for i in range(len(arr)):
        if i == 0 or i == len(arr) - 1:
            values_2.append(' ')
        else:
            values_2.append(round((arr[i + 1] - 2 * arr[i] + arr[i - 1]) / h ** 2, 5))
    return values_2


# вычисляем погрешность O(h) = f' - f'(h)~
def err_1(ders, difs):
    errors_1 = []
    for i in range(len(difs)):
        if i == len(difs) - 1:
            errors_1.append(' ')
        else:
            errors_1.append(ders[i] - difs[i])
    return errors_1


# вычисляем погрешность O(h^2)
def err_2(ders, difs):
    errors_2 = []
    for i in range(len(difs)):
        if i == 0 or i == len(difs) - 1:
            errors_2.append(' ')
        else:
            errors_2.append(ders[i] - difs[i])
    return errors_2

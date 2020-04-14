import math
import Lagrange



# нам дана точка f(x)=0.8, найти х по интерполяционному многочлену

# определим фукнцию f
def f(x):
    return round(math.cos(x), 4)


# определим фукнцию обратную к f
def inv_fun(x):
    return round(math.acos(x), 8)


# значение полинома Лагранжа в точке х
def p(x):
    return polynomial.get_val(x)


# метод Ньютона для уточнения корня
def newton_method(eps, a, b):
    num = 1000
    i = 1
    xk_1 = 0
    x_k = (a + b) / 2
    fx_k = p(x_k)
    derfx_k = (p(x_k + eps) - p(x_k)) / eps
    derffx_k = (p(x_k + 2 * eps) - 2 * p(x_k + eps) + p(x_k)) / eps
    if fx_k * derffx_k < 0:
        while True:
            xk_1 = x_k - fx_k / derfx_k
            if xk_1 < a or xk_1 > b:
                while xk_1 < a or xk_1 > b:
                    xk_1 = (x_k + xk_1) / 2
            if abs(x_k - xk_1) < eps or i >= num:
                return x_k
            x_k = xk_1
            i += 1


# метод бисекций для отделения корня
def bisect_method(val, a, b, eps):
    res = 0
    eps *= 10 ** (-3)

    while p(a) * p(b) > 0:
        a -= 1
        b += 1

    if p(a) - val == 0:
        return a
    if p(b) - val == 0:
        return a

    while b - a > eps:
        x_i = (a + b) / 2
        if (p(x_i) - val) * (p(a) - val) < 0:
            b = x_i
        else:
            a = x_i
    return a, b


# main
# массив узлов
arr1 = -0.6, -0.5, -0.3, -0.2, -0.1, 0
# данные нам значения функции в узлах
values = [f(arr1[i]) for i in range(len(arr1))]

# вычисляем делители полинома Лагранжа
polynomial = Lagrange.Lagrange(arr1, values)

y_0 = 0.8
a = 0
b = math.pi
eps = 10 ** (-6)

# находим отрезок, в котором лежит корень
x1, x2 = bisect_method(y_0, a, b, eps)

# находим корень
x = newton_method(eps, x1, x2)
x1 = inv_fun(y_0)

if x * x1 < 0:
    x1 *= (-1)

print('\n', 'корень поулчившийся в результате обратного интерполирования:', x)
print(' корень получившийся с помощью обратной функции', x1)
print(' фактическая погрешность: ', abs(x1 - x))

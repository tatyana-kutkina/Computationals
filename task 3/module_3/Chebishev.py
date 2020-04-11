import math
import Lagrange


def f(x):
    return round(1 / (1 + x ** 2), 5)


# вычисляем узлы
def node(k,n):
    val = math.cos(math.pi * (2 * k + 1) / (2 * (n + 1)))
    return val


# вычисляем значение полинома
def chebishev_val(x, n):

    nodes = [node(k, n) for k in range(n + 1)]  # узлы - корни многочлена Чебышева
    values = [f(nodes[i]) for i in range(len(nodes))]  # значения функции в узлах
    polynomial = Lagrange.Lagrange(nodes, values)  # вычисляем делители полинома Лагранжа

    return polynomial.get_val(x)  # возвращаем значение полинома в точке х


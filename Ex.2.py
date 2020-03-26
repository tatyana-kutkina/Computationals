import math
from Lagrange import Lagrange


# нам дана точка f(x)=0.8, найти х по интерполяционному многочлену

# определим фукнцию f
def f(x):
    return round(math.cos(x), 4)

def Newton_method(polynomial, eps, a, b):
    


# main
# массив узлов
arr1 = -0.6, -0.5, -0.3, -0.2, -0.1, 0
# данные нам значения функции в точке
values = [f(arr1[i]) for i in range(len(arr1))]

polynomial = Lagrange(arr1, values)
'''
print(polynomial.nodes)
print(polynomial.dividers)
'''
a = min(polynomial.nodes)
b = max(polynomial.nodes)
eps = 1
Newton_method(polynomial, a, b, eps)

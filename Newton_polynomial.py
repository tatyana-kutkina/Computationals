import math


# определим фукнцию f
def f(x):
    return round(math.cos(x), 4)


class Newton:

    def __init__(self, nodes, n=0, x=0):  # инициализируем класс "полином в форме Ньютона"
        self.deg = n  # степень полинома

        arr2 = []  # массив расстояний между точкой интерполирования и узлами
        for i in nodes:
            arr2 += [abs(x - i)]

        d = {}  # словарь узлов и расстояний к ним

        for i in range(len(nodes)):
            d[nodes[i]] = arr2[i]

        # X - это список n+1 узлов, в порядке близости к точке х: [узел, расстояние от точки интерполирования]
        X = list(d.items())
        X.sort(key=lambda i: i[1])

        i = len(X) - n - 1
        while i > 0:
            del X[len(X) - 1]
            i -= 1

        xx = []
        for i in X:
            xx.append(i[0])
        self.nodes = xx  # узлы, по кт строится полином
        values = []
        for i in self.nodes:
            values.append(f(i))
        self.values = values


arr1 = -0.6, -0.5, -0.3, -0.2, -0.1, 0
x = Newton(arr1, 3, -0.4)
print(x.values)

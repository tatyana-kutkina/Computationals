
def f(x):
    return round(1 / (1 + x ** 2), 5)


# вычисляем значение полинома степени n в точке х
def newton_val(n, coefs, a, h):
    arr = []
    nodes = []
    for i in range(n + 1):
        nodes.append(a + h * (i - n // 2))
        arr.append(f(a + h * (i - n // 2)))

    diffs = sep_diffs(arr, nodes)

    values = [0] * (n + 1)

    k = (n // 2)
    sch = 0

    for i in range(len(diffs)):
        y = coefs[i]
        sch += 1
        y *= diffs[i][k]
        y = round(y, 5)
        if i == 0:
            values[i] = y
        else:
            values[i] = values[i - 1] + y
        if sch % 3 == 2:
            k -= 1
            sch = 0

    return values[n]


# разделенные разности
def sep_diffs(arr, nodes):
    RR1 = []
    for i in range(len(arr) - 1):
        val = (arr[i + 1] - arr[i])
        RR1.append(val)
    RR2 = []
    for i in range(len(arr) - 2):
        val = RR1[i + 1] - RR1[i]
        RR2.append(val)

    RR = [arr, RR1, RR2]  # будущий массив разделенных разностей

    for i in range(3, len(arr)):
        vals = []
        for j in range(len(arr) - i):
            vals.append(
                round((RR[i - 1][j + 1] - RR[i - 1][j]), 5)
            )
        RR.append(vals)
    return RR


# коэффициенты N_k для составления полинома
def coefficient(n, t):
    coefs = [0] * (n + 1)
    coefs[0] = 1
    for i in range(1, n + 1):
        y = 1
        for j in range(1, i + 1):
            y *= (t - ((-1) ** j) * (j // 2)) / j
        coefs[i] = round(y, 5)
    return coefs




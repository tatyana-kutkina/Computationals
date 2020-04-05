import pandas as pd

'''
# увеличиваем ширину печати dataframe
pd.options.display.max_columns = 20
desired_width = 400
pd.set_option('display.width', desired_width)
'''

# создаем список узлов
def create_nodes(dict):
    nodes = []
    for x in dict.keys():
        nodes += [x] * len(dict[x])
    return nodes


def sep_diffs(dict, nodes):
    n = len(nodes)  # количество узлов , по кт будет строиться полином
    values = [dict[x][0] for x in nodes]
    RR1 = []
    for i in range(n - 1):
        if nodes[i] == nodes[i + 1]:
            RR1.append(dict[nodes[i]][1])
        else:
            val = (dict[nodes[i + 1]][0] - dict[nodes[i]][0]) / (nodes[i + 1] - nodes[i])
            RR1.append(val)
    RR2 = []
    for i in range(n - 2):
        if nodes[i] == nodes[i + 2]:
            RR2.append(dict[nodes[i]][2] / 2)
        else:
            val = (RR1[i + 1] - RR1[i]) / (nodes[i + 2] - nodes[i])
            RR2.append(val)

    RR = [values, RR1, RR2]  # будущий массив разделенных разностей

    for i in range(3, n):
        vals = []
        for j in range(n - i):
            vals.append(
                round((RR[i - 1][j + 1] - RR[i - 1][j]) / (nodes[j + i] - nodes[j]), 5)
            )
        RR.append(vals)

    return RR


# создаем таблицу разделенных разностей
def create_table(values, indexes):
    df = pd.DataFrame(data=values, columns=indexes).fillna(' ').T
    return df


# выделим коэффициенты полинома
def coefficient(rr):
    coefs = [rr[i][0] for i in range(len(rr))]
    return coefs


# вычислить значение полинома
def P(x, arr, x_k):
    y = 0
    for i in range(len(arr)):
        if i == 0:
            y += arr[i]
        else:
            y1 = 1
            for j in range(i):
                y1 *= (x - x_k[j])
            y += (y1 * arr[i])
    return y


# напечатать полином
def print_polynomial(arr, xx):
    s = ''
    for i in range(len(arr)):
        if i == 0:
            s += str(arr[i])
        else:
            y1 = ''
            for j in range(i):
                if xx[j] < 0:
                    y1 += "*(x+%.f)" % (-1 * xx[j])
                else:
                    if xx[j] == 0:
                        y1 += "*x"
                    else:
                        y1 += "*(x-%.f)" % xx[j]
            if arr[i] < 0:
                s += "%.3f" % arr[i] + y1
            else:
                s += "+%.3f" % arr[i] + y1
    print(s)
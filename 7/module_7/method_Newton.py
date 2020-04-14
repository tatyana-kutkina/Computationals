import pandas as pd
from math import sin, cos, sqrt


def Newton_method(xk, yk, eps, kmax, f, g, dfx, dfy, dgx, dgy):
    k = 0
    xx, yy, differ, val_f, val_g = [], [], [], [], []
    while True:

        xx.append(xk)
        yy.append(yk)
        val_f.append(f(xk, yk))
        val_g.append(g(xk, yk))

        D = dfx(xk, yk) * dgy(yk) - dgx(xk) * dfy(xk, yk)
        DX = f(xk, yk) * dgy(yk) - g(xk, yk) * dfy(xk, yk)
        DY = dfx(xk, yk) * g(xk, yk) - dgx(xk) * f(xk, yk)

        xk_1 = xk - DX / D
        yk_1 = yk - DY / D

        if k == 0:
            differ.append(' ')
        else:
            norma = sqrt((xx[k] - xx[k-1])**2 + (yy[k] - yy[k-1])**2)
            differ.append(norma)
            if norma < eps or k >= kmax:
                val = [xk, yk]
                break

        xk = xk_1
        yk = yk_1
        k += 1

    data = xx, yy, differ, val_f, val_g
    columns = [
        "$x_k$",
        "$y_k$",
        "$||(x_k − x_{k−1} , y_k − y_{k−1} )||$",
        "$f(x_k, y_k)$",
        "$g(x_k, y_k)$"
    ]
    df = pd.DataFrame(data, columns).T
    df.columns.name = "$k$"
    return df, val



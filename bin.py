import numpy as np
import math
from scipy.misc import derivative
from decimal import Decimal


def f(x):
    return round(math.cos(x), 4)
modules = [0]*4
for i in np.linspace(0.4, 0.6, 20):
    m = max(abs(derivative(f, Decimal(i), dx=1.0)))

print(m)
#print(round(i,4), end =' ')
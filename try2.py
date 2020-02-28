
import math
from decimal import Decimal

print('Дана функция f(x)=cos(x)', '\n')
#определим фукнцию f
def f(x):
    return math.cos(x)

print('Даны узлы: -0.6, -0.5, -0.3, -0.2, -0.1, 0 ', '\n')
#x1, x2, x3, x4, x5, x6 =
print('Точка интерполирования: x = -0.4', '\n')
print('Порядок интерполирования = 3', '\n')


n=3
x = -0.4
#массив узлов
arr1= -0.6, -0.5, -0.3, -0.2, -0.1, 0

arr2=[] #массив расстояний между точкой интерполирования и узлами
for i in arr1:
    a=abs(x-i)
    arr2 += [abs(x-i)]
#cловарь узлов и расстояний к ним
d={}
for i in range(len(arr1)):
    d[arr1[i]] = arr2[i]

X = list(d.items())
X.sort(key=lambda i: i[1])

i=len(X)-n-1
while i>0:
    del X[len(X)-1]
    i-=1

# X - это список n+1 узлов, в порядке близости к точке х,: [узел, расстояние от точки интерполирования]

xx = []
for i in X:
    xx.append(i[0])

r1_1_2 = (f(xx[2])-(f(xx[1])))/(xx[2]-xx[1])
r1_2_3 = (f(xx[3])-f(xx[2]))/(xx[3]-xx[2])
r2_1_2_3 = (r1_2_3 - r1_1_2)/(xx[3]-xx[1])

f0 = f(xx[0])
f1 = (f(xx[1]) - f0)/(xx[1]-xx[0])
f2 = (r1_1_2-f1)/(xx[2]-xx[0])
f3 = (r2_1_2_3-f2)/(xx[3]-xx[0])

p0 = f0
p1 = p0 + f1*(x-xx[0])
p2 = p1 + f2*(x-xx[0])*(x-xx[1])
p3 = p2 + f3*(x-xx[0])*(x - xx[1])*(x-xx[2])

print(p0, p1, p2, p3)



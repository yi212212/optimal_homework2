# find the set of optimal solutions of problem1 in ./asset/homework_2.PDF
import matplotlib.pyplot as plt
import numpy as np
import math
import seaborn as sns
from mpl_toolkits import mplot3d


def f1(x):
    return -2 * x + 1


def f2(x):
    return -(1 / 3) * x + (1 / 3)


# def f(x, y):
#     return x + y


def f(x, y):
    return -x - y


# def f(x, y):
#     return np.maximum(x, y)

# def f(x, y):
#     return x ** 2 + 9 * (y ** 2)


plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.set_xlabel(r'$x_1$')
ax.set_ylabel(r'$x_2$')
ax.set_zlabel(r'$f(x_1,x_2)$')
x = np.arange(0, 2.5, 0.001)
y = np.arange(0, 2.5, 0.001)
X, Y = np.meshgrid(x, y)
Z = f(X, Y)
sub = np.ones(Z.shape)

for i in np.arange(0, 0.5, 0.001):
    for j in np.arange(0, f1(i), 0.001):
        sub[int(j * 1000)][int(i * 1000)] = np.nan

for i in np.arange(0, 1, 0.001):
    for j in np.arange(0, f2(i), 0.001):
        sub[int(j * 1000)][int(i * 1000)] = np.nan

ZZ = sub * Z

t = np.zeros(Z.shape)
TT = t * ZZ

# ax.plot_surface(X, Y, TT)
ax.plot_surface(X, Y, ZZ, color='red')
# ax.set_title(r'$f(x_1,x_2)=x_1+x_2$')
ax.text(1.5, 1.5, -2, rf'min $f(x_1,x_2) = -Inf$')
ax.set_title(r'$f(x_1,x_2)=-x_1-x_2$')
# ax.set_title(r'$f(x_1,x_2)=max(x_1,x_2)$')
# ax.set_title(r'$f(x_1,x_2)=x^2_1+9x^2_2$')
plt.show()

# Sketch the feasible set of problem1 in ./homework_2.PDF
import numpy as np
import matplotlib.pyplot as plt
from sympy.solvers import solve
from sympy import Symbol


def f1(x):
    return 1 - 2 * x


def f2(x):
    return (1 - x) / 3


xr = np.linspace(-0.5, 2, 100)
y1r = f1(xr)
y2r = f2(xr)
plt.plot(xr, y1r, label=r'$2x_1 + x_2 - 1 = 0$')
plt.plot(xr, y2r, label=r'$x_1 + 3x_2 - 1 = 0$')
x = Symbol('x')
x1, = solve(f1(x) - f2(x))
y1 = f1(x1)
plt.fill([0, 0, x1, 1, 2.5, 2.5, 0], [2.5, 1, y1, 0, 0, 2.5, 2.5], 'brown', alpha=0.5)
plt.axvline(0, color='r', label=r'$x_1 = 0$')
plt.axhline(0, color='g', label=r'$x_2 = 0$')
plt.xlim((-0.5, 2.500))
plt.ylim((-0.5, 2.500))
plt.legend()
plt.xlabel(r'$x_1$', fontsize=13)
plt.ylabel(r'$x_2$', fontsize=13)
plt.title('feasible set')
plt.annotate('the feasible set', xy=(1, 1.5), xytext=(+30, -30), textcoords='offset points', fontsize=16,
             arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=.0'))
plt.show()

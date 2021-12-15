# Sketch the feasible set of problem2 in ./asset/homework_2.PDF
import numpy as np
import matplotlib.pyplot as plt

# 利用sin,cos函数画圆
# 利用fill()函数填充图形区域
a_x = np.arange(0, 2 * np.pi, 0.01)
a = 1 + 1 * np.cos(a_x)
b = 1 + 1 * np.sin(a_x)
plt.plot(a, b, color='b', linestyle='-', label=r'$(x_1-1)^2+(x_2-1)^2 ≤ 1$')
plt.fill(a, b, color='b')
plt.plot(a, -b, color='purple', linestyle='-', label=r'$(x_1-1)^2+(x_2+1)^2 ≤ 1$')
plt.fill(a, -b, color='purple')

a = 0.8 * np.cos(a_x)
b = 0.8 * np.sin(a_x)
plt.plot(a, b, linestyle='-.', label=r'$p = 0.8$')

a = 1.2 * np.cos(a_x)
b = 1.2 * np.sin(a_x)
plt.plot(a, b, linestyle='-.', label=r'$p = 1.2$')

a = 1.6 * np.cos(a_x)
b = 1.6 * np.sin(a_x)
plt.plot(a, b, linestyle='-.', label=r'$p = 1.6$')

plt.axvline(0, color='black')
plt.axhline(0, color='black')
plt.plot(0, 0, '.')
plt.plot(1, 0, '.', color='r')

plt.annotate('feasible point', xy=(1, 0), xytext=(+30, -30), textcoords='offset points', fontsize=10,
             arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=.0'))

plt.ylim(-3, 5)
plt.xlim(-3, 5)
plt.legend()
plt.show()

import matplotlib.pyplot as plt
import numpy as np
import math
import seaborn as sns
from mpl_toolkits import mplot3d

plt.rcParams['font.sans-serif'] = ['SimHei']  # 步骤一(替换sans-serif字体)
plt.rcParams['axes.unicode_minus'] = False  # 原文出自【易百教程】，商业转载请联系作者获得授权，非商业请保留原文链接：

fig = plt.figure()
ax = plt.axes(projection='3d')
x = np.linspace(0, 1, 100)
y = np.linspace(0, 1, 100)

z = x + y
print(x.shape, y.shape, z.shape)
ax.plot3D(x, y, z, 'gray')
ax.set_title('3D line plot')
plt.show()

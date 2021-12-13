# Solve the problems of problem3 in ./asset/homework_2.PDF
import numpy as np
import matplotlib.pyplot as plt

# 初始化x,y,theta
x = np.matrix([[2, 0], [0, 1], [0, 0]])
y = np.matrix([3, 2, 2]).T
theta = np.matrix(np.array([0, 0]))


# 正规方程解法：
# t = np.linalg.inv(x.T * x) * x.T * y
# print([t])
# inner = np.power(x * t - y, 2)
# print(np.sum(inner))


def h(x, theta):
    return x * theta.T


def computeCost(x, y, theta):
    # 计算代价函数
    inner = np.power((h(x, theta) - y), 2)
    return np.sum(inner)


# 约束条件
def constraint(W, t):
    if W[0, 0] ** 2 + W[0, 1] ** 2 > t:
        return True
    else:
        return False


# 梯度下降
def gradientDescent(X, y, theta, alpha, iters):
    temp = np.matrix(np.zeros(theta.shape))
    parameters = int(theta.ravel().shape[1])
    cost = []
    for i in range(iters):
        error = h(x, theta) - y
        for j in range(parameters):
            term = np.multiply(error, X[:, j])
            temp[0, j] = theta[0, j] - ((alpha / len(X)) * np.sum(term))
        theta = temp
        cost.append(computeCost(X, y, theta))
        # 加入约束条件，约束参数
        if constraint(temp, t=10):
            break
    return theta, cost


theta, cost = gradientDescent(x, y, theta, 0.01, 10000)
print(f'约束条件：t=10\n最优参数为：w = {theta}\n最小值是：{cost[-1]}')

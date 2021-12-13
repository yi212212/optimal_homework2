# Solve the problems of problem3 in ./asset/homework_2.PDF
import numpy as np
import matplotlib.pyplot as plt

# 初始化x,y,theta
x = np.matrix([[2, 0], [0, 1], [0, 0]])
y = np.matrix([3, 2, 2]).T
theta = np.matrix(np.array([0, 0]))


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


def gradientDescent(X, y, theta, alpha, iters):
    temp = np.matrix(np.zeros(theta.shape))
    parameters = int(theta.ravel().shape[1])
    cost = np.zeros(iters)
    for i in range(iters):
        error = h(x, theta) - y
        for j in range(parameters):
            term = np.multiply(error, X[:, j])
            temp[0, j] = theta[0, j] - ((alpha / len(X)) * np.sum(term))
        theta = temp
        cost[i] = computeCost(X, y, theta)
    return theta, cost


theta, cost = gradientDescent(x, y, theta, 0.01, 10000)
print(f'最优参数w为：{theta}\n最小值是：{cost[-1]}')

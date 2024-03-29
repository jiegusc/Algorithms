import numpy as np
import scipy as sp
from scipy.optimize import leastsq
import matplotlib.pyplot as plt
# %matplotlib inline
# 目标函数
def real_func(x):
    return np.sin(2*np.pi*x)

# 多项式
# ps: numpy.poly1d([1,2,3])  生成  $1x^2+2x^1+3x^0$*
def fit_func(p, x):
    f = np.poly1d(p)
    return f(x)

# 十个点
x = np.linspace(0, 1, 10)
x_points = np.linspace(0, 1, 1000)
# 加上正态分布噪音的目标函数的值
y_ = real_func(x)
y = [np.random.normal(0, 0.1)+y1 for y1 in y_]

def fitting(M=0):
    """
    n 为 多项式的次数
    """
    # 随机初始化多项式参数
    p_init = np.random.rand(M+1)
    # 最小二乘法
    p_lsq = leastsq(residuals_func, p_init, args=(x, y))
    print('Fitting Parameters:', p_lsq[0])

    # 可视化
    plt.plot(x_points, real_func(x_points), label='real')
    plt.plot(x_points, fit_func(p_lsq[0], x_points), label='fitted curve')
    plt.plot(x, y, 'bo', label='noise')
    plt.legend()
    # plt.show()
    return p_lsq

# p_lsq_9 = fitting(M=9)


regularization = 0.0001

# 残差 p:ans, x, y: samples
def residuals_func(p, x, y):
    ret = fit_func(p, x) - y
    return ret


def residuals_func_regularization(p, x, y):
    ret = fit_func(p, x) - y
    # 此处append正则化项
    ret = np.append(ret, (0.5*regularization*np.square(p))) # L2范数作为正则化项
    return ret

# 设置9次多项式
p_init = np.random.rand(5+1)
p_lsq_regularization = leastsq(residuals_func_regularization, p_init, args=(x, y))
p_lsq = leastsq(residuals_func, p_init, args=(x, y))

plt.plot(x_points, real_func(x_points), label='real')
plt.plot(x_points, fit_func(p_lsq[0], x_points), label='fitted curve')
plt.plot(x_points, fit_func(p_lsq_regularization[0], x_points), label='regularization')
plt.plot(x, y, 'bo', label='noise')
plt.legend()
plt.show()


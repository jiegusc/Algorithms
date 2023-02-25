import numpy as np
import scipy.stats

man_distribution = scipy.stats.norm(172, 5).pdf(180)
print(man_distribution)
woman_distribution = scipy.stats.norm(162, 5).pdf(180)
print(woman_distribution)

import matplotlib.pyplot as plt

μ = 30  # 数学期望
σ = 2  # 方差
x = μ + σ * np.random.randn(10000)  # 正态分布
plt.hist(x, bins=100)  # 直方图显示
# plt.show()
# 输出最有可能的期望和方差
print(scipy.stats.norm.fit(x))

from sympy import symbols, pi, exp, log
from sympy.stats import Probability, Normal

# 样本
X = [1,2,3,4,5, 3,4,2,5,6,]
x = symbols('x')
# 总体 mu 和 sigma
m, s = symbols('m s')
# pdf
pdf = 1/ (s * (2*pi)**0.5)*exp( -(x-m)**2 / (2*s**2) )
logpdf = log(pdf)
print(logpdf)


num1, mu1, var1 = 300, [5, 8], [[1, 0],[0,3]]
X1 = np.random.multivariate_normal(mu1, var1, num1)
num2, mu2, var2 = 300, [-3, 3], [[1, 0],[0,1]]
X2 = np.random.multivariate_normal(mu2, var2, num2)
X = np.vstack((X1, X2))


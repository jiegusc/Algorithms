from scipy.stats import norm
import matplotlib.pyplot as plt
import random


#   假设目标平稳分布是一个均值3，标准差2的正态分布，而选择的马尔可夫链状态转移矩阵
#   Q(i, j)的条件转移概率是以 i 为均值,方差1的正态分布在位置 j 的值。

def norm_dist_prob(theta):
    #   loc = mean, scale = standard variance
    y = norm.pdf(theta, loc=3, scale=2)
    return y

T = 5000
pi = [0 for i in range(T)]
sigma = 1
t = 0
while t < T-1:
    t = t + 1
    pi_star = norm.rvs(loc=pi[t - 1], scale=sigma, size=1, random_state=None)   #状态转移进行随机抽样
    alpha = min(1, (norm_dist_prob(pi_star[0]) / norm_dist_prob(pi[t - 1])))   #alpha值
    # print(alpha)
    u = random.uniform(0, 1)
    if u < alpha:
        pi[t] = pi_star[0]
    else:
        pi[t] = pi[t - 1]

# plt.scatter(pi, norm.pdf(pi, loc=3, scale=2),label='Target Distribution')
# num_bins = 50
# plt.hist(pi, num_bins, density=1, facecolor='red', alpha=0.7,label='Samples Distribution')
# plt.legend()
# plt.show()


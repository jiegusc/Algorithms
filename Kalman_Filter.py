import numpy as np
import matplotlib.pyplot as plt

delta_t = 0.1  # 每0.1秒钟采一次样
end_t = 7  # 时间长度
time_t = end_t * 10  # 采样次数
t = np.arange(0, end_t, delta_t)  # 设置时间数组
u = 1  # 定义外界对系统的作用 加速度
x = 1 / 2 * u * t ** 2  # 实际真实位置

v_var = 1  # 测量噪声的方差
# 创建高斯噪声，精确到小数点后两位
v_noise = np.round(np.random.normal(0, v_var, time_t), 2)

X = np.mat([[0], [0]])  # 定义预测优化值的初始状态,这个初始状态可以自己根据情况定义
v = np.mat(v_noise)  # 定义测量噪声
z = x + v  # 定义测量值（假设测量值=实际状态值+噪声）

A = np.mat([[1, delta_t], [0, 1]])  # 定义状态转移矩阵
B = [[1 / 2 * (delta_t ** 2)], [delta_t]]  # 定义输入控制矩阵
P = np.mat([[1, 0], [0, 1]])  # 定义初始状态协方差矩阵
Q = np.mat([[0.001, 0], [0, 0.001]])  # 定义状态转移(预测噪声)协方差矩阵
H = np.mat([1, 0])  # 定义观测矩阵
R = np.mat([1])  # 定义观测噪声协方差
X_mat = np.zeros(time_t)  # 初始化记录系统预测优化值的列表
X_vec = np.zeros(time_t)
for i in range(time_t):
    # 预测
    X_predict = A * X + np.dot(B, u)  # 估算状态变量
    P_predict = A * P * A.T + Q  # 估算状态误差协方差
    # 校正
    K = P_predict * H.T / (H * P_predict * H.T + R)  # 更新卡尔曼增益
    X = X_predict + K * (z[0, i] - H * X_predict)  # 更新预测优化值
    P = (np.eye(2) - K * H) * P_predict  # 更新状态误差协方差
    # 记录系统的预测优化值
    X_mat[i] = X[0, 0]
plt.plot(x, "b", label='actual state value')  # 设置曲线数值
plt.plot(X_mat, "g", label='predict optimal value')
plt.plot(z.T, "r--", label='measurement value')
# plt.plot(X_vec, "b", label='predict optimal velocity')
plt.xlabel("time")  # 设置X轴的名字
plt.ylabel("distance")  # 设置Y轴的名字
plt.title("Falman filter diagram")  # 设置标题
plt.legend()  # 设置图例
# plt.show()

a = [1,1,1,1]
b = [5,6,7,8]
# s = sum(b)/4
# u = [(i - s) ** 2 for i in b]
# print(sum(u)/3)
k = np.stack((a,b))
print(k)
print(np.cov(a,b))
# print(np.cov(k.T))



#####################################################
# x=np.arange(10e-10, 1, 0.01)
#
# def func_px(u, x):
#     return np.exp(-(u**2 / (2 * x)))
#
# def func_qx(x):
#     return np.sqrt(2 * np.pi * x)
#
# N = [0.005, 0.03, 0.06, 0.1,0.2,0.3]
# plt.plot(x, func_qx(x), "b", label="qx value")
#
# for i in range(len(N)):
#     plt.plot(x, func_px(N[i], x), label=f'px value in {N[i]}')
#
# plt.xlim(0, 1)
# plt.legend()  # 设置图例
# plt.show()

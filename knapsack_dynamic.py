# # 这里使用了图解中的吉他，音箱，电脑，手机做的测试，数据保持一致
# w = [0, 1, 4, 3, 1]   #n个物体的重量(w[0]无用)
# p = [0, 1500, 3000, 2000, 2000]   #n个物体的价值(p[0]无用)
# n = len(w) - 1   #计算n的个数　     东西的种类
# m = 4   #背包的载重量
#
# x = []   #装入背包的物体，元素为True时，对应物体被装入(x[0]无用)
# v = 0
# #optp[i][j]表示在前i个物体中，能够装入载重量为j的背包中的物体的最大价值
# optp = [[0 for col in range(m + 1)] for raw in range(n + 1)]
# #optp 相当于做了一个n*m的全零矩阵的赶脚，n行为物件，m列为自背包载重量
#
# def knapsack_dynamic(w, p, n, m, x):
#     #计算optp[i][j]
#     for i in range(1, n + 1):       # 物品一件件来
#         for j in range(1, m + 1):   # j为子背包的载重量，寻找能够承载物品的子背包
#             if (j >= w[i]):         # 当物品的重量小于背包能够承受的载重量的时候，才考虑能不能放进去
#                 optp[i][j] = max(optp[i - 1][j], optp[i - 1][j - w[i]] + p[i])    # optp[i - 1][j]是上一个单元的值， optp[i - 1][j - w[i]]为剩余空间的价值
#             else:
#                 optp[i][j] = optp[i - 1][j]
#
#     #递推装入背包的物体,寻找跳变的地方，从最后结果开始逆推
#     j = m
#     for i in range(n, 0, -1):
#         if optp[i][j] > optp[i - 1][j]:
#             x.append(i)
#             j = j - w[i]
#
#     #返回最大价值，即表格中最后一行最后一列的值
#     v = optp[n][m]
#     return v
#
# print ('最大值为：' + str(knapsack_dynamic(w, p, n, m, x)))
# print ('物品的索引：',x)

# print(table)
def knapsack_dynamic(weights, values, weight_bag):
    #   keep the order, the first is useless, just keep the form.
    weights = [0, 1, 4, 3, 1]
    values = [0, 1500, 3000, 2000, 2000]
    weight_bag = 4

    result_weight = []
    #   the number of the items
    num = len(weights) - 1
    table = [[0 for _ in range(num + 1)] for _ in range(weight_bag + 1)]

    for i in range(1, num + 1):
        for j in range(1, weight_bag + 1):
            if j >= weights[i]:
                table[i][j] = max(table[i - 1][j], values[i] + table[i - 1][j - weights[i]])
            else:
                table[i][j] = table[i - 1][j]

    j = weight_bag
    for i in range(num, 0, -1):
        if table[i][j] > table[i - 1][j]:
            result_weight.append(i)
            j = j - weights[i]

    return result_weight, table[num][weight_bag]


weights = [0, 1, 4, 3, 1]
values = [0, 1500, 3000, 2000, 2000]
weight_bag = 4
a, b = knapsack_dynamic(weights, values, weight_bag)
# print(a, b)

# def mapeach(w,v):
#     table = [[1,1] for _ in range(len(w))]
#     for i in range(len(table)):
#         table[i][0] = w[i]
#         table[i][1] = v[i]
#     table.sort()
#     return table
# print(mapeach(weights,values))


# double CPU problem
# w is the amount of the time each task.
def double_CPU(w):
    p = list(map(lambda x: x/1024, w))
    limit = int(sum(p)/2) + 1
    table = [[0] * int(limit + 1) for _ in range(len(w))]
    for i in range(1, len(p)):
        for j in range(1, limit + 1):
            if j >= p[i]:
                table[i][j] = max(table[i - 1][j], p[i] + table[i - 1][j - int(p[i])])
            else:
                table[i][j] = table[i - 1][j]
    j = limit
    ans = []
    for i in range(len(table) - 1, -1, -1):
        if table[i][j] > table[i - 1][j]:
            ans.append(w[i])
            j -= int(p[i])
    ans2 = w
    for i in ans:
        ans2.remove(i)
    ans2.pop(0)
    return table[-1][-1], ans, ans2


# w = [0, 3072, 3072, 7168, 3072, 1024]  # 假设进入处理的的任务大小
# w = map(lambda x:x/1024,w)
# print(list(w))
# print(double_CPU(w))


# LIS
def Lis(a):
    dp = [1] * len(a)
    max_len = 0
    for i in range(len(a)):
        for j in range(i):
            if a[i] > a[j] and dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
                max_len = max(max_len, dp[i])
    return max_len

lis = [2 ,1, 5, 3, 6 ,4 ,8 ,9, 7]
# print(Lis(lis))


#   LCS
def LCS(a,b):
    dp = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp

s1 = [1,3,4,5,6,7,7,8]
s2 = [3,5,7,4,8,6,7,8,2]
# s1 = [6,5,4,3,2,1]
# s2 = [1,2,3,4,5,6]
print(LCS(s1, s2))



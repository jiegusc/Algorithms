
"""
不确定性越大，熵越大，确定该事所需的信息量也越大；
不确定性越小，熵越小，确定该事所需的信息量也越小。
分类时熵越小越好！！！！！！！！！！！！！！！！！！！
https://blog.csdn.net/gracejpw/article/details/101906614
entropy 是表示不纯度，即没有有效信息 或者 这个信息对于分类没有帮助。
entropy值越大，越不纯。
"""

from math import log #我们要用到对数函数，所以我们需要引入math模块中定义好的log函数（对数函数）

def createDataSet():
    dataSet = [[1,1,'yes'],
              [1,1,'yes'],
              [1,0,'no'],
              [0,1,'no'],
              [0,1,'no'],
              [0,1,'no']] # 我们定义了一个list来表示我们的数据集，这里的数据对应的是上表中的数据

    labels = ['no surfacing','flippers']

    return dataSet, labels


def calcShannonEnt(dataSet):#传入数据集
# 在这里dataSet是一个链表形式的的数据集
    shannonEnt = {}
    for i in range(len(dataSet[0])):
        shannonEnt[i] = {}

    for label in range(len(dataSet[0])):
        for num in range(len(dataSet)):
            if dataSet[num][label] not in shannonEnt[label].keys():
                shannonEnt[label][dataSet[num][label]] = 0
            shannonEnt[label][dataSet[num][label]] += 1
    print(shannonEnt)
    ans = []
    gini_ans = []
    error_ans = []
    for label in range(len(dataSet[0])):
        entropy = 0
        gini = 1
        error_max = -float('inf')
        for key in shannonEnt[label]:
            prob = float(shannonEnt[label][key] / len(dataSet))
            entropy -= prob * log(prob, 2)
            gini -= (prob)**2
            error_max = max(prob, error_max)
        ans.append(entropy)
        gini_ans.append((gini))
        error_ans.append(1 - error_max)

    return f" entropy: {ans}, gini: {gini_ans}, error: {error_ans}"

# data,labels=createDataSet()
# se=calcShannonEnt(data)
# print(se)
# print(labels)

a = {'c0': 1, 'c1': 3}
b = {'c0': 8, 'c1': 0}
c = {'c0': 1, 'c2': 7}

# entropy = - 1/3 * log(1/3, 2) - 2/3 * log(2/3, 2)
# print(entropy)
# entropy1 = - 1 * log(1/2) - 0
# print(entropy1)
# entropy2 = - 1/8 * log(1/8, 2) - 7/8 * log(7/8, 2)
# print(entropy2)
# print(1 - 4 / 20 * entropy - 8/20 * entropy1 - 8/20 * entropy2)
#
#
# entropy3 = - 4 / 10 * log(4/10, 2) - 6 / 10 * log(6/10, 2)
# print(1 - 1/2 * entropy3 - 1/2 * entropy3)
# https://zhuanlan.zhihu.com/p/78311644
# 伯努利实验，arr里是每一次样本里head 朝上出现的次数
arr = [5,9,8,4,7]
# 每次样本里实验的次数
total_num = 10
# a: A硬币的正面朝上的概率（因为硬币可能不是均匀的）
# b: B硬币的正面朝上的概率（因为硬币可能不是均匀的）
# head： 每次采样的时候朝上的概率
# total: 一共采样的次数
# arob: 为了复用这个函数，True为A占总比的概率，False为B占总比的概率
# This is Estimation step:
#     Estimate the probability of choosing from A or B. Pay attention on the past param.
def funcp(a, b, head, total, aorb):
    if(aorb):
        return (a ** head * (1 - a) ** (total - head)) / \
               ((a ** head * (1 - a) ** (total - head)) +
                (b ** head * (1 - b) ** (total - head)))
    else:
        return (b ** head * (1 - b) ** (total - head)) / \
               ((a ** head * (1 - a) ** (total - head)) +
                (b ** head * (1 - b) ** (total - head)))


probability_a = 0.5
probability_b = 0.5
def em(a, b, arr, total_num):
    bef = 99999
    now = 88888
    count = 20
    probability_a = a
    probability_b = b
    while (count > 0):

        # 这里是最大似然函数求导之后，得出的thetaA，thetaB的公式。
        # 公式里的10为每次采样的次数
        # 每次实验是A或者B的概率需要根据当次的a 和 b 的probability计算。
        numeratora = sum([funcp(probability_a, probability_b, i, total_num, True) * i for i in arr])
        denominatora = sum([funcp(probability_a, probability_b, i, total_num,True) * 10 for i in arr])
        probability_a = numeratora / denominatora
        # numeratorb = sum([(1 - funcp(probability_a, probability_b, i,total_num, True)) * i for i in arr])
        # denominatorb = sum([(1 - funcp(probability_a, probability_b, i,total_num, True)) * 10 for i in arr])
        numeratorb_ = sum([funcp(probability_a, probability_b, i, total_num, False) * i for i in arr])
        denominatorb_ = sum([funcp(probability_a, probability_b, i, total_num, False) * 10 for i in arr])
        probability_b = numeratorb_ / denominatorb_
        print(probability_a, probability_b)
        count -= 1
    return probability_a, probability_b

em(probability_a, probability_b,arr,total_num)

# https://zhuanlan.zhihu.com/p/85236423



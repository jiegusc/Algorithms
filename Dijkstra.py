# 一共有2种表达形式
# 1. 二维数组
# 2. 图的形式：字典类型

"""
NOTE(Jay):
Calculate the smallest distance from the start point to each point in the matrix of in the graph.
"""
MAX= float('inf')

# NOTE(Jay): Max: 到不了的物理意义表示
matrix = [
    [0,10,MAX,4,MAX,MAX],
    [10,0,8,2,6,MAX],
    [MAX,8,10,15,1,5],
    [4,2,15,0,6,MAX],
    [MAX,6,1,6,0,12],
    [MAX,MAX,5,MAX,12,0]
    ]

def dijkstra(matrix, start_node):
    # 矩阵一维数组的长度，即节点的个数
    matrix_length = len(matrix)
    # 访问过的节点数组
    used_node = [False] * matrix_length
    # 最短路径距离数组
    distance = [MAX] * matrix_length
    # 初始化，将起始节点的最短路径修改成0
    distance[start_node] = 0
    # 将访问节点中未访问的个数作为循环值，其实也可以用个点长度代替。
    while used_node.count(False):
        min_value = float('inf')
        min_value_index = 999

        # 在最短路径节点中找到最小值，已经访问过的不在参与循环。
        # 得到最小值下标，每循环一次肯定有一个最小值
        # NOTE(Jay): first point is the starting point
        for index in range(matrix_length):
            if not used_node[index] and distance[index] < min_value:
                min_value = distance[index]
                # NOTE(Jay): current the most smallest distance index
                min_value_index = index

        # 将访问节点数组对应的值修改成True，标志其已经访问过了
        used_node[min_value_index] = True

        # 更新distance数组。
        # 以B点为例：distance[x] 起始点达到B点的距离，
        # distance[min_value_index] + matrix[min_value_index][index] 是起始点经过某点达到B点的距离，比较两个值，取较小的那个。
        for each in range(matrix_length):
            distance[each] = min(distance[each], distance[min_value_index] + matrix[min_value_index][each])

    return distance



start_node = int(input('请输入起始节点:'))
result = dijkstra(matrix, start_node)
print('起始节点到其他点距离：%s' % result)



# below is the graph case
# graph_dict = {
# 's1':[('s2',1),('s3',1),('s4',1)],
# 's2':[('s1',1), ('s4',1)],
# 's3':[('s1',1), ('s4',1)],
# 's4':[('s1',1),('s2',1),('s3',1)],
# }
#https://leetcode.com/problems/network-delay-time/

#
# def networkDelayTime(times, n: int, k: int) -> int:
#     node_pass = [False] * n
#     dis = [float('inf')] * n
#     dis[k - 1] = 0
#     while node_pass.count(False):
#         min_val = float('inf')
#         min_index = -1
#         for i in range(n):
#             if not node_pass[i] and dis[i] < min_val:
#                 min_val = dis[i]
#                 min_index = i
#         if min_index == -1:
#             break
#         node_pass[min_index] = True
#         for j in times:
#             if j[0] - 1 == min_index:
#                 dis[j[1] - 1] = min(dis[j[1] - 1], min_val + j[2])
#     ans = max(dis)
#     return ans if ans < float('inf') else -1
#
# list = [[2,1,1],[2,3,1],[3,4,1]]
# n = 4
# k = 2
#
#
# print(networkDelayTime(list, n, k))
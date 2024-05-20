#!/usr/bin/env python3

# ================= 代码实现开始 =================

''' 请在这里定义你需要的全局变量 '''

# 给定一个n个点m条边的无向图，第i条边边权为i，求所有需要升级的边
# n：如题意
# m：如题意
# U：大小为m的数组，表示m条边的其中一个端点
# V：大小为m的数组，表示m条边的另一个端点
# 返回值：所有需要升级的边，从小到大排列；第一小问的答案自然即为返回值的size，所以你不必考虑如何返回size
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            if self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            elif self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1

def getAnswer(n, m, U, V):
    ''' 请使用最小生成树算法 '''
    # 构建边的列表
    edges = [(i, U[i-1], V[i-1]) for i in range(1, m+1)]

    # 按照边的权重（即标号）从小到大排序
    edges.sort(reverse=True)

    # 初始化并查集
    uf = UnionFind(n+1)

    # 选出最小生成树的边
    selected_edges = []

    for edge in edges:
        index, u, v = edge

        if uf.find(u) != uf.find(v):
            selected_edges.append(index)
            uf.union(u, v)

    return selected_edges

n, m = map(int, input().split())
U, V = [], []

for i in range(m):
    u, v = map(int, input().split())
    U.append(u)
    V.append(v)

ans = getAnswer(n, m, U, V)
ans.sort()
print(len(ans))
print(*ans, sep='\n')
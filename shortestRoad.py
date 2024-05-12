#!/usr/bin/env python3

# ================= 代码实现开始 =================

''' 请在这里定义你需要的全局变量 '''

# 这个函数的功能是计算答案（即最少花费的金钱）
# n：表示序列长度
# a：存储整个序列 a
# 返回值：最少花费的金钱（需要注意，返回值的类型为 64 位有符号整数）
import heapq
 
def dijkstra(graph, start, end):
    n = len(graph)
    dist = [float('inf')] * n
    dist[start - 1] = 0
    pq = [(0, start)]
 
    while pq:
        curr_dist, node = heapq.heappop(pq)
 
        if curr_dist > dist[node - 1]:
            continue
 
        for neighbor, weight in graph[node]:
            new_dist = curr_dist + weight
            if new_dist < dist[neighbor - 1]:
                dist[neighbor - 1] = new_dist
                heapq.heappush(pq, (new_dist, neighbor))
 
    return dist[end - 1]
 

n, m, s, t = map(int, input().split())
graph = {i: [] for i in range(1, n + 1)}
 
for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))
 

result = dijkstra(graph, s, t)
 

print(result)
 
 
 

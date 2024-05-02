#!/usr/bin/env python3

# ================= 代码实现开始 =================

''' 请在这里定义你需要的全局变量 '''


def max_cars(n, board):
    def find_path(i):
        for j in range(n):
            if board[i][j] == 1 and not visited[j]:
                visited[j] = True
                if match[j] == -1 or find_path(match[j]):
                    match[j] = i
                    return True
        return False
 
    match = [-1] * n
    result = 0
 
    for i in range(n):
        visited = [False] * n
        if find_path(i):
            result += 1
 
    return result
 

n = int(input())
board = []
for _ in range(n):
    row = list(map(int, input().split()))
    board.append(row)
 

max_cars_count = max_cars(n, board)
 

print(max_cars_count)

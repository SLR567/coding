#!/usr/bin/env python3

# ================= 代码实现开始 =================

''' 请在这里定义你需要的全局变量 '''

# 这个函数的功能是计算答案（即最少花费的金钱）
# n：表示序列长度
# a：存储整个序列 a
# 返回值：最少花费的金钱（需要注意，返回值的类型为 64 位有符号整数）
def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    result = -1
 
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] >= target:
            result = arr[mid]
            high = mid - 1
        else:
            low = mid + 1
 
    return result
 
 

n = int(input())
sequence = list(map(int, input().split()))
q = int(input())
 

sorted_sequence = sorted(sequence)
 

for _ in range(q):
    x = int(input())
 
        
    result = binary_search(sorted_sequence, x)
 

    print(result)
 


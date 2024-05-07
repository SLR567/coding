#!/usr/bin/env python3

# ================= 代码实现开始 =================

''' 请在这里定义你需要的全局变量 '''

# 这个函数的功能是计算答案（即最少花费的金钱）
# n：表示序列长度
# a：存储整个序列 a
# 返回值：最少花费的金钱（需要注意，返回值的类型为 64 位有符号整数）
def merge_and_count(arr, left, mid, right):
    i, j, k = left, mid + 1, 0
    count = 0
    temp = [0] * (right - left + 1)
 
    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp[k] = arr[i]
            i += 1
        else:
            temp[k] = arr[j]
            count += mid - i + 1  
            j += 1
        k += 1
 
    while i <= mid:
        temp[k] = arr[i]
        i += 1
        k += 1
 
    while j <= right:
        temp[k] = arr[j]
        j += 1
        k += 1
 
    for i in range(len(temp)):
        arr[left + i] = temp[i]
 
    return count
 
def merge_sort_and_count(arr, left, right):
    count = 0
    if left < right:
        mid = (left + right) // 2
        count += merge_sort_and_count(arr, left, mid)
        count += merge_sort_and_count(arr, mid + 1, right)
        count += merge_and_count(arr, left, mid, right)
    return count
 
def min_swaps(arr):
    return merge_sort_and_count(arr, 0, len(arr) - 1)
 

n = int(input())
arr = list(map(int, input().split()))
 

result = min_swaps(arr)
print(result)
 

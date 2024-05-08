#!/usr/bin/env python3

# ================= 代码实现开始 =================

# 这是进行排序的函数
# n：题目描述中的 n
# A：各同学的算法训练营成绩
# DS：各同学的数据结构训练营成绩
# 返回值：将要输出的数字依次加入到返回值的数组中
def merge_sort(arr):
    if len(arr) <= 1:
        return arr, 0
    
    mid = len(arr) // 2
    left, left_inv = merge_sort(arr[:mid])
    right, right_inv = merge_sort(arr[mid:])
    
    merged, merge_inv = merge(left, right)
    total_inv = left_inv + right_inv + merge_inv
    
    return merged, total_inv

def merge(left, right):
    merged = []
    inversions = 0
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i][1] > right[j][1] or (left[i][1] == right[j][1] and left[i][2] > right[j][2]):
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            inversions += len(left) - i
            j += 1
    
    merged.extend(left[i:])
    merged.extend(right[j:])
    
    return merged, inversions

n = int(input())
students = []

for i in range(n):
    a, b = map(int, input().split())
    students.append((i+1, a+b, a, b))

sorted_students, inversions = merge_sort(students)

for i, student in enumerate(sorted_students):
    print(student[0], student[1], student[2], student[3])

print(inversions)
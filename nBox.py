#!/usr/bin/env python3

# ================= 代码实现开始 =================

''' 请在这里定义你需要的全局变量 '''

# 执行操作时会调用这个函数
# op：对应该次操作的 op（具体请见题目描述）
# x：对应该次操作的 x（具体请见题目描述）
# 返回值：如果输出为"Succeeded"，则这个函数返回 1，否则返回 0
'''
你有一个盒子，你可以往里面放数，也可以从里面取出数。

初始时，盒子是空的，你会依次做 Q 个操作，操作分为两类：

插入操作：询问盒子中是否存在数 x，如果不存在则把数 x 丢到盒子里。
删除操作：询问盒子中是否存在数 x，如果存在则取出 x。
对于每个操作，你需要输出是否成功插入或删除。

第一行一个正整数 Q，表示操作个数。

接下来 Q 行依次描述每个操作。每行 2 个用空格隔开的非负整数 op,x 描述一个操作：op 表示操作类型，op=1 则表示这是一个插入操作，op=2 则表示这是一个删除操作；x 的意义与操作类型有关，具体见题目描述。
'''
table = set()

def check(op, x):
    if op == 1:
        if x in table:
            return 0
        else:
            table.add(x)
            return 1
    else:
        if x in table:
            table.remove(x)
            return 1
        else:
            return 0


# ================= 代码实现结束 =================

Q = int(input())
for _ in range(Q):
    op, x = map(int, input().split())
    print("Succeeded" if check(op, x) else "Failed")
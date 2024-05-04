#include <bits/stdc++.h>


// ================= 代码实现开始 =================



/* 请在这里定义你需要的全局变量 */

// 这是求解整个问题的函数
// w：题目描述中的 w（所有）
// n：题目描述中的 n
// 返回值：答案
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int find(vector<int>& parent, int x) {
    while (parent[x] != x) {
        parent[x] = parent[parent[x]];
        x = parent[x];
    }
    return x;
}

void unionSets(vector<int>& parent, vector<int>& rank, int x, int y) {
    int xroot = find(parent, x);
    int yroot = find(parent, y);
    if (rank[xroot] < rank[yroot]) {
        parent[xroot] = yroot;
    } else if (rank[xroot] > rank[yroot]) {
        parent[yroot] = xroot;
    } else {
        parent[yroot] = xroot;
        rank[xroot] += 1;
    }
}

bool getAnswer(int n, int m, vector<int>& A, vector<int>& B, vector<int>& E) {
    vector<int> parent(n + 1);
    vector<int> rank(n + 1, 0);
    for (int i = 1; i <= n; i++) {
        parent[i] = i;
    }
    for (int i = 0; i < m; i++) {
        int a = A[i];
        int b = B[i];
        int e = E[i];
        if (e == 1) {
            unionSets(parent, rank, a, b);
        }
    }
    for (int i = 0; i < m; i++) {
        int a = A[i];
        int b = B[i];
        int e = E[i];
        if (e == 0 && find(parent, a) == find(parent, b)) {
            return false;
        }
    }
    return true;
}

int main() {
    int T;
    cin >> T;
    while (T--) {
        int n, m;
        cin >> n >> m;
        vector<int> A(m), B(m), E(m);
        for (int i = 0; i < m; i++) {
            cin >> A[i] >> B[i] >> E[i];
        }
        bool answer = getAnswer(n, m, A, B, E);
        if (answer) {
            cout << "Yes" << endl;
        } else {
            cout << "No" << endl;
        }
    }
    return 0;
}
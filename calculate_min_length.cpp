#include <bits/stdc++.h>


// ================= 代码实现开始 =================



/* 请在这里定义你需要的全局变量 */

// 这是求解整个问题的函数
// w：题目描述中的 w（所有）
// n：题目描述中的 n
// 返回值：答案
#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <queue>
#include <ext/pb_ds/priority_queue.hpp> //pb_ds库
#define LL long long 
using namespace std;
struct node{
    LL w,h;
    node(LL W, LL H){
        w=W,h=H;
    }
};
bool operator<(node a, node b){
    if(a.w!=b.w) return a.w>b.w; 
    return a.h>b.h;  //如果长度相等，高度小的优先
} //构造小根堆的操作。
__gnu_pbds::priority_queue <node, std::less<node>, __gnu_pbds::pairing_heap_tag> q; //优先队列
int n,k,cnt;
LL temp,maxh,ans;

int main()
{
    scanf("%d",&n);
    k=2;
    for(int i=1; i<=n; i++){
        scanf("%lld",&temp);
        q.push(node(temp,1));
    }
    if((n-1)%(k-1) != 0) cnt=k-1-(n-1)%(k-1);  //判断是否要补空节点
    for (int i=1; i<=cnt; i++)
        q.push(node(0,1)); //补空节点
    cnt+=n;     //cnt为根节点个数(最初每个根节点都为其本身）
    while(cnt>1){
        temp=maxh=0;
        for(int i=1; i<=k; i++){
            temp+=q.top().w;
            maxh=max(maxh,q.top().h);
            q.pop();
        }
        ans+=temp; //维护带权路径长度之和
        q.push(node(temp, maxh+1)); //合并，高度为最高子树高度+1
        cnt-=k-1; //减少根节点
    }
    printf("%lld",ans);
    return 0;
}
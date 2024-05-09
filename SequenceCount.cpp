#include <bits/stdc++.h>
using namespace std;

const int N = 300005;

int n, d,  max_value[N], min_value[N];
vector<int> a;

long long solve(int l,int r){
    if(l==r)
        return 0;
    int mid = (l+r)>>1;
    long long ans = solve(l,mid)+solve(mid+1,r); 

    for(int i = mid+1; i<=r; ++i){
        min_value[i] = (i == mid+1)?a[i]:min(min_value[i-1],a[i]);
        max_value[i] = (i == mid+1)?a[i]:max(max_value[i-1],a[i]);
    }

    int mn = 0,mx = 0, pos = r;
    for(int i=mid; i>=l && pos > mid; --i){

        mn = (i==mid)?a[i]:min(mn,a[i]);
        mx = (i==mid)?a[i]:max(mx,a[i]);
        for(; pos>mid && max(mx, max_value[pos])-min(mn, min_value[pos]) > d; --pos);
        ans += pos - mid; 
    }
    return ans;
}

long long getAnswer(int n, int d, vector<int> a) {

    ::n = n;
    ::d = d;
    ::a = a;
    return solve(0,n-1);
}

 
 
int main() {
    int n, d;
    scanf("%d%d", &n, &d);
    vector<int> a;
    a.resize(n);
    for (int i = 0; i < n; ++i)
        scanf("%d", &a[i]);
    printf("%lld\n", getAnswer(n, d, a));
    return 0;
}
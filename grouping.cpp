#include <iostream>
#include<cstdio>
#include <vector>
using namespace std;

typedef long long ll ;

bool check( long long d , int n , int m , vector<int> &a )
{
    long long sum = 0 ;             
    int cnt = 1 ;                       

    for( int i = 0 ; i < n ; i++ )
    {
        if( a[i] > d )        
            return false ;
        sum += a[i] ;         
        if( sum > d )
        {
            sum =a [i] ;           
            cnt ++ ;
        }
    }
    return cnt <= m ;
}



bool check2( long long d , int n , int m , vector<int > &a )
{
    ll sum = 0 ;
    int cnt = 1 ;
    for( int i = 0 ;  i< n ; i++ )
    {
        if( a[i] > d )
            return false ;
        sum += a[i] ;
        if( sum > d )
        {
            sum =a[i] ;
            cnt ++ ;
        }
    }

    return cnt <= m ;
}


long long getAnswer( int n, int m, vector<int> a)
{
   
    long long l = 1 , r = 0 ;

   
    for( int i = 0 ; i < n ; i++ )
        r += a[i] ;

    
    while( l <= r )
    {
        long long mid = ( l + r ) >> 1 ;
        if( check( mid , n , m , a ) )      
            r = mid - 1 ;
        else
            l = mid + 1 ;
    }
    return r + 1 ;      
}

int main() {
    int n, m;
    scanf("%d%d", &n, &m);
    vector<int> a;
    a.resize(n);
    for (int i = 0; i < n; ++i)
        scanf("%d", &a[i]);
    printf("%lld\n", getAnswer(n, m, a));
    return 0;
}

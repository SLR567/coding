#include <iostream>
#include <vector>
using namespace std ;

int allOne ;                
vector<bool> vis[2] ;               
string ans ;            


int twoPow( int x )
{
    return 1 << x ;
}

void dfs( int u )       
{
    for( int i = 0 ; i< 2 ; i++ )
    {
        if( !vis[i][u] )
        {
            int v = ( ( u << 1 ) | i ) & allOne ;       
            vis[i][u] = 1 ;
           
            dfs( v ) ;
            ans.push_back( '0' + i ) ;
        }
    }
}


string getAnswer( int n )
{
    
    allOne = twoPow( n -1 ) -1 ;
    ans = "";
    for( int i = 0 ; i< 2 ; i++ )
        vis[i].resize( twoPow(n-1) , 0 ) ;
    dfs(0) ;
    return ans ;
}

int main() {
    int n;
    scanf("%d", &n);
    cout << getAnswer(n) << endl;
    return 0;
}
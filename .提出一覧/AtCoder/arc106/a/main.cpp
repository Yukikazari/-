#include <bits/stdc++.h>
#define _GLIBCXX_DEBUG
#define _overload3(_1,_2,_3,name,...) name
#define _rep(i,n) repi(i,0,n)
#define repi(i,a,b) for(int i=int(a);i<int(b);++i)
#define rep(...) _overload3(__VA_ARGS__,repi,_rep,)(__VA_ARGS__)
#define PI 3.14159265359
typedef long long ll;
using namespace std;

int main(){
    ll N;
    cin >> N;

    int a = 1;
    while(N > pow(3, a)){
        ll n = N - pow(3, a);
        int b = 0;
        while(n % 5 == 0){
            n /= 5;
            b += 1;
        }
        if (n == 1 && b > 0)
        {
            cout << a << " " << b << endl;
            return 0;
        }

        a += 1;
    }
    cout << -1 << endl;
    return 0;
}
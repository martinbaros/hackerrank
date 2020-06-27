#include <iostream>
#include <cstdio>
using namespace std;

/*
Add `int max_of_four(int a, int b, int c, int d)` here.
*/
int max_of_four(int a, int b, int c, int d){
    int maxo = 0;
    if (a>maxo){
        maxo = a;
    }
    if (b>maxo){
        maxo = b;
    }
    if (c>maxo){
        maxo = c;
    }
    if (d>maxo){
        maxo = d;
    }
    return maxo;
}

int main() {
    int a, b, c, d;
    scanf("%d %d %d %d", &a, &b, &c, &d);
    int ans = max_of_four(a, b, c, d);
    printf("%d", ans);

    return 0;
}

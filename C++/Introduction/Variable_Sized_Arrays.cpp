#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int n,q;
    cin >> n >> q;

    int** o = new int*[n];

    for(int i = 0; i < n; i++) {
        int k;
        cin >> k;
        o[i] = new int[k];
        for(int j = 0; j < k; j++) {
            cin >> o[i][j];
        }
    }

    // Perform queries:
    while(q-- > 0) {
        int oi, ii;
        cin >> oi >> ii;
        cout << o[oi][ii] << endl;
    }

    return 0;
}

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int n;
    vector<int> v;
    cin >> n;
    for (int i = 0; i < n; ++i){
        int q;
        cin >> q;
        v.push_back(q);
    }
    sort(v.begin(),v.end());
    for (int i:v){
        cout << i << " ";
    }
    cout << endl;
    return 0;
}

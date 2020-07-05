#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    int d,q,z,kk;
    cin >> d;
    vector<int> v;
    for (int i = 0,k;  i < d; ++i) {
        cin >> k;
        v.push_back(k);
    }
    cin >> q;
    v.erase(v.begin()+q-1);
    cin >> z >> kk;
    v.erase(v.begin()+z-1,v.begin()+kk-1);
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    cout << v.size() << endl;
    for (int i:v){
        cout << i << " ";
    }
    return 0;
}

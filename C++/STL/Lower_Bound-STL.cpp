#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    vector<int> v;
    int n,p;
    cin >> n ;
    for (int i = 0,k; i<n; i++){
        cin >> k;
        v.push_back(k);
    }

    std::sort (v.begin(), v.end());

    std::vector<int>::iterator low;

    cin >> p;
    for (int i = 0,h; i<p; i++){
        cin >> h;
        low=std::lower_bound (v.begin(), v.end(), h);
        if (v[low - v.begin()] == h){
            cout << "Yes" << " ";
        }else{
            cout << "No" << " ";
        }


        cout <<  (low- v.begin())+1 <<endl;
    }
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    return 0;
}

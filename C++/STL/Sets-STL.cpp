#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <set>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int t;
    set<int> s;
    set<int>::iterator itr;
    cin >> t;
    for (int i = 0,x,h; i < t ; ++i){
        cin >> x >> h;
        switch (x) {
            case 1:
                s.insert(h);
                break;
            case 2:
                s.erase(h);
                break;
            case 3:
                itr = s.find(h);
                if (itr != s.end()){
                    cout << "Yes" << endl;
                }else{
                    cout << "No" << endl;
                }
        }
    }
    return 0;
}

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <set>
#include <map>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    map<string, int> m;
    map<string,int>::iterator itr;
    int t;
    cin >>t;
    for (int i = 0,x; i < t; ++i){
        string p;
        cin >> x;
        switch (x) {
            case 1:
                int h;
                cin >> p >> h;
                itr = m.find(p);
                if (itr != m.end()) {
                    m[p] = m[p]+h;
                }else{
                    m.insert(make_pair(p, h));
                }

                break;
            case 2:
                cin >> p;
                m.erase(p);
                break;
            case 3:
                cin >> p;
                cout << m[p] <<endl;
                break;
        }
    }
    return 0;
}

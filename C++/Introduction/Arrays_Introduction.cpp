#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    int sizeofarray;
    cin>>sizeofarray;
    int arr[sizeofarray];
    for(int i=0; i<sizeofarray; i++)
    {
        cin>>arr[i];
    };
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    for (int i = sizeofarray; i>0; i--){
        cout << arr[i-1];
        if (i == 0){
            cout << endl;
        }else{
            cout << " ";
        }
    };
    return 0;
}

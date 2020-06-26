#include <bits/stdc++.h>

using namespace std;



int main()
{
    int n;
    cin >> n;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    // Write Your Code Here
    string nums[10] = {"one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "Greater than 9"};
    if (n <= 9){
        cout << nums[n-1];
    }else{
        cout << nums[9];
    }
    return 0;
}

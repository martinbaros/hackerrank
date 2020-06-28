#include <iostream>
#include <string>
using namespace std;

int main() {
	// Complete the program
    string a,b;
    cin >> a;
    cin >> b;
    cout << a.size() << " " << b.size() << endl;
    cout << a+b << endl;
    char p_a = a[0];
    char p_b = b[0];
    a[0] = p_b;
    b[0] = p_a;
    cout << a << " " << b <<endl;
    return 0;
}

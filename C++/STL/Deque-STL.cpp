#include <iostream>
#include <deque>
using namespace std;

void printKMax(int arr[], int n, int k){
    int pp = k;
    deque<int> max;
    for(int i = 0; i < n; i++){
        for(;!max.empty() && arr[i] > max.back();){
            max.pop_back();
        }  
        max.push_back(arr[i]);
        if(i >= pp && max.front() == arr[i-pp]){
          max.pop_front();
        }
        if(i >= pp-1){
          if (i<n-1){
            cout << max.front() << " ";
          }else{
            cout << max.front() << endl;
          }
        }

    }
}

int main(){

	int t;
	cin >> t;
	while(t>0) {
		int n,k;
    	cin >> n >> k;
    	int i;
    	int arr[n];
    	for(i=0;i<n;i++)
      		cin >> arr[i];
    	printKMax(arr, n, k);
    	t--;
  	}
  	return 0;
}

#include<iostream>
using namespace std;

int main(){
	int a,sum;
	sum = 0;
	cin>>a;
	for(int i=1; i<a+1; i++){
		sum=sum+i;
	}
	cout<<sum;
	return 0;
}
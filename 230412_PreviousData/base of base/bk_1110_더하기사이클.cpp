#include<iostream>
using namespace std;

int main(){
	cin.tie(NULL);
	ios_base::sync_with_stdio(false); 
	int a, count=0, tmp;
	cin>>a;
	tmp = a;

	do{
		tmp=tmp%10*10+((tmp/10)+tmp%10)%10;
		count++;
	}while(a!=tmp);
	cout<<count;
	return 0;
}
#include<iostream>
using namespace std;

int main(){
	cin.tie(NULL);
	ios_base::sync_with_stdio(false); 
	int num,a,b;
	cin>>num;
	for(int i=1; i<num+1; i++){
		cin>>a>>b;
		cout<<"Case #"<<i<<": "<<a+b<<"\n";
	}
	return 0;
}
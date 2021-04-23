#include<iostream>
using namespace std;

int main(){
	cin.tie(NULL);
	ios_base::sync_with_stdio(false); 
	int num,x,b;
	cin>>num>>x;
	for(int i=0; i<num; i++){
		cin>>b;
		if(b<x)
			cout<< b<< ' ';
	}
	return 0;
}
#include<iostream>
using namespace std;

int main(){
	cin.tie(NULL);
	ios_base::sync_with_stdio(false); 
	int a,mem=0,max=-1000000;
	for(int i=1; i<10; i++){
		cin>>a;
		if(a>max){
			mem=i;
			max=a;
		}
	}
	cout<<max<<"\n"<<mem;
	return 0;
}
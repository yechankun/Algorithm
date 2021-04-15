#include<iostream>
using namespace std;

int main(){
	cin.tie(NULL);
	ios_base::sync_with_stdio(false); 
	int num,a,min=1000000,max=-1000000;
	cin>>num;
	for(int i=0; i<num; i++){
		cin>>a;
		if(a<min)
			min=a;
		if(a>max)
			max=a;
	}
	cout<<min<<" "<<max;
	return 0;
}
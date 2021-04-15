#include<iostream>
using namespace std;
main(){
	int i,n,k,s=0,m=0;
	cin>>n;
	for(i=0;i<n;i++){
		cin>>k;
		if(k>m)
		    m=k;
		s+=k;
	}
	cout<<(float)s/m*100/n;
}
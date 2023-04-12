#include<iostream>
using namespace std;
main() {
	int i,n,k;
	cin>>n;
	cin.ignore();
	for (i=0;i<n;i++){
		int p=1,s=0;
		while(1){
			k=cin.get();
			if(k=='\n'||k==-1)break;
			if(k=='O')
				s+=p++;
			else
				p=1;
		}
		cout<<s<<endl;
	}
}
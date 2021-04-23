#include<iostream>
using namespace std;
main() {
	int i,a,b,c,r,s[10]={0,};
	cin>>a>>b>>c;
	r=a*b*c;
	while(r!=0) {
		s[r%10]++;
		r/=10;
	}
	for(i=0; i<10; i++)
		cout<<s[i]<<'\n';
}
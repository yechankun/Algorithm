#include<iostream>
#include<algorithm>
using namespace std;
main(){
	int i,s[10];
	for(i=0;i<10;i++){
		cin>>s[i];
		s[i]%=42;
	}
	sort(s,s+10);
	fill(unique(s,s+10),s+10,-1);
	cout<<10-count(s,s+10,-1);
}
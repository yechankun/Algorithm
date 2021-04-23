#include<iostream>
using namespace std;

int main() {
	char string[100];
	int n;
	int sum=0;

	cin >> n;
	cin >> string;
	for (int i = 0; i < n; i++) {
		sum = sum + (int)string[i]-48;
	}
	cout << sum;
}
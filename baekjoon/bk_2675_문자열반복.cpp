#include<iostream>
using namespace std;

int main() {
	int t;
	int n;
	char str[20];
	cin >> t;
	for (int i = 0; i < t; i++) {
		cin >> n >> str;
		for (auto s : str) {
			if (s == '\0')
				break;
			for (int i = 0; i < n; i++)
				cout << s;
		}
		cout << endl;
	}	
}
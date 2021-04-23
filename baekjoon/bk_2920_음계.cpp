#include<iostream>
using namespace std;

int main() {
	cin.tie(NULL);
	ios_base::sync_with_stdio(false);
	int front, check = 1;
	for (int i = 1; i < 9; i++) {
		cin >> front;
		if (front != i || check != 1) {
				check = 0;
			if (front != 9 - i) {
			    check = -1;
				break;
			}
		}
	}
	switch (check) {
	case 1: cout << "ascending"; break;
	case 0: cout << "descending"; break;
	case -1: cout << "mixed"; break;
	}
	return 0;
}
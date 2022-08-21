#include<iostream>
#include<cmath>
using namespace std;

void selfnum(int x);
int main() {
	selfnum(1);
	return 0;
}

void selfnum(int x) {
	int sum;
	int ck[10000] = { 0, };
	int count = 0;

	for (int i = 0; i < 10000; i++) {
		sum = x;
		do{
			sum = sum + (x / (int)pow(10, count)) % 10;
		} while (x / (int)pow(10, count++) != 0);
		count = 0;
		if(sum<10001)
			ck[sum-1] = 1;
		x++;
	}
	
	for (int i = 0; i < 10000; i++) {
		if (ck[i] == 0)
			cout << i + 1 << endl;
	}
}
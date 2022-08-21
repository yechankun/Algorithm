#include<iostream>
#include<stdio.h>
using namespace std;

int main()
{
	int n, m;
	cin >> n;
	n = n + 1;

	for (m = 1; m < n; m++)
		printf("%d\n", m);
	return 0;
}
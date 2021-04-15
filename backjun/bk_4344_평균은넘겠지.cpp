#include<iostream>
#include<vector>
using namespace std;
int main() {
	int i, j, n, k, m, s;
	float r;
	vector<int> a;
	cin >> n;
	for (i = 0; i < n; i++) {
		cin >> m;
		s = 0;
		for (j = 0; j < m; j++) {
			cin >> k;
			a.push_back(k);
			s += a[j];
		}
		r = (float)s / m;
		s = 0;
		for (j = 0; j < m; j++) 
			if (a[j]>r) s++;
		a.clear();
		cout.precision(3);
		cout << fixed << (double)s / m * 100<<"%"<<endl;
	}
}
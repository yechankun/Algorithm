#include<iostream>
using namespace std;

int hansu(int x);
int main() {
	int x;
	cin >> x;
	cout << hansu(x);
	return 0;
}

int hansu(int x) {
    int o, t, h, count = 0;
    if (x < 100)
        return x;
    else {
        for (int i = 100; i <= x; i++) {
            h = i / 100;
            t = (i % 100) / 10;
            o = (i % 100) % 10;
            if ((h - t) == (t - o))
                count++;
        }
        return (99 + count);
    }
}
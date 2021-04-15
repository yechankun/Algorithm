#include<iostream>
#include<vector>
using namespace std;

int main() {
	char str[101];
	int ck[26];
	std::fill_n(ck, 26, -1);
	cin >> str;

	int i = 0;
	for (auto s : str) {
		if (ck[s - 'a'] == -1)
			ck[s - 'a'] = i++;
		else
			i++;
		if (s == '\0')
			break;
	}
	for (i = 0; i < 26; i++) {
		cout << ck[i] << ' ';
	}
}
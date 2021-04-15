#include<iostream>

using namespace std;

int main()
{
	int num;
	char ps[50] = { 0, };
	char stack[50] = { 0, };
	int top = -1;
	int yesno;
	cin >> num;
	cin.get();
	for (int i = 0; i < num; i++) {
		yesno = 1;
		top = -1;
		for (int j = 0; j < 51; j++) {
			ps[j] = cin.get();
			if (ps[j] == '\n')
				break;
			if (ps[j] == '(') {
				stack[++top] = '(';
			}
			if (top == -1 && ps[j] == ')')
				yesno = 0;
			if (stack[top] == '(' && ps[j] == ')') {
				stack[top--] = 0;
			}
		}
		if (yesno == 1 && top == -1)
			cout << "YES" << endl;
		else
			cout << "NO" << endl;
	}
	return 0;
}
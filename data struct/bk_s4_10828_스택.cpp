#include<iostream>
#include<cstring>
using namespace std;

void push(int* point);

void pop(int* point);

int main()
{
	int num, i;
	char command[6];
	int a;//스택부분
	int top = -1;
	cin >> num;
	
	int *stack = new int[num];
	
	for (i = 0; i < num; i++)
	{
		cin >> command;
		if (strcmp(command, "push") == 0) {
			push(stack + top++);		
		}
		else if (strcmp(command, "pop") == 0){
			if (top>-1)
				pop(stack + --top);
			else
				cout << -1 << endl;
		}
		else if (strcmp(command, "size") == 0){
			cout << top + 1 << endl;
		}
		else if (strcmp(command, "empty") == 0){
			if (top == -1)
				cout << 1 << endl;
			else
				cout << 0<< endl;
		}
		else if (strcmp(command, "top") == 0) {
			if(top == -1)
				cout << -1 << endl;
			else
				cout << *(stack + top -1) << endl;
		}
		command[0] = '\0';
	}
	return 0;
}

void push(int* point) {
	cin >> *point;
}

void pop(int* point) {
	cout << *point << endl;
}
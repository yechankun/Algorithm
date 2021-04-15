#include<stdio.h>

int main()
{
	int a = 5 * 60, b = 1 * 60, c = 10;
	int time;

	scanf(" %d", &time);

	if (time%c == 0) {
		printf("%d ", time / a);
		printf("%d ", (time%a) / b);
		printf("%d", ((time%a) % b) / c);
	}
	else
		printf("-1");
	return 0;
}
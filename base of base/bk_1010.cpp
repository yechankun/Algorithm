#include<stdio.h>

int main()
{
	int test, m, n, i;
	int com[30][30] = { 0 };

	for (i = 0; i < 30; i++)
		com[i][0] = i + 1;
	for (m = 1; m < 30; m++)
		for (n = 1; n < 30; n++)
			com[m][n] = com[m - 1][n - 1] + com[m - 1][n];
	scanf("%d", &test);

	for (i = 0; i < test; i++)
	{
		scanf("%d %d", &n, &m);

		printf("%d\n", com[m-1][n-1]);
	}
    return 0;
}
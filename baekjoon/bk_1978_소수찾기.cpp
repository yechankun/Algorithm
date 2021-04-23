#include<stdio.h>

int main()
{
	int n, i, o, sum, num = 0;
	int namuzi[1000];
	int a[100];

	scanf("%d", &n);

	for (i = 1; i <= n; i++){   //3
		scanf("%d", &a[i]);
		sum = 0;
		for (o = 1; o <= a[i]; o++){//
			namuzi[i] = a[i] % o;
			if (namuzi[i] == 0){
				sum++;
			}
		}
		if (sum == 2){
			num++;
		}
	}
	printf("%d", num);
}
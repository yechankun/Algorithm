#include<stdio.h>
#include<string.h>
int m, n;
int count;
int bachu[51][51];

int think(int y, int x){
	if (bachu[y][x] == 1 && x >= 0 && y >= 0 && x < m&&y < n){
		return 1;
	}
	else
		return 0;
	
}
int pop(int y, int x){
	bachu[y][y] = 1;
	return 0;
}
int push(int y, int x){
	bachu[y][x] = 0;
	return 0;
}
int search(int y, int x){
	if (think(y, x) == 1){
		bachu[y][x] = 0;
		if (think(y, x + 1) == 1){
			search(y, x + 1);
		}
		if (think(y, x - 1) == 1){
			search(y, x - 1);
		}
		if (think(y + 1, x) == 1){
			search(y + 1, x);
		}
		if (think(y - 1, x) == 1){
			search(y - 1, x);
		}
		return 1;
	}
	else
		return 0;
}


int main(){
	int num, test, x, y, f = 0;
	scanf("%d", &test);
	while (f < test){
		memset(bachu, 0, sizeof(bachu));
		count = 0;
		scanf("%d %d %d", &m, &n, &num);

		for (int i = 0; i < num; i++){
			scanf("%d %d", &x, &y);
			bachu[y][x] = 1;
		}
		for (int o = 0; o < n; o++){
			for (int k = 0; k < m; k++){
				if (search(o, k) == 1)
					count++;
			}
		}
		f++;
		printf("%d\n", count);
	}
	return 0;
}
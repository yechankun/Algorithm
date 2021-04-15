#include<stdio.h>

int main()
{
	int input,line,star;
	scanf("%d",&input);
	if(input>=0)
		for(line=0;line<=input-1;line++){
			for(star=0;star<=line;star++){
			printf("*");
			}
		printf("\n");
	}
}
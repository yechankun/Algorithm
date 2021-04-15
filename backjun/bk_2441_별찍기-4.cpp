#include<stdio.h>

int main()
{
	int input,line,star;
	scanf("%d",&input);
	if(input>=0)
		for(line=input;line>0;line--){
			for(star=1;star<=line;star++){
				printf("*");
			}
		printf("\n");
	}
}
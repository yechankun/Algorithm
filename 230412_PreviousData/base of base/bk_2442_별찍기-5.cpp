#include<stdio.h>

int main()
{
	int input,blank,line,star;
	scanf("%d",&input);
	if(input>=0)
		for(line=1;line<=input;line++){
			for(blank=0;blank<input-line;blank++){
				printf(" ");
			}
			for(star=1;star<=2*line-1;star++){
				printf("*");
			}
		printf("\n");
	}
}
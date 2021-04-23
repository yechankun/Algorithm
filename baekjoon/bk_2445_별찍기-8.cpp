#include<stdio.h>

int main()
{
	int input,blank,line,star;
	scanf("%d",&input);
	for(line=1;line<=input*2-1;line++){
		if(line<=input){
			for(star=1;star<=line;star++){
				printf("*");
			}
			for(blank=0;blank<input*2-(2*line);blank++){
				printf(" ");
			}
			for(star=1;star<=line;star++){
				printf("*");
			}
		}
		else{
			for(star=1;star<=input*2-line;star++){
				printf("*");
				}
			for(blank=0;blank<(2*line)-(input*2);blank++){
				printf(" ");
				}
			for(star=1;star<=input*2-line;star++){
				printf("*");
			}
		}
			printf("\n");
	}
}
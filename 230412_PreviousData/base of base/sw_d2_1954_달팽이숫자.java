//https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PobmqAPoDFAUq&categoryId=AV5PobmqAPoDFAUq&categoryType=CODE&problemTitle=1954&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1
import java.util.Scanner;

public class sw_d2_1954_달팽이숫자 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		int input;
		int[][] map;
		
		//우, 하, 좌, 상 반복
		int[] dr = {0, 1, 0, -1};
		int[] dc = {1, 0, -1, 0};
		
		
		for(int test=1; test<=T; test++) {
			input = sc.nextInt();
			map = new int[input][input];
			map[0][0] = 1;
			int nr=0, nc=1;
			if(input != 1)
				out:
				for(int i= 0, j = 0, num=2, d=0; i<input; i++) {
					
					for(j=0; j<input; j++) {
						map[nr][nc] = num++;
						nr += dr[d];
						nc += dc[d];
						if(nr > input - 1 || nc < 0 || nc > input - 1 || map[nr][nc] != 0) {
							nr -= dr[d];
							nc -= dc[d];
							d = (++d)%4;	
							nr += dr[d];
							nc += dc[d];
							if(map[nr][nc] != 0)
								break out;
						}
						
					}
			}
			System.out.println("#"+test);
			
			for(int[] i: map) {
				for(int j: i) {
					System.out.printf("%d ", j);
				}
				System.out.println();
			}
		}
	}
}

// https://swexpertacademy.com/main/code/userProblem/userProblemDetail.do?contestProbId=AWlHcsEqf1YDFASG

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

// 중복순열
public class SW_D4_7208_지도칠하기 {
	static int color = 4, countryCnt, min;
	static int[] colorNums;
	static int[] inputColors;
	static int[][] country;
	static int testcase;

	public static void permutation(int cnt) {
		if (cnt == countryCnt) { // 모든 순열을 다 뽑은 상태		
			int dC =0;
			//인접되어 있고 색상이 같으면 리턴
			for(int i = 0, j=0; i<countryCnt-1; i++) {
				for(j = i+1; j<countryCnt; j++) {
					if(country[i][j] == 1 && colorNums[i] == colorNums[j]) {
						return;
					}
				}
			}
			for (int i = 0; i < countryCnt; i++) {
				//기존에 배치된 색과  새로 칠한 색이 다르면
				if(colorNums[i] != inputColors[i]) {
					dC++;			//
				}
			}
			min = Math.min(dC, min);
			return;
		}
		for (int i = 1; i <= color; i++) {
			colorNums[cnt] = i;
			permutation(cnt + 1);
		}
	}

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		int testcase = Integer.parseInt(br.readLine());
		
		for (int i = 1, j = 0, k = 0; i <= testcase; i++) {
			countryCnt = Integer.parseInt(br.readLine().trim());
			st = new StringTokenizer(br.readLine().trim());
			
			inputColors = new int[countryCnt];
			colorNums = new int[countryCnt];
			
			country = new int[countryCnt][countryCnt];
			for (j = 0; j < countryCnt; j++) {
				inputColors[j] = Integer.parseInt(st.nextToken().trim());
			}
			for (j = 0; j < countryCnt; j++) {
				st = new StringTokenizer(br.readLine().trim());
				for (k = 0; k < countryCnt; k++)
					country[j][k] = Integer.parseInt(st.nextToken().trim());
			}
			
			min = Integer.MAX_VALUE;
			permutation(0);
			
			System.out.printf("#%d %d\n", i, min);
		}
	}
}
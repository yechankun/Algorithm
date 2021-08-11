package com.ssafy.combination;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class SW_D3_5215{
	static int N, R, L;
	static int[] numbers;
	static int T[], K[];
	static int testcase, max_score;
	
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		testcase = Integer.parseInt(in.readLine().trim());
		
		StringTokenizer st;
		for(int i=1; i<=testcase; i++) {
			max_score = Integer.MIN_VALUE;
			st = new StringTokenizer(in.readLine().trim());
			N = Integer.parseInt(st.nextToken().trim());		
			L = Integer.parseInt(st.nextToken().trim());
			
			T = new int[N];
			K = new int[N];
			for(int j=0; j<N;j++) {
				st = new StringTokenizer(in.readLine().trim());
				T[j] = Integer.parseInt(st.nextToken().trim());
				K[j] = Integer.parseInt(st.nextToken().trim());
			}
			
			
			numbers = new int[N];
			combination(0, 0, 0);
			
			System.out.printf("#%d %d\n", i, max_score);
		}		
	}
	
	private static void combination(int cnt, int kal_sum, int t_sum) {
		if(kal_sum > L) {
			return;
		}
		if(cnt == N) {
			max_score = Math.max(t_sum, max_score);
			System.out.println(Arrays.toString(numbers));
			return;
		}
		
		numbers[cnt] = K[cnt];

		combination(cnt+1, kal_sum+K[cnt], t_sum+T[cnt]);
		combination(cnt+1, kal_sum, t_sum);
	}
}

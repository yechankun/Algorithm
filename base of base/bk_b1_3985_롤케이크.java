package com.ssafy.im;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class bk_b1_3985_롤케이크 {

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int L = Integer.parseInt(br.readLine());
		int N = Integer.parseInt(br.readLine());
		int rollcake[] = new int[L + 1];
		
		int maxwant = Integer.MIN_VALUE;
		int maxwant_idx = -1;
		int maxtaken = Integer.MIN_VALUE;
		int maxtaken_idx = -1;

		StringTokenizer st;
		for (int i = 1; i <= N; i++) {
			st = new StringTokenizer(br.readLine());
			int left = Integer.parseInt(st.nextToken());
			int right = Integer.parseInt(st.nextToken());
			if(maxwant < right-left) {
				maxwant = right-left;
				maxwant_idx = i;
			}
			int sum = 0;
			for(;left <= right; left++) {
				if(rollcake[left] == 0) {
					rollcake[left] = i; sum++;
				}
			}
			if(maxtaken < sum) {
				maxtaken = sum;
				maxtaken_idx = i;
			}
		}
		System.out.println(maxwant_idx);
		System.out.println(maxtaken_idx);
	}
}

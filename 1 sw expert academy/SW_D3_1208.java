package com.ssafy;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class SW_D3_1208 {

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		int testCase = 10;
		int dump;
		int[] height = new int[100];
		int num=0, sum = 0, avg = 0;
		for (int i = 1, j = 0, k=0; i <= testCase; i++) {
			dump = Integer.parseInt(br.readLine());
			st = new StringTokenizer(br.readLine());
			//입력
			for (j = 0; j < 100; j++) {
				height[j] = Integer.parseInt(st.nextToken());
			}
			Arrays.sort(height);
			for (j = 0; j < dump; j++) {
				height[0]++;
				height[99]--;
				//좌측에 오른쪽 값보다 큰 값이 들어올 경우
				for (k = 0; height[k] > height[k + 1]; k++) {
					height[k] ^= height[k + 1];
					height[k + 1] ^= height[k];
					height[k] ^= height[k + 1];
				}
				//우측에 왼쪽 값보다 작은 값이 달라질 경우
				for (k = 99; height[k] < height[k - 1]; k--) {
					height[k] ^= height[k - 1];
					height[k - 1] ^= height[k];
					height[k] ^= height[k - 1];
				}
			}
			System.out.printf("#%d %d\n", i, height[99] - height[0]);
		}
	}

}

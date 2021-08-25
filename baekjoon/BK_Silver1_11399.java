package com.ssafy.im;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class BK_Silver1_11399 {

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		int N = Integer.parseInt(br.readLine());
		int output[] = new int[N];
		StringTokenizer st = new StringTokenizer(br.readLine());
		for (int i = 0; i < N; i++) {
			output[i] = Integer.parseInt(st.nextToken());
		}
		Arrays.sort(output);
		int sum = 0;
		int answer = 0;
		for (int i = 0; i < N; i++) {
			answer += sum += output[i];
		}
		System.out.println(answer);
	}
}

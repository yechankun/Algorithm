package com.ssafy.im;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class SW_D3_1209 {

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		for (int tc = 0; tc < 10; tc++) {
			int T = Integer.parseInt(br.readLine());
			int rowsum[] = new int[100];
			int colsum[] = new int[100];
			int leftdown = 0, rightdown = 0;

			StringTokenizer st;
			for (int i = 0; i < 100; i++) {
				st = new StringTokenizer(br.readLine(), " ");
				int sum = 0;
				for (int j = 0; j < 100; j++) {
					int in = Integer.parseInt(st.nextToken());
					sum += in;
					colsum[j] += in;

					if (i == j)
						leftdown += in;
					if (i == 99 - j)
						rightdown += in;
				}
				rowsum[i] = sum;
			}
			int a = Arrays.stream(rowsum).max().getAsInt();
			int b = Arrays.stream(colsum).max().getAsInt();

			int maxs[] = { a, b, leftdown, rightdown };

			System.out.printf("#%d %d%n", T, Arrays.stream(maxs).max().getAsInt());
		}
	}

}

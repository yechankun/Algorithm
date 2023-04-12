package com.ssafy.im;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class bk_s3_2477_참외밭 {

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		int K = Integer.parseInt(br.readLine());

		int bean[] = new int[6];
		StringTokenizer st;
		int maxW = 0, maxH = 0;
		for (int i = 0; i < 6; i++) {
			st = new StringTokenizer(br.readLine());
			Integer.parseInt(st.nextToken());
			bean[i] = Integer.parseInt(st.nextToken());
			if (i % 2 == 0) {
				maxW = Math.max(bean[i], maxW);
			} else {
				maxH = Math.max(bean[i], maxH);
			}
		}
		int big = maxW * maxH;
		int smallW = 0, smallH = 0;
		for (int i = 0; i < 6; i++) {
			if (i % 2 == 0) {
				if (bean[(i + 5) % 6] + bean[(i + 1) % 6] == maxH) {
					smallW = bean[i];
				}
			} else {
				if (bean[(i + 5) % 6] + bean[(i + 1) % 6] == maxW) {
					smallH = bean[i];
				}
			}
		}
		int diff = smallW * smallH;
		System.out.println(K * (big - diff));
	}
}

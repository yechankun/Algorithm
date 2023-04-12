package com.ssafy.im;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class jo_1523_별삼각형1 {

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int n = Integer.parseInt(st.nextToken());
		int m = Integer.parseInt(st.nextToken());

		if (0 > n || 100 < n) {
			System.out.print("INPUT ERROR!");
			return;
		}
		switch (m) {
		case 1:
			for (int i = 0; i < n; i++) {
				for (int j = -1; j < i; j++) {
					System.out.print("*");
				}
				System.out.println();
			}
			break;
		case 2:
			for (int i = n; i >= 0; i--) {
				for (int j = 0; j < i; j++) {
					System.out.print("*");
				}
				System.out.println();
			}
			break;
		case 3:
			for (int i = 0; i < n; i++) {
				for (int j = 1; j < n - i; j++) {
					System.out.print(" ");
				}

				for (int k = 0; k < 2 * i + 1; k++) {
					System.out.print("*");
				}
				System.out.println();
			}
			break;
		default:
			System.out.print("INPUT ERROR!");
		}
	}

}

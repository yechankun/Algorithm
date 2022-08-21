package com.ssafy.im;

import java.util.Scanner;

public class bk_b1_2999_비밀이메일 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String message = sc.nextLine();
		int N = message.length();
		int R, C;
		for (R = (int) Math.sqrt(N); N % R != 0; R--) {
		}
		C = N / R;
		char[][] convert = new char[R][C];
		for (int col = 0, index = 0; col < C; col++)
			for (int row = 0; row < R; row++) {
				convert[row][col] = message.charAt(index++);
			}

		StringBuilder sb = new StringBuilder();
		for (int i = 0; i < R; i++)
			sb.append(convert[i]);

		System.out.print(sb.toString());
	}
}

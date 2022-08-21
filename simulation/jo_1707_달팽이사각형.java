package com.ssafy.im;

import java.util.Scanner;

public class jo_1707_달팽이사각형 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int n = sc.nextInt();
		int[][] map = new int[n][n];

		int move = n, row = 0, col = -1, cnt = 1;
		while (move > 0) {
			for (int i = 0; i < move; i++)
				map[row][++col] = cnt++;
			move--;
			for (int i = 0; i < move; i++)
				map[++row][col] = cnt++;
	
			for (int i = 0; i < move; i++)
				map[row][--col] = cnt++;
			move--;
			for (int i = 0; i < move; i++)
				map[--row][col] = cnt++;
		}
		
		StringBuilder sb = new StringBuilder();
		for(int r[] : map) {
			for(int c : r) {
				sb.append(c).append(' ');
			}
			sb.append('\n');
		}
		System.out.print(sb.toString());
	}

}

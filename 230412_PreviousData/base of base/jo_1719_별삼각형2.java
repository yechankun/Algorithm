package com.ssafy.im;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class jo_1719_별삼각형2 {

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int n = Integer.parseInt(st.nextToken());
		int m = Integer.parseInt(st.nextToken());

		if (0 > n || 100 < n || n % 2 == 0) {
			System.out.print("INPUT ERROR!");
			return;
		}
		
		switch (m) {
		case 1:
			for (int i = 0; i < n/2; i++) {
				for (int j = -1; j < i; j++) {
					System.out.print("*");
				}
				System.out.println();
			}
			for (int i = n/2; i > -1; i--) {
				for (int j = -1; j < i; j++) {
					System.out.print("*");
				}
				System.out.println();
			}
			break;
		case 2:
			for (int i = 0; i < n/2; i++) {
				for (int j = n/2 - i; j > 0; j--) {
					System.out.print(" ");
				}
				for (int j = -1; j < i; j++) {
					System.out.print("*");
				}
				System.out.println();
			}
			for (int i = n/2; i > -1; i--) {
				for (int j = 0; j < n/2-i; j++) {
					System.out.print(" ");
				}
				for (int j = -1; j < i; j++) {
					System.out.print("*");
				}
				System.out.println();
			}
			break;
		case 3:
			for (int i = 0; i < n/2; i++) {
				for (int j = 0; j < i; j++) {
					System.out.print(" ");
				}
				for (int j = -1; j<(n/2-i)*2; j++) {
					System.out.print("*");
				}
				System.out.println();
			}
			for (int i = n/2; i > -1; i--) {
				for (int j = 0; j < i; j++) {
					System.out.print(" ");
				}
				for (int j = -1; j<(n/2-i)*2; j++) {
					System.out.print("*");
				}
				System.out.println();
			}
			break;
		case 4:
			for (int i = n/2; i > -1; i--) {
				for (int j = 0; j < n/2-i; j++) {
					System.out.print(" ");
				}
				for (int j = -1; j < i; j++) {
					System.out.print("*");
				}
				System.out.println();
			}
			for (int i = 0; i < n/2; i++) {
				for(int j=0; j<n/2; j++)
					System.out.print(" ");
				for (int j = -2; j < i; j++) {
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

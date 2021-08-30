package com.ssafy.im;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class SW_D3_4615{

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(br.readLine());
		StringTokenizer st;

		int[] dr = { -1, 1, 0, 0, -1, -1, 1, 1 };
		int[] dc = { 0, 0, -1, 1, -1, 1, -1, 1 };
		int rock[] = {0, 2, 2};
		for (int tc = 1; tc <= T; tc++) {
			st = new StringTokenizer(br.readLine());
			int N = Integer.parseInt(st.nextToken());
			int[][] map = new int[N][N];

			// 바둑판 초기화
			int half_N = N / 2;
			map[half_N][half_N] = 2;
			map[half_N - 1][half_N - 1] = 2;
			map[half_N][half_N - 1] = 1;
			map[half_N -1][half_N] = 1;
			int M = Integer.parseInt(st.nextToken());
			
			for (int i = 0; i < M; i++) {
				st = new StringTokenizer(br.readLine());
				int row = Integer.parseInt(st.nextToken()) - 1;
				int col = Integer.parseInt(st.nextToken()) - 1;
				map[row][col] = Integer.parseInt(st.nextToken());
				rock[map[row][col]]++;
				for (int j = 0, nr, nc; j < 8; j++) {
					nr = row + dr[j];
					nc = col + dc[j];
					boolean flag = false;
					while(nr > -1 && nr < N && nc > -1 && nc < N && map[nr][nc] != 0) {					
						if(map[nr][nc] == map[row][col]) { 
							flag = true;
							break;
						}
						nr += dr[j];
						nc += dc[j];						
					}
					if(flag) {
						while(nr != row || nc != col) {
							nr -= dr[j];
							nc -= dc[j];
							rock[map[row][col]]++;
							rock[map[nr][nc]]--;
							map[nr][nc] = map[row][col];
						}
					}	
				}
			}
			System.out.printf("#%d %d %d%n", tc, rock[1], rock[2]);
			rock[1] = rock[2] = 2;
		}
	}

}

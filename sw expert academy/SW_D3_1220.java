package com.ssafy.im;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class SW_D3_1220 {

	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		for(int tc=1; tc<=10; tc++) {
			int map[][] = new int[100][100];
			
			br.readLine();
			//접근 속도를 위해 행 열 뒤집어버리기.
			StringTokenizer st;
			for(int row =0;row<100; row++) {
				st = new StringTokenizer(br.readLine());
				for(int col = 0; col<100; col++) {
					map[col][row] = Integer.parseInt(st.nextToken()); 
				}
			}
			int answer = 0;
			boolean ck;	
			//왼쪽 오른쪽으로 N과 S가 놓인 테이블이라고 생각하면 됨.
			for(int row=0; row<100; row++) {
				ck = true;	//N극(==1)을 만날 수 있는 상태
				for(int col=0; col<100; col++) {
					if(ck && map[row][col]==1) {
						ck = false;
					}else if(!ck && map[row][col]==2) {
						ck = true;
						answer++;
					}
				}
			}
			System.out.println("#"+tc+" "+answer);
		}
	}
}

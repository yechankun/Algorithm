//https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PnnU6AOsDFAUq&categoryId=AV5PnnU6AOsDFAUq&categoryType=CODE&problemTitle=1948&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1
package com.ssafy.im;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class sw_d2_1948_날짜계산기 {
	public static void main(String[] args) throws Exception {
		int date_vol[] = { 0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 };

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		int T = Integer.parseInt(br.readLine().trim());
		StringTokenizer st;
		for (int tc = 1; tc <= T; tc++) {
			st = new StringTokenizer(br.readLine());
			int startM =  Integer.parseInt(st.nextToken());
			int startD =  Integer.parseInt(st.nextToken());
			int endM =  Integer.parseInt(st.nextToken());
			int endD =  Integer.parseInt(st.nextToken());
			
			int diffDate = startM == endM ? endD-startD : date_vol[startM]-startD+endD;
			for(int i=startM+1; i<endM&&i<14; i++) {
				diffDate += date_vol[i];
			}
			System.out.printf("#%d %d%n", tc, ++diffDate);
		}
	}

}

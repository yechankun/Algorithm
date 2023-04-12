package com.ssafy.recursive;
//ㅠㅠ 백준에서 패키지 들어가면 오류 생긴다는 것 잊고 런타임 에러가 배열부분에서 생기는가 싶어서 계속 디버깅 해보다 2시간을 날렸습니다.. 
//import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class bk_s4_1244_스위치켜고끄기 {
	public static void BK(String[] args) throws FileNotFoundException {
//		System.setIn(new FileInputStream("input.txt")); // 왔다갔다하면됨.
		Scanner sc = new Scanner(System.in);

		int switchCnt = sc.nextInt() + 1;
		int[] swit = new int[switchCnt];
		for (int i = 1; i < switchCnt; i++) { // 번호가 1부터 시작이므로 공간을 소모해서 연산을 줄임
			swit[i] = sc.nextInt();
		}

		int stuNum = sc.nextInt();
		int gender = 0, switchNum = 0, gl = 0, gr = 0;
		for (int i = 0; i < stuNum; i++) {
			gender = sc.nextInt();
			switchNum = sc.nextInt();

			if (gender == 1) { // 남자
				for (int j = switchNum; j < switchCnt; j += switchNum)
					swit[j] ^= 1; // 토글
			} else { // 여자
				gl = switchNum - 1;
				gr = switchNum + 1;
				swit[switchNum] ^= 1; // 토글
				while (true) {
					//앞행이 체크되면 후행은 체크 안됨.
					if (gl == 0 || gr == switchCnt || swit[gl] != swit[gr] ) 
						break;
					swit[gl--] ^= 1;
					swit[gr++] ^= 1;
				}					
			}
		}
		for (int i = 1; i < switchCnt; i++) {
			System.out.print(swit[i] + " ");
			if (i % 20 == 0)
				System.out.println();
		}
	}
}

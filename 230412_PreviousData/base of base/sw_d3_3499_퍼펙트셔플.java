//https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWGsRbk6AQIDFAVW
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class sw_d3_3499_퍼펙트셔플 {

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int T = Integer.parseInt(br.readLine())+1;
		String[] cards;
		StringBuilder sb = new StringBuilder();
		int N, half;

		for (int i = 1, j=0; i < T; i++) {
			N = Integer.parseInt(br.readLine());
			cards = br.readLine().split(" ");
			
			sb.append("#"+i);
			half = (N+1)/2;
			//뒤섞은 카드 순서는 0 3 1 4 2 5 가된다 [짝수 i, 홀수 (N+1)/2+i]
			for(j=0; j <half; j ++) {
				if(j == half - 1) {
					if(N%2 == 1) {//홀수면
						sb.append(" " +cards[j]);
						break;
					}
				}
				sb.append(" " + cards[j]);
				sb.append(" " +cards[half+j]);
			}
			System.out.println(sb);
			sb.setLength(0);
		}
	}
}

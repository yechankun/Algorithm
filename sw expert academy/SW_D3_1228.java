import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.StringTokenizer;

public class SW_D3_1228 {
	public static void main(String[] args) throws NumberFormatException, IOException {
		LinkedList<String> cryptolist = new LinkedList<>();
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N, order_N, x, y;
		StringBuilder sb = new StringBuilder();

		StringTokenizer st;
		for (int testcase = 1, i, j; testcase <= 10; testcase++) {
			N = Integer.parseInt(br.readLine());

			st = new StringTokenizer(br.readLine());
			for (i = 0; i < N; i++)
				cryptolist.add(st.nextToken());

			order_N = Integer.parseInt(br.readLine());
			st = new StringTokenizer(br.readLine());
			for (i = 0; i < order_N; i++) {
				st.nextToken();
				x = Integer.parseInt(st.nextToken());
				y = Integer.parseInt(st.nextToken());

				for (j = 0; j < y; j++) {
					cryptolist.add(x++, st.nextToken());
				}
			}
			sb.append("#"+testcase);
			
			for(i=0; i<10; i++) {
				sb.append(" "+cryptolist.get(i));
			}
			System.out.println(sb);
			sb.setLength(0);
			cryptolist.clear();
		}
	}
}

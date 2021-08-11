import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BK_Silver5_2563 {

	public static void BK(String[] args) throws NumberFormatException, IOException {
			int[][] map = new int[100][100];
			
			BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
			
			int N = Integer.parseInt(br.readLine());
			int sum = 0, start_r, start_c;
			for(int i =0; i<N; i++) {
				StringTokenizer st = new StringTokenizer(br.readLine(), " ");
				start_c = Integer.parseInt(st.nextToken());
				start_r = Integer.parseInt(st.nextToken());
				for(int j = start_r; j < start_r + 10; j++) {
					for(int k = start_c;k < start_c + 10;k++) {
						if (map[j][k] != 1) {
							map[j][k] = 1;
							sum++;
						}
					}
				}
			}
			System.out.println(sum);
	}
}

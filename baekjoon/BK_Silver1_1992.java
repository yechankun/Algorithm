import java.io.BufferedReader;
import java.io.InputStreamReader;

public class BK_Silver1_1992 {
	static char map[][];
	static StringBuilder sb;

	static void dfs(int size, int start_r, int start_c) {
		boolean flag, ck = true;
		out: for (int i = start_r; i < start_r + size; i++) {
			flag = map[start_r][start_c] == '0';
			for (int j = start_c; j < start_c + size; j++) {
				if (flag != (map[i][j] == '0')) {
					ck = false;
					break out;
				}
			}
		}
		if (ck) {
			sb.append(map[start_r][start_c]);
			return;
		}

		int mid_size = size / 2;

		sb.append('(');
		dfs(mid_size, start_r, start_c);
		dfs(mid_size, start_r, start_c + mid_size);
		dfs(mid_size, start_r + mid_size, start_c);
		dfs(mid_size, start_r + mid_size, start_c + mid_size);
		sb.append(')');
	}

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		sb = new StringBuilder();
		int N = Integer.parseInt(br.readLine());

		map = new char[N][N];
		for (int i = 0; i < N; i++) {
			map[i] = br.readLine().toCharArray();
		}

		dfs(N, 0, 0);

		System.out.print(sb.toString());
	}
}

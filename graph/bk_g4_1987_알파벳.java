import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class bk_g4_1987_알파벳 {
	static int R, C;
	static char[][] board;
	
	static int[] dx = { -1, 1, 0, 0 };
	static int[] dy = { 0, 0, -1, 1 };
	
	static int max = Integer.MIN_VALUE;
	static boolean[] visit = new boolean[26];

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		R = Integer.parseInt(st.nextToken());
		C = Integer.parseInt(st.nextToken());
		
		board = new char[R][];
		for(int i=0; i<R; i++) {
			board[i] = br.readLine().toCharArray();
		}
		
		dfs(0, 0, 0);
		System.out.println(max);
	}
	
	public static void dfs(int r, int c, int count) {
		if (visit[board[r][c]-'A']) { 
			max = Math.max(max, count); 
			return;
		} else {
			visit[board[r][c]-'A'] = true;
			for (int i = 0; i < 4; i++) {
				int cx = r + dx[i];
				int cy = c + dy[i];
				if (cx >= 0 && cy >= 0 && cx < R && cy < C) {
					dfs(cx, cy, count + 1);
				}

			}
			visit[board[r][c]-'A'] = false;
		}
	}
}

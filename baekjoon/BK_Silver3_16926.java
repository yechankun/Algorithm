import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class BK_Silver3_16926 {
	static String[][] map;
	static int N, M, R;
	
	static int[] dr = {1, 0, -1, 0};
	static int[] dc = {0, 1, 0, -1};
	static private void dfs(int sr, int sc, int n, int m, int cnt) {
		if(m == 0 || n == 0)
			return;
		Queue<String> queue = new LinkedList<>();
		int nr=sr, nc=sc, nd=0;
		queue.offer(map[sr][sc]);
		for(int i=0; i<m*2+(n-2)*2 + cnt; i++) {
			nr += dr[nd];
			nc += dc[nd];
			
			if(nr < sr || nr == sr + n || nc < sc || nc == sc + m) {
				nr -= dr[nd];
				nc -= dc[nd++];
				nd = nd == 4 ? 0 : nd;
				nr += dr[nd];
				nc += dc[nd];
			}
			queue.offer(map[nr][nc]);
			if(queue.size() == cnt + 1) {
				map[nr][nc] = queue.poll();
			}
		}
		dfs(sr+1, sc+1, n-2, m-2, cnt);
	}

	public static void BK(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		R = Integer.parseInt(st.nextToken());
		
		map = new String[N][M];
		for(int i=0; i<N; i++) {
			st = new StringTokenizer(br.readLine());
			for(int j =0; j<M; j++)
				map[i][j] = st.nextToken();
		}
		dfs(0, 0, N, M, R);
		
		StringBuilder sb = new StringBuilder();
		for(String[] s : map) {
			for(String i : s)
				sb.append(i +" ");
			sb.append("\n");
		}
		System.out.print(sb.toString());
	}
}


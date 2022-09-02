import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class bk_g2_3109_빵집 {
	// dfs와 백트래킹, 그리디
	// 메모이제이션, map으로 메모이제이션 가능
	static int R, C, count;
	static char map[][];
	static int[] dr = { -1, 0, 1 };	
	//항상 윗쪽을 먼저 dfs로 탐색해주어야 그리디로 최선의 결과가 나옴.

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		R = Integer.parseInt(st.nextToken());
		C = Integer.parseInt(st.nextToken()) - 1; //기저조건에서 열의 크기-1만 씀

		map = new char[R][];
		for (int i = 0; i < R; i++) {
			map[i] = br.readLine().toCharArray();
		}
		for(int i=0; i< R; i++) {	// 그리디하게 풀기 위해 row 0부터 아래로 dfs
			dfs(i, 0);
		}
		System.out.println(count);
	}

	private static boolean dfs(int row, int column) {
		for(int i = 0; i<3; i++) {
			int nr = row + dr[i];
			int nc = column + 1;
			if(nr > -1 && nr < R && map[nr][nc] == '.') {
				if(nc == C) {
					count++;
					return true;
				}
				map[nr][nc] = 'V';
				if(dfs(nr, nc))
					return true;
			}
		}
		return false;
	}
}

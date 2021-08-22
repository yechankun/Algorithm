import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BK_Silver2_1780 {
	static int[][] paper;
	static int[] cCnt = {0,0,0};
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		
		StringTokenizer st;
		paper = new int[N][N];
		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < N; j++) {
				paper[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		colorCnt(N, 0, 0);
		for(int cnt : cCnt)
			System.out.println(cnt);
	}

	static void colorCnt(int size, int start_r, int start_c) {
		int color = checkFull(size, start_r, start_c);
		if(color != -2) {
			cCnt[color+1]++;
			return;
		}

		int tri_divide_size = size / 3;
		for(int i=0; i<3; i++)
			for(int j=0; j<3; j++)
				colorCnt(tri_divide_size, start_r+tri_divide_size*i, start_c+tri_divide_size*j);
	}
	
	static int checkFull(int size, int start_r, int start_c) {
		int color = paper[start_r][start_c];
		for (int i = start_r; i < start_r + size; i++) {
			for (int j = start_c; j < start_c + size; j++) {
				if (paper[i][j] != color) {
					return -2;
				}
			}
		}
		return color;
	}
}

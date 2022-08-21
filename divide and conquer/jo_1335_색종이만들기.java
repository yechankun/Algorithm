import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class jo_1335_색종이만들기 {
	static int[][] paper;
	static int white, blue;
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
		System.out.println(white);
		System.out.println(blue);
	}

	static void colorCnt(int size, int start_r, int start_c) {
		int color = checkFull(size, start_r, start_c);
		if(color != -1) {
			if(color == 1)blue++;
			else white++;
			return;
		}

		int mid_size = size / 2;
		colorCnt(mid_size, start_r, start_c);
		colorCnt(mid_size, start_r, start_c + mid_size);
		colorCnt(mid_size, start_r + mid_size, start_c);
		colorCnt(mid_size, start_r + mid_size, start_c + mid_size);
	}
	
	static int checkFull(int size, int start_r, int start_c) {
		int color = paper[start_r][start_c];
		for (int i = start_r; i < start_r + size; i++) {
			for (int j = start_c; j < start_c + size; j++) {
				if (paper[i][j] != color) {
					return -1;
				}
			}
		}
		return color;
	}
}


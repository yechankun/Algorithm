import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class SW_test_4012{
	static int T, N, synergy[][], min, select1[], select2[], half_N;
	static boolean selected[];

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		T = Integer.parseInt(br.readLine());

		StringTokenizer st;
		for (int tc = 1; tc <= T; tc++) {
			N = Integer.parseInt(br.readLine());
			half_N = N/2;
			synergy = new int[N][N];
			for (int i = 0; i < N; i++) {
				st = new StringTokenizer(br.readLine());
				for (int j = 0; j < N; j++) {
					synergy[i][j] = Integer.parseInt(st.nextToken());
				}
			}
			min = Integer.MAX_VALUE;
			selected = new boolean[N];
			select1 = new int[N/2];
			select2 = new int[N/2];
			comb(0, 0);
			System.out.printf("#%d %d%n", tc, min);
		}

	}

	private static void comb(int cnt, int start) {
		if(cnt == half_N) {
			min = Math.min(food_diff(), min);
			return;
		}
		if(start == N) return;
		
		selected[start] = true;
		comb(cnt+1, start+1);
		selected[start] = false;
		comb(cnt, start+1);
	}

	private static int food_diff() {
		int sc1=0, sc2=0, sumA=0, sumB=0;
		for(int i = 0; i<N; i++) {
			if(selected[i])
				select1[sc1++] = i;
			else
				select2[sc2++] = i;
		}		
		for(int i = 0; i<half_N; i++) {
			for(int j=0; j<half_N; j++) {
				sumA += synergy[select1[i]][select1[j]];
				sumB += synergy[select2[i]][select2[j]];
			}
		}
		return Math.abs(sumA-sumB);
	}
}

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BK_Silver1_2961 {
	static int N, food[][], min_dif=Integer.MAX_VALUE;
	static boolean[] selected;
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		N = Integer.parseInt(br.readLine());
		
		food = new int[N][2];
		StringTokenizer st;
		for(int i=0; i< N; i++) {
			st = new StringTokenizer(br.readLine());
			food[i][0] = Integer.parseInt(st.nextToken());
			food[i][1] = Integer.parseInt(st.nextToken());
		}
		selected = new boolean[N];
		com_subset(0);
		
		System.out.print(min_dif);
	}

	private static void com_subset(int cnt) {
		if(cnt == N) {
			int sin = 1;
			int sun = 0;
			boolean is_empty = true;
			for(int i =0; i<N; i++) {
				if(selected[i]) {
					sin *= food[i][0];
					sun += food[i][1];
					is_empty = false;
				}
			}
			if(is_empty) return;
			min_dif = Math.min(min_dif, Math.abs(sin-sun));
			return;
		}
		selected[cnt] = true;
		com_subset(cnt+1);
		selected[cnt] = false;
		com_subset(cnt+1);
	}
	
}

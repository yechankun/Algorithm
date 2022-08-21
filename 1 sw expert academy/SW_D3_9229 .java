import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class SW_D3_9229 {
	static int N, M, max_weight = 0, inputs[], number[] = new int[2];
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int TC = Integer.parseInt(br.readLine());
		StringTokenizer st;
		for (int testcase = 1, i; testcase <= TC; testcase++) {
			st = new StringTokenizer(br.readLine());
			N = Integer.parseInt(st.nextToken());
			M = Integer.parseInt(st.nextToken());
			
			inputs = new int[N];

			st = new StringTokenizer(br.readLine());
			for (i = 0; i < N; i++) {
				inputs[i] = Integer.parseInt(st.nextToken());
			}
			
			max_weight=-1;
			combination(N, 2, 0);
			System.out.println("#" + testcase + " " +max_weight);
		}
	}
	
	static void combination(int n, int r, int weight) {
		if(r == 0) {
			if(weight <= M)
				max_weight = Math.max(weight, max_weight);
			return;
		}
		if(n<r)return;
		//선택
		number[r-1] = inputs[n-1];
		combination(n-1, r-1, weight + inputs[n-1]);
		//비선택
		combination(n-1, r, weight);
	}
}

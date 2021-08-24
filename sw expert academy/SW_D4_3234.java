import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class SW_D4_3234{
	static int N, weight[], count;

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(br.readLine());
		StringTokenizer st;
		for (int tc = 1; tc <= T; tc++) {
			N = Integer.parseInt(br.readLine());
			count = 0;
			st = new StringTokenizer(br.readLine(), " ");

			weight = new int[N];
			int sum = 0;
			for (int i = 0; i < N; i++) {
				sum += weight[i] = Integer.parseInt(st.nextToken());
			}
			pick(0, 0, 0, 0, sum);
			System.out.printf("#%d %d%n", tc, count);
		}
	}

	static void pick(int cnt, int flag, int sumL, int sumR, int remain) {
		if (cnt == N) {
			count++;
			return;
		}
		if (sumL >= sumR + remain) {
			int mul = 1;
			for (int k = 1; k <= N - cnt; k++) {
				mul *= k * 2; // n!*2^n
			}
			count += mul;
			return;
		}

		for (int i = 1, j = 0; j < N; i++, j++) {
			if ((flag & 1 << i) != 0)
				continue;
			// 왼쪽에 추 올리기
			pick(cnt + 1, flag | 1 << i, sumL + weight[j], sumR, remain - weight[j]);
			int newSumR = sumR + weight[j];
			// 오른쪽에 추 올리기
			if (newSumR <= sumL)
				pick(cnt + 1, flag | 1 << i, sumL, newSumR, remain - weight[j]);
		}
	}
}

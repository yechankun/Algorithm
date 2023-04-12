// https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWgv9va6HnkDFAW0
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class sw_d3_6808_규영이와인영이의카드게임 {
	private static int N = 9, win;
	private static int[] inNum, kuNum;
//	private static HashMap<Integer, Integer> kuNum = new HashMap<>();
	private static boolean[] kuSelect;

	private static void permutation(int cnt, int flag, int ku_score, int in_score) {
		if (cnt == 9) {
			if (ku_score > in_score)
				win++;
			return;
		}
		for (int i = 1, j = 0, ku_num, in_num; i <= N; i++, j++) {
			if ((flag & 1 << i) != 0)
				continue; // 인덱스 i에 해당하는 수가 사용중임.
			ku_num = kuNum[cnt];
			in_num = inNum[j];
			if (ku_num > in_num)
				permutation(cnt + 1, flag | 1 << i, ku_score + ku_num + in_num, in_score);
			else
				permutation(cnt + 1, flag | 1 << i, ku_score, in_score + ku_num + in_num);
		}
	}

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		int T = Integer.parseInt(br.readLine());
		inNum = new int[N];
		kuNum = new int[N];
		kuSelect = new boolean[19];
		for (int tc = 1; tc <= T; tc++) {			
			win = 0;

			StringTokenizer st = new StringTokenizer(br.readLine(), " ");
			for (int i = 0; i < 9; i++) {
				kuNum[i] = Integer.parseInt(st.nextToken());
				kuSelect[kuNum[i]] = true;
			}
			for (int i = 1, cnt = 0; i <= 18; i++) {
				if (!kuSelect[i]) 
					inNum[cnt++] = i;
			}
			permutation(0, 0, 0, 0);
			
			sb.append("#").append(tc).append(" ").append(win).append(" ").append(362880 - win).append("\n");
			Arrays.fill(kuSelect, false);
		}
		System.out.print(sb);
		sb.setLength(0);
		br.close();
	}
}

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.HashSet;
import java.util.StringTokenizer;

public class bk_g4_1062_가르침 {
	static String[] strs;
	static char cs[][], select_chars[];
	static Character[] char_set;
	static int count = 0, N, K;
	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		HashSet<Character> set = new HashSet<>(); 
		N = Integer.parseInt(st.nextToken());
		K = Integer.parseInt(st.nextToken());

		if(K < 5) {
			System.out.println(0);
			return;
		}
		if(K > 25) {
			System.out.println(N);
			return;
		}	
		
		strs = new String[N];
		cs = new char[N][]; 
		for(int i = 0; i<N; i++) {
			cs[i] =  br.readLine().replace("a", "").replace("c", "").
					replace("n", "").replace("t", "").replace("i", "").
					toCharArray();
			for(int j=0; j<cs[i].length; j++)
				set.add(cs[i][j]);
		}
		char_set = new Character[set.size()];
		set.toArray(char_set);
		if(char_set.length < K-5) {
			System.out.println(N);
			return;
		}
		select_chars = new char[K-5];
		combination(char_set.length, K-5);
		System.out.println(count);
	}

	private static void combination(int n, int r) {
		if(r == 0) {
			int cnt =0;
			start:
			for(int j=0; j<N; j++) {
				for(int i=0; i<cs[j].length; i++) {
					if(Arrays.binarySearch(select_chars, cs[j][i]) < 0)
						continue start;
				}
				cnt++;
			}
			count = Math.max(cnt, count);
			return;
		}
		if(n<r) return;
		select_chars[r-1] = char_set[n-1];
		combination(n-1, r-1);
		//비선택
		combination(n-1,r);
	}
}


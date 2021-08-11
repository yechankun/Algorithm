import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.HashSet;
import java.util.Stack;
import java.util.StringTokenizer;


//DFS로 풀기
//연산자의 밑의 리프노드엔 항상 숫자
//숫자의 자식이나 부모는 숫자가 될 수 없음.
public class SW_D4_1233 {
	static String tree[] = new String[201];
	static int N;
	static boolean isvalid = true;
	static HashSet<String> hash = new HashSet<>();
	public static void main(String[] args) throws NumberFormatException, IOException {	
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		hash.add("*");
		hash.add("/");
		hash.add("-");
		hash.add("+");
		StringTokenizer st;
		for(int tc = 1, i; tc < 11; tc++) {
			N = Integer.parseInt(br.readLine());
			
			for(i=1; i <= N; i++) {
				st = new StringTokenizer(br.readLine());
				st.nextToken();
				tree[i] = st.nextToken();
			}
			isvalid = true;
			dfs(1);
			System.out.printf("#%d %d\n", tc, isvalid?1:0);
			
		}
		Arrays.fill(tree, null);
	}
	
	private static void dfs(int c) { //시작은 1로
		if(!isvalid)	//false가 나오면 재귀 종료
			return;
		//왼쪽 자식노드 방문
		if(c*2<=N) {
			dfs(c * 2);
		}else {//왼쪽 자식노드가 없으면 리프노드다
			if(hash.contains(tree[c]))
				isvalid = false;
			return; 
		}
		//오른쪽 자식 노드 방문
		if(c*2+1<=N) { 
			dfs(c*2 +1);
		}
		//현재 노드 처리
		if(!hash.contains(tree[c]))
			isvalid = false;
	}
}

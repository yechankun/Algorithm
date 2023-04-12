import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class sw_d4_3289_서로소집합 {
	static int[] parent;

	public static int findSet(int v) {
		if (v == parent[v]) // 부모가 더 이상 없이 자기 자신이 루트노드이면
			return v; // root를 리턴한다.
		
		 // 부모가 같으면 모두 부모에 연결시켜서
		// 최소 신장 트리로 만든다.
		return parent[v] = findSet(parent[v]);
	}

	public static void unionSet(int u, int v) {
		parent[findSet(u)] = findSet(v); // 부모를 서로 연결함.
	}

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		int T = Integer.parseInt(br.readLine());

		StringTokenizer st;
		StringBuilder sb = new StringBuilder();
		for (int tc = 1; tc <= T; tc++) {
			st = new StringTokenizer(br.readLine());
			int n = Integer.parseInt(st.nextToken());
			int m = Integer.parseInt(st.nextToken());
			parent = new int[n+1];
			
			for(int i =1; i<=n; i++) {
				parent[i] = i;
			}
			
			sb.append("#").append(tc).append(" ");
			for (int i = 0; i < m; i++) {
				st = new StringTokenizer(br.readLine());
				
				int op = Integer.parseInt(st.nextToken());
				int a = Integer.parseInt(st.nextToken());
				int b = Integer.parseInt(st.nextToken());
				
				if(op == 0) {
					unionSet(a, b);
				}
				else {
					sb.append(findSet(a) == findSet(b) ? 1 : 0);
				}
			}
			sb.append("\n");
		}
		System.out.print(sb.toString());
	}
}

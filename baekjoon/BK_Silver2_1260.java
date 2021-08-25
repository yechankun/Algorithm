import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Stack;
import java.util.StringTokenizer;

public class BK_Silver2_1260{
	static boolean graph[][], visited[];
	static int N, M;

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		int start = Integer.parseInt(st.nextToken()) - 1;
		graph = new boolean[N][N];
		visited = new boolean[N];
		for (int i = 0; i < M; i++) {
			st = new StringTokenizer(br.readLine());
			int sp = Integer.parseInt(st.nextToken()) - 1;
			int dist = Integer.parseInt(st.nextToken()) - 1;

			graph[sp][dist] = true;
			graph[dist][sp] = true;
		}
		DFS(start);
		System.out.println();
		Arrays.fill(visited, false);
		BFS(start);

	}

	private static void DFS(int sp) {
		Stack<Integer> stack = new Stack<>();
		stack.add(sp);
		while(!stack.isEmpty()) {
			int curr = stack.pop();
			if(visited[curr]) continue;
			visited[curr] = true;
			System.out.print(curr+1 + " ");
			for(int i = N-1; i>-1; i--) {	//후입선출
				if(graph[curr][i] && !visited[i]) {
					stack.push(i);
				}
			}
		}
	}

	private static void BFS(int sp) {
		Queue<Integer> queue = new LinkedList<>();
		queue.offer(sp);
		visited[sp] = true;
		System.out.print(sp+1 + " ");
		while(!queue.isEmpty()) {
			int curr = queue.poll();
			
			for(int i = 0; i<N; i++) {
				if(graph[curr][i] && !visited[i]) { //선입선출
					queue.offer(i);
					visited[i] = true;
					System.out.print(i+1 + " ");
				}
			}
		}
	}
}
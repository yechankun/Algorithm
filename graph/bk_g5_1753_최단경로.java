import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.PriorityQueue;
import java.util.StringTokenizer;


public class bk_g5_1753_최단경로 {
	static class Vertex implements Comparable<Vertex>{
		int to;
		int weight;
		public Vertex(int to, int weight) {
			this.to = to;
			this.weight = weight;
		}
		
		public int compareTo(Vertex o){
			return this.weight - o.weight;			
		}
	}
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		StringTokenizer st = new StringTokenizer(br.readLine());

		int V = Integer.parseInt(st.nextToken());
		int E = Integer.parseInt(st.nextToken());

		int start = Integer.parseInt(br.readLine()) - 1;
		List<Vertex> weight[] = new ArrayList[V];
		boolean visited[] = new boolean[V];
		int distance[] = new int[V];
		
		for(int i = 0; i < V; i++) {
			weight[i] = new ArrayList<>();
			distance[i] = Integer.MAX_VALUE;
        }
		
		for (int i = 0; i < E; i++) {
			st = new StringTokenizer(br.readLine());
			int u = Integer.parseInt(st.nextToken()) - 1;
			int v = Integer.parseInt(st.nextToken()) - 1;
			int w = Integer.parseInt(st.nextToken());
			weight[u].add(new Vertex(v, w));
		}
		distance[start] = 0;
		
		PriorityQueue<Vertex> queue = new PriorityQueue<>();
        
        queue.offer(new Vertex(start, 0));

		while(!queue.isEmpty()) {
			Vertex min = queue.poll();
			if(visited[min.to])continue;
			if (distance[min.to] < min.weight) {
                continue;
            }
			visited[min.to] = true;
            for (int i = 0; i < weight[min.to].size(); i++) {
            	Vertex to = weight[min.to].get(i);
                if (distance[to.to] > min.weight + to.weight) {
                    distance[to.to] = min.weight + to.weight;
                    queue.add(new Vertex(to.to, min.weight + to.weight));
                }
            }
		}
		StringBuilder sb = new StringBuilder();
		for (int i : distance) {
			sb.append(i == Integer.MAX_VALUE ? "INF" : i).append('\n');
		}
		System.out.print(sb.toString());
	}
}
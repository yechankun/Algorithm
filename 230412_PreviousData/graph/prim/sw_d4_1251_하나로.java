//https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV15StKqAQkCFAYD
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.PriorityQueue;
import java.util.StringTokenizer;
 
 
public class sw_d4_1251_하나로 {
    static class Vertex implements Comparable<Vertex> {
        int no;
        long weight;
 
        public Vertex(int no, long weight) {
            this.no = no;
            this.weight = weight;
        }
 
        public int compareTo(Vertex o) {
            return Long.compare(this.weight, o.weight);
        }
    }
 
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
 
        int T = Integer.parseInt(br.readLine());
 
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();
        for (int tc = 1; tc <= T; tc++) {
            int N = Integer.parseInt(br.readLine());
            long[][] adj = new long[N][N];
            int[][] mapXY = new int[N][2];
            boolean[] visited = new boolean[N];
            long[] minEdge = new long[N];
 
            st = new StringTokenizer(br.readLine());
            for (int i = 0; i < N; i++) {
                mapXY[i][0] = Integer.parseInt(st.nextToken());
            }
            st = new StringTokenizer(br.readLine());
            for (int i = 0; i < N; i++) {
                mapXY[i][1] = Integer.parseInt(st.nextToken());
            }
            double E = Double.parseDouble(br.readLine());
            // 간선 배열 저장 <== 각 간선의 길이의 곱들을 저장해서 크기 비교
            for (int i = 0; i < N; i++) {
                for (int j = 0; j < N; j++)
                    adj[j][i] = adj[i][j] = distance(mapXY[i][0], mapXY[i][1], mapXY[j][0], mapXY[j][1]);
                minEdge[i] = Long.MAX_VALUE;
            }
 
            long result = 0;
            int nodeCount = 0;
            PriorityQueue<Vertex> queue = new PriorityQueue<>();
            queue.offer(new Vertex(0, 0));  //시작점이 주어지지 않았으므로 0부터
            minEdge[0] = 0;
            while(!queue.isEmpty()) {//모든 정점(인접된 정점) 수만큼 반복
                Vertex min = queue.poll();  //최소힙을 통해 앞으로 가봐야할 정점 중 최소 비용의 정점이 추출됨
                if(visited[min.no])continue; // 최소 비용의 정점이 방문했던 정점이라면 pass 다음 정점을 처리
                 
                //최소 비용의 정점이 방문하지 않은 정점이라면 선택
                result += min.weight;   //비용 처리
                visited[min.no] = true;     //방문 처리
                 
                if(++nodeCount == N) break; //모든 정점이 다 연결됐다면 중단.
                //선택한 정점에서 출발하는 모든 간선의 대한 비용을 업데이트   
                 
                for (int i = 0; i < N; i++) {
                    //방문하지 않은 정점        인접되어 있어야함.          최소비용
                    if (!visited[i] && adj[min.no][i] != 0 &&  minEdge[i] > adj[min.no][i]  ) {
                        minEdge[i] = adj[min.no][i];
                        queue.offer((new Vertex(i, adj[min.no][i])));
                    }
                }
            }
            sb.append(String.format("#%d %d%n", tc, Math.round(E * result)));
        }
        System.out.print(sb.toString());
    }
 
    static long distance(int x1, int y1, int x2, int y2) {
        long d = (long) ((Math.pow(x1 - x2, 2) + Math.pow(y1 - y2, 2)));
        return d;
    }
}
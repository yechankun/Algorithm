import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class JO_문제은행_1661 {
	private static char[][] map; // 가중치가 없는 인접 행렬 정보
	private static boolean[][] visited; // Node에 대한 방문 여부
	private static int map_width, map_height; // Node 수

	//상하 좌우
	private static int[] dr = {-1, 1, 0, 0};
	private static int[] dc = {0, 0, -1, 1};
	
	private static int X, Y, EX, EY;
	public static void JO(String[] args) throws Exception {
		//1. 입력처리
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		map_width = Integer.parseInt(st.nextToken());
		map_height = Integer.parseInt(st.nextToken());

		map = new char[map_height][map_width];		
		visited = new boolean[map_height][map_width];
		
		//1.1. 시작과 종료 위치 받기
		st = new StringTokenizer(br.readLine());
		X = Integer.parseInt(st.nextToken()) - 1;
		Y = Integer.parseInt(st.nextToken()) - 1;
		
		EX = Integer.parseInt(st.nextToken()) - 1;
		EY = Integer.parseInt(st.nextToken()) - 1;
		
		//1.2. 맵 정보 받기
		for(int i=0; i<map_height; i++) {
			map[i] = br.readLine().toCharArray();
		}
		//2. 그래프를 탐색
		System.out.println(bfs());

	}

	private static int bfs() {
		Queue<int[]> queue = new LinkedList<>(); // 탐색할 노드를 담을 queue

//		1. 첫 방문 node를 queue에 담고 시작
		queue.offer(new int[] {Y, X, 0}); //이동값을 포함한 큐 
//		2. queue에 담은 node를 방문처리
		visited[Y][X] = true;

//		3. 탐색 시작
		while (!queue.isEmpty()) {
			int[] cur = queue.poll();
			int r = cur[0];
			int c = cur[1];
			for (int i = 0; i < 4; i++) {
				int nr = r+dr[i];
				int nc = c+dc[i];
				
				if(nr > -1 && nr < map_height && nc > -1 && nc < map_width && map[nr][nc] == '0' && !visited[nr][nc]) {
					if(nr == EY && nc == EX) {
						return cur[2]+1;	//마지막 이동을 포함한 결과값 리턴.
					}else {
						queue.offer(new int[] {nr, nc, cur[2] + 1}); 
						visited[nr][nc] = true;
					}
				}
			}
		}
		return 0;	//EX, EY까지 이동이 불가능할경우 반환된다.
	}
}

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BK_Gold5_15686 {
	
	//조합문제이다.
	//
	static int N, M, chicken_pos[][], home_pos[][], ck_top, home_top, ck_select[][];
	static int city_chicken_dist=Integer.MAX_VALUE;

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        
        home_pos = new int[2*N][2];
        chicken_pos = new int[13][2];
        ck_select = new int[M][];
        
        for(int i=0; i<N; i++) {
        	st = new StringTokenizer(br.readLine());
        	for(int j=0; j<N; j++) {
        		int type =  Integer.parseInt(st.nextToken());
        		if(type == 1) {
        			home_pos[home_top][0] = i;
        			home_pos[home_top++][1] = j;
        		} else if(type==2) {
        			chicken_pos[ck_top][0] = i;
        			chicken_pos[ck_top++][1] = j;
        		}
        	}	
        }
        chick_cal(0, 0);
        System.out.print(city_chicken_dist);
	}
	
	private static void chick_cal(int cnt, int start) {
		if(cnt == M) {	//다 뽑힌 경우
			chiken_dist_cal();
			return;
		}
		// 모든 치킨집 조합 뽑기
		for(int i = start; i< ck_top; i++) {
			ck_select[cnt] = chicken_pos[i];
			//다음 치킨집 뽑기
			chick_cal(cnt+1, i+1);
		}		
	}
	private static void chiken_dist_cal() {
		int city_dist = 0;
		for(int j=0; j<home_top; j++) {	//집마다
			int chick_dist = Integer.MAX_VALUE;
			for(int i=0; i<M; i++) {	//치킨집과의 거리의 최소값을 계산
				chick_dist = min_dist_cal(chick_dist, home_pos[j], ck_select[i]);
			}
			city_dist += chick_dist;
		}
		//전체 치킨거리를 최소값으로 최신화
		city_chicken_dist = Math.min(city_chicken_dist, city_dist);
	}
	
	private static int min_dist_cal(int min,int[] a, int[] b) {
		return Math.min(min,Math.abs(a[0]-b[0]) +
				Math.abs(a[1]-b[1]));
	}
}

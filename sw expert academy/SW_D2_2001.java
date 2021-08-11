import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;


public class SW_D2_2001 {
    public static void main(String args[]) throws Exception{
    	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
        int T;
        T= Integer.parseInt(br.readLine());
        int[][] map;
        int[][] sum;
        
        //부분합을 구한다. DP!!
        for(int testcase = 1, N, M; testcase <= T; testcase++)
        {
        	map = new int[17][17];	
        	sum = new int[17][17];

            st = new StringTokenizer(br.readLine().trim());
			N = Integer.parseInt(st.nextToken().trim());		
			M = Integer.parseInt(st.nextToken().trim());
			
            int max=0;
            //계산 효율성을 위해 0으로 채워진 0번째 row와 col을 만듬.
            for(int i=1;i<=N;i++) {
            	st = new StringTokenizer(br.readLine().trim());
                for (int j = 1; j <= N; j++) {
                    map[i][j] = Integer.parseInt(st.nextToken().trim());
                    
                    sum[i][j] = map[i][j];
                    //i, j기준으로 왼쪽과 위를 더하고 좌상의 값을 뺌.
                    sum[i][j] += sum[i - 1][j] + sum[i][j - 1] - sum[i - 1][j - 1];
                }
            }
            
            //부분 합인 sum으로 결과를 구함 
            for(int i=0;i<=N-M;i++) {
                for(int j=0;j<=N-M;j++){
                	//i, j를 기준으로 M*M의 정사각형에서  sum의 좌상과 우하를 더하고 좌와 상을 빼면 그 범위의 합임.
                    max = Math.max(max, sum[i+M][j+M]-sum[i][j+M]-sum[i+M][j]+sum[i][j]);
                }
            }
            System.out.printf("#%d %d\n", testcase, max);
        }
    }
}
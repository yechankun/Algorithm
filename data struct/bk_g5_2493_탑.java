import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;
import java.util.StringTokenizer;

public class bk_g5_2493_탑 {
	public static void BK(String[] args) throws NumberFormatException, IOException {
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(in.readLine());
		StringTokenizer st = new StringTokenizer(in.readLine());
		Stack<int[]> stack = new Stack<>();//0번째가 높이 1번째가 인덱스
		
		int temp;
		 for (int i = 1; i < N + 1; i++) {
        	temp = Integer.parseInt(st.nextToken());
            while(!stack.isEmpty() && stack.peek()[0] < temp) {
                stack.pop();
            }
            
            if(stack.isEmpty()) System.out.print("0 ");
            else System.out.print(stack.peek()[1]+" ");
            stack.push(new int[] {temp, i});
		 }
	}
}

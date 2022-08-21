import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Stack;
import java.util.StringTokenizer;

public class SW_test_1952 {

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		int T = Integer.parseInt(br.readLine()) + 1;
		Stack<int[]> stack = new Stack<>();
		int[] monthcost = new int[12]; 
		int[] useplan = new int[12]; 
		
		StringTokenizer st;
		int min, daily, montly, month3, temp;
		int[] stackpop;
		for (int i = 1, j = 0; i < T; i++) {
			st = new StringTokenizer(br.readLine());
			
			daily = Integer.parseInt(st.nextToken());
			montly = Integer.parseInt(st.nextToken());
			month3 = Integer.parseInt(st.nextToken());
			min = Integer.parseInt(st.nextToken()); //year값
			
			st = new StringTokenizer(br.readLine());
			for (j = 0; j < 12; j++) {
				temp = useplan[j] = Integer.parseInt(st.nextToken());
				monthcost[j] =   Math.min(temp*daily, montly);
			}
			
			stack.push(new int[]{0,0});
			while(!stack.isEmpty()) {
				stackpop = stack.pop();
				if(stackpop[0]>11) {
					min = Math.min(stackpop[1], min);
					continue;
				}else {
					if(useplan[stackpop[0]]>0) {
						stack.push(new int[] {stackpop[0]+1, stackpop[1]+monthcost[stackpop[0]]});
						stack.push(new int[] {stackpop[0]+3, stackpop[1]+month3});
					}else {
						stackpop[0]++;
						stack.push(stackpop);
					}
				}
			}			
			System.out.printf("#%d %d\n", i, min);
			Arrays.fill(monthcost, 0);
		}
	}
}

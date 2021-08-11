import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class SW_D3_1225 {

	public static void main(String[] args) throws NumberFormatException, IOException {
		Queue<Integer> queue = new LinkedList<Integer>();
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		int T, temp, minus;
		for (int i = 1; i < 11; i++) {
			T = Integer.parseInt(br.readLine());
			st = new StringTokenizer(br.readLine());
			for(int j=0; j<8; j++) {
				queue.offer(Integer.parseInt(st.nextToken()));
			}
			minus = 1;
			while(true) {
				minus = minus == 6 ? 1 : minus;
				temp = queue.poll() - minus++;
				if(temp < 1) {
					queue.offer(0);
					break;
				}
				queue.offer(temp);
			}
			System.out.print("#"+T);
			for(int q: queue) {
				System.out.print(" "+q);
			}
			System.out.println();
			queue.clear();
		}
	}
}

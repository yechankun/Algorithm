//https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14eWb6AAkCFAYD
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Stack;

public class sw_d4_1218_괄호짝짓기 {

	public static void main(String[] args) throws NumberFormatException, IOException {
		
		Stack<Character> stack = new Stack<>();
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		HashMap<Character,Character> ch_map = new HashMap<Character,Character>();
		ch_map.put('(', ')');
		ch_map.put('[', ']');
		ch_map.put('{', '}');
		ch_map.put('<', '>');
		
		int t_len, result;
		char[] ch;
		for (int i = 1, j=0; i < 11; i++) {
			t_len = Integer.parseInt(br.readLine());
			ch = br.readLine().toCharArray();
			
			result = 1;
			for(j=0; j<t_len; j++) {
				if(ch_map.containsKey(ch[j])) {
					stack.push(ch[j]);
				}
				else {
					if(stack.isEmpty()) {
						result =0;
						break;
					}
					if(ch_map.get(stack.pop()) != ch[j]) {
						result = 0;
						break;
					}
				}
			}
			stack.clear();
			System.out.printf("#%d %d\n", i, result);
		}
	}
}

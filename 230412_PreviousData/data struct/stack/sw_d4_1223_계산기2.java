// https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14nnAaAFACFAYD
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Stack;

public class sw_d4_1223_계산기2 {

	public static void main(String[] args) throws Exception {
		Stack<Character> opStack = new Stack<>();
		Stack<Integer> numStack = new Stack<>();
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int size;
		StringBuilder sb = new StringBuilder();
		for (int tc = 1; tc <= 10; tc++) {
			size = Integer.parseInt(br.readLine());
			char[] sick = br.readLine().toCharArray();
			for (int i = 0; i < size; i++) { // 전위식 변환
				char c = sick[i];
				if ('0' <= c && c <= '9')
					sb.append(c);
				else {
					if (c == '*')
						opStack.push(c); // 우선순위
					else {
						while (!opStack.isEmpty() && (opStack.peek() == '*' || opStack.peek() == '+')) {
							sb.append(opStack.pop());
						}
						opStack.push(c);
					}
				}
			}
			while (!opStack.empty())
				sb.append(opStack.pop());

			for (int i = 0; i < size; i++) {
				char c = sb.charAt(i);
				if ('0' <= c && c <= '9') {
					numStack.push(c - '0');
				} else {
					if (c == '*')
						numStack.push(numStack.pop() * numStack.pop());
					else
						numStack.push(numStack.pop() + numStack.pop());
				}
			}
			System.out.printf("#%d %d%n", tc, numStack.pop());
			sb.setLength(0);
		}
	}
}
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;
 
public class JO_Intermediate_Coder_1141 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        Stack<Integer> stack = new Stack();
        long sum = 0;
 
        int tmp=0;
        for (int i = 0; i < N; i++) {
        	tmp = Integer.parseInt(br.readLine());
            while(!stack.isEmpty() && stack.peek()<tmp) {
                stack.pop();
            }
            sum += stack.size();
            stack.push(tmp);
        }
        System.out.println(sum);
    }
}
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class SW_D3_1289 {

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		int T = Integer.parseInt(br.readLine()) + 1;
		char curr = '0';
		int cnt = 0;
		for (int i = 1; i < T; i++) {
			curr = '0';
			cnt = 0;
			String input = br.readLine();	
			for (int j = 0; j < input.length(); j++) {
				if (input.charAt(j) != curr) {
					curr = curr == '0' ? '1' : '0';
					cnt++;
				}
			}
			System.out.printf("#%d %d\n", i, cnt);
		}
	}
}

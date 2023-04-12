import java.util.Arrays;
import java.util.Scanner;

public class jo_1810_백설공주 {
	static int n = 9, r = 7, nanzangs[] = new int[9], numbers[] = new int[7];
	public static void JO(String[] args) {
		Scanner sc = new Scanner(System.in);
		for (int i = 0; i < n; i++)
			nanzangs[i] = sc.nextInt();
		sc.close();
		combination(n, r);
	}

	private static void combination(int n, int r) {
		if (r == 0) {
			int sum = 0;
			for (int num : numbers) {
				sum += num;
			}
			if (sum == 100) {
				for (int num : numbers) {
					System.out.println(num);
				}
				System.out.println(Arrays.toString(numbers));
			}
			return;
		}
		if (n < r)
			return;
		// 선택
		numbers[r - 1] = nanzangs[n - 1];
		combination(n - 1, r - 1);
		// 비선택
		combination(n - 1, r);
	}
}

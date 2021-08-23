import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.StringTokenizer;

public class JO_문제은행_1828{
	
	static class Ref implements Comparable<Ref>{
		int lowC;	//최저온도
		int highC;	//최고온도
		public Ref(int inTime, int outTime) {
			super();
			this.lowC = inTime;
			this.highC = outTime;
		}
		@Override
		public int compareTo(Ref o) {
			return  highC - o.highC;
		}
	}
	public static void main(String[] args) throws Exception {
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(in.readLine());
		ArrayList<Ref> list = new ArrayList<>(N);
		StringTokenizer st;
		for (int i = 0; i< N ; i++) {
			st = new StringTokenizer(in.readLine());
			list.add(new Ref(Integer.parseInt(st.nextToken()),
					Integer.parseInt(st.nextToken())
					));			
		}
		//최고 온도를 기준으로 정렬
		Collections.sort(list);
		int ref_num = 1;
		int high = list.get(0).highC;		
		for(int i = 1; i<N; i++) {
			if(high < list.get(i).lowC) {	// 이게 참이면 새로운 냉장고가 필요함
				high = list.get(i).highC;		
				ref_num++;
			}
		}   
		System.out.println(ref_num);		
	}
}


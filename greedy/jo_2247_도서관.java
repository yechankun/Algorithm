import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.StringTokenizer;

public class JO_문제은행_2247{
	
	static class Library implements Comparable<Library>{
		int inTime;	//시작 시간
		int outTime;	//종료 시간
		public Library(int inTime, int outTime) {
			super();
			this.inTime = inTime;
			this.outTime = outTime;
		}
		@Override
		public int compareTo(Library o) {
			return  inTime - o.inTime;
		}
	}
	public static void main(String[] args) throws Exception {
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(in.readLine());
		ArrayList<Library> list = new ArrayList<>(N);
		StringTokenizer st;
		for (int i = 0; i< N ; i++) {
			st = new StringTokenizer(in.readLine());
			list.add(new Library(Integer.parseInt(st.nextToken()),
					Integer.parseInt(st.nextToken())
					));			
		}
		//시작시간을 기준으로 정렬
		Collections.sort(list);
		int max_time = Integer.MIN_VALUE; 
		int min_time = Integer.MIN_VALUE;
		
		int start = list.get(0).inTime;
		//종료시간과 시작시간을 비교해 줘야 하므로 종료시간을 미리 변수로 빼놓음
		int end = list.get(0).outTime;
		for(int i = 1; i<N; i++) {
			int temp = list.get(i).inTime;
			if(end >= temp) {	// 이게 참이면 도서관에 사람이 비지 않고 사람이 들어옴.
				//사람이 추가로 들어와 종료시간이 바뀐다면 갱신
				end = Math.max(end, list.get(i).outTime);
				max_time = Math.max(max_time, end-start);
			}else {							// 사람이 비고 다시 사람이 들어옴
				start = temp;
				min_time = Math.max(min_time, start - end);	//비어있던 시간의 최소값 갱신
				end = list.get(i).outTime;
			}
		}   
		max_time = Math.max(max_time, end-start);
		System.out.println(max_time+" "+min_time);		
	}
}


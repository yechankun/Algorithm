import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class JO_Intermediate_Coder_3517{
	static int[] datas;
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		int N = Integer.parseInt(br.readLine());
		datas = new int[N];
		StringTokenizer st = new StringTokenizer(br.readLine());
		for(int i=0; i<N; i++) {
			datas[i] = Integer.parseInt(st.nextToken());
		}		
		int Q = Integer.parseInt(br.readLine());
		st = new StringTokenizer(br.readLine());
		StringBuilder sb = new StringBuilder();
		for(int i=0; i<Q; i++) {
			sb.append(binarySearch(Integer.parseInt(st.nextToken()), 0, N-1)+" ");
			if(i%1000 == 0) {
				bw.write(sb.toString());
				sb.setLength(0);
			}
		}
		br.close();
		bw.write(sb.toString());
        bw.close();
	}

	public static int binarySearch(int find, int start, int end) {
      if(start>end) return -1;
      int mid = (start+end)/2;
      int data = datas[mid];
      if(find==data) {
          return mid;
      }
      else if(find<data) {
          return binarySearch(find,start,mid-1);
      }
      return binarySearch(find,mid+1,end);
	}
}

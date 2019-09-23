
//baekjoon source = "https://www.acmicpc.net/problem/2559"

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class _2559_¼ö¿­ {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		int n = Integer.parseInt(st.nextToken());
		int k = Integer.parseInt(st.nextToken());
		int[] arr= new int[n];
		st = new StringTokenizer(br.readLine());
		for(int i = 0; i<n; ++i) {
			arr[i] = Integer.parseInt(st.nextToken());
		}
		
		int sum = 0, result = 0;
		for(int i = 0; i<k; ++i) {
			sum += arr[i];
		}
		result = sum;
		
		for(int i = 0; i<n-k; ++i) {
			sum -= arr[i];
			sum += arr[i+k];
			result = Math.max(result, sum);
		}
		bw.write(result+"");
		bw.flush();
	}
}

//baekjoon source = "https://www.acmicpc.net/problem/7568"
package j_브루트포스;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class _7568_덩치 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

		int n = Integer.parseInt(br.readLine());
		int[][] arr = new int[n][2];
		for (int i = 0; i < n; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			arr[i][0] = Integer.parseInt(st.nextToken());
			arr[i][1] = Integer.parseInt(st.nextToken());
		}
		
		StringBuilder sb = new StringBuilder();
		for(int i = 0; i<n; i++) {
			int result = 0;
			for(int j = 0; j<n; j++) {
				if(arr[i][0] < arr[j][0] && arr[i][1] < arr[j][1])
					result++;
			}
			sb.append(result+1+" ");
		}
		bw.write(sb+"");
		bw.flush();
		
	}
}

//baekjoon source = "https://www.acmicpc.net/problem/3078"
package 큐;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.StringTokenizer;

public class _3078_좋은친구 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

		StringTokenizer st = new StringTokenizer(br.readLine());
		int n = Integer.parseInt(st.nextToken()), k = Integer.parseInt(st.nextToken());
		int[] arr = new int[n];
		int[][] check = new int[21][2];
		
		long result = 0;

		for (int i = 0; i < n; i++) {
			st = new StringTokenizer(br.readLine());
			arr[i] = st.nextToken().length();
		}

		for (int i = 0; i < n; i++) {
			int r = 0;
			int end = i + k > n - 1 ? n - 1 : i + k;
			int len = arr[i];
			int start = i;
			
			if (check[len][0] > i) {
				start = check[len][0];
				result += (check[len][1]-1);
				r = check[len][1]-1;
			}else {
				check[len][1] = 0;
			}
			
			for (int j = start+1; j <= end; j++) {
				if (len == arr[j]) {
					check[len][0] = j;
					result++;
					r++;
				}
			}
			check[len][1] = r;
		}
		
		bw.write(result + "");
		bw.flush();
	}
}

//baekjoon source = "https://www.acmicpc.net/problem/11055"
package 다이나믹프로그래밍;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class _11055_가장큰증가부분수열 {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

		int a = Integer.parseInt(br.readLine());
		int[] arr = new int[a];
		int[] dp = new int[a];
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		for (int i = 0; i < a; i++) {
			arr[i] = Integer.parseInt(st.nextToken());
		}
		int result = arr[0];
		dp[0] = arr[0];
		for (int i = 1; i < a; i++) {
			dp[i] = arr[i];
			for (int j = 0; j < i; j++) {
				if (arr[j] < arr[i] && dp[i] < dp[j] + arr[i]) {
					dp[i] = dp[j] + arr[i];
				}
			}
			result = Math.max(result, dp[i]);
		}
		bw.write(result+"");

		bw.flush();
	}
}

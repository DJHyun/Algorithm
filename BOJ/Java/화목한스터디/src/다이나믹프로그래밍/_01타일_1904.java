//baekjoon source = "https://www.acmicpc.net/problem/1904"
package 다이나믹프로그래밍;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;

public class _01타일_1904 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

		int n = Integer.parseInt(br.readLine());
		int[] dp = new int[n + 1];
		if (n == 1) {
			dp[1] = 1;
		} else {
			dp[1] = 1;
			dp[2] = 2;
		}

		for (int i = 3; i <= n; i++) {
			dp[i] = (dp[i - 2] + dp[i - 1]) % 15746;
		}
		bw.write(dp[n] + "\n");
		bw.flush();
	}
}

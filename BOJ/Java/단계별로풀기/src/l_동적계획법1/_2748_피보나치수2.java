//baekjoon source = "https://www.acmicpc.net/problem/2557"
package l_동적계획법1;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;

public class _2748_피보나치수2 {
	static int n;
	static long[] dp;

	static long solution(int x) {
		if (x == 0)
			return 0;
		if (x == 1)
			return 1;

		if (dp[x] != 0)
			return dp[x];
		dp[x] = solution(x - 1) + solution(x - 2);
		return dp[x];
	}

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

		n = Integer.parseInt(br.readLine());
		dp = new long[n + 1];
		dp[0] = 0; dp[1] = 1;
		if (n > 1) {
			solution(n);
		}
		bw.write(dp[n] + "");
		bw.flush();

	}
}

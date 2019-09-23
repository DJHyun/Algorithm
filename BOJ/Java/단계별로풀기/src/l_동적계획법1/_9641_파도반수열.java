//baekjoon source = "https://www.acmicpc.net/problem/9641"
package l_동적계획법1;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class _9641_파도반수열 {
	static int n;
	static long[] dp;

	static long solution(int x) {
		if (x < 3)
			return 1;

		if (dp[x] != 0)
			return dp[x];
		dp[x] = solution(x - 2) + solution(x - 3);
		return dp[x];
	}

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

		int T = Integer.parseInt(br.readLine());
		for (int t = 0; t < T; ++t) {
			n = Integer.parseInt(br.readLine());
			if (n < 3) {
				bw.write(1 + "\n");
			} else {
				dp = new long[n];
				dp[0] = dp[1] = dp[2] = 1;
				solution(n-1);
				bw.write(dp[n-1]+"\n");
			}
		}
		bw.flush();
	}
}

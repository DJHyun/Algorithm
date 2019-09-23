//baekjoon source = "https://www.acmicpc.net/problem/1003"
package l_동적계획법1;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;

public class _1003_피보나치함수 {

	static int n;
	static int[][] dp;
	static int zero, one;

	static int solution(int x) {
		if (x == 0) {
			zero++;
			return 0;
		} else if (x == 1) {
			one++;
			return 1;
		} else if (dp[x][0] != 0 && dp[x][1] != 0) {
			zero += dp[x][0];
			one += dp[x][1];
		}else {
			solution(x-1);
			solution(x-2);
			dp[x][0] = zero;
			dp[x][1] = one;
		}
		return 0;
	}


	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

		int T = Integer.parseInt(br.readLine());
		for (int t = 0; t < T; t++) {
			n = Integer.parseInt(br.readLine());
			dp = new int[n + 1][2];
			one = 0;
			zero = 0;
			
			if (n > 1) {
				solution(n);
				bw.write(dp[n][0] + " "+ dp[n][1]+"\n");
			} else if (n == 1) {
				bw.write(0 + " " + 1 + "\n");
			} else {
				bw.write(1 + " " + 0 + "\n");
			}
			
		}
		bw.flush();
	}
}

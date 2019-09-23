//baekjoon source = "https://www.acmicpc.net/problem/12865"
package 다이나믹프로그래밍;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.StringTokenizer;

public class _12865_평범한배낭 {

	static int n, k, result;
	static int[][] arr;
	static int[][] dp;
	
	static int solution(int pos, int capacity) {
		if (pos == n)
			return 0;

		int r = dp[pos][capacity];
		if (r != -1)
			return r;
		if (capacity >= arr[pos][0]) {
			r = solution(pos + 1, capacity - arr[pos][0]) + arr[pos][1];
		}
		r = Math.max(r, solution(pos + 1, capacity));

		return dp[pos][capacity] = r;
	}

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

		StringTokenizer st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		k = Integer.parseInt(st.nextToken());
		arr = new int[n][2];
		dp = new int[n][100001];
		
		for(int i =0; i<n; i++) {
			Arrays.fill(dp[i], -1);
		}
		
		result = 0;
		for (int i = 0; i < n; i++) {
			st = new StringTokenizer(br.readLine());
			arr[i][0] = Integer.parseInt(st.nextToken());
			arr[i][1] = Integer.parseInt(st.nextToken());
		}
		
		bw.write(solution(0,k)+"\n");
		bw.flush();
	}
}

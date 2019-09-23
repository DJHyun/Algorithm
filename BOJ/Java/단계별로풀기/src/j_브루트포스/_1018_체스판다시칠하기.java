//baekjoon source = "https://www.acmicpc.net/problem/2557"
package j_브루트포스;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class _1018_체스판다시칠하기 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

		StringTokenizer st = new StringTokenizer(br.readLine());
		int n = Integer.parseInt(st.nextToken()), m = Integer.parseInt(st.nextToken());
		char[][] arr = new char[n][m];
		int result = Integer.MAX_VALUE;

		for (int i = 0; i < n; i++) {
			st = new StringTokenizer(br.readLine());
			char[] s = st.nextToken().toCharArray();
			for (int j = 0; j < s.length; j++) {
				arr[i][j] = s[j];
			}
		}

		for (int i = 0; i <= n - 8; i++) {
			for (int j = 0; j <= m - 8; j++) {
				boolean flag = false;
				int cnt = 0;
				if (arr[i][j] == 'B') {
					flag = true;
				}

				for (int a = i; a < i + 8; a++) {
					for (int b = j; b < j + 8; b++) {
						if (a == i && b == j)
							continue;
						if (flag) {
							if (arr[a][b] == 'B') {
								cnt++;
							}
							flag = false;
						} else {
							if (arr[a][b] == 'W') {
								cnt++;
							}
							flag = true;
						}
						if (b == j + 7)
							flag = !flag;
					}
				}
				if (cnt > 32)
					cnt = 64 - cnt;
				result = Math.min(result, cnt);
			}
		}
		bw.write(result + "");
		bw.flush();
	}
}

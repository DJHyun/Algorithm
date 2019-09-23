//baekjoon source = "https://www.acmicpc.net/problem/1966"
package 큐;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class _1966_프린터큐 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

		int t = Integer.parseInt(br.readLine());
		for (int test_case = 0; test_case < t; test_case++) {
			Queue<Integer> q = new LinkedList<>();
			StringTokenizer st = new StringTokenizer(br.readLine());
			int n = Integer.parseInt(st.nextToken()), m = Integer.parseInt(st.nextToken()) + 1;
			int[] check = new int[101];
			st = new StringTokenizer(br.readLine());
			int max = Integer.MIN_VALUE;
			for (int i = 0; i < n; i++) {
				int c = Integer.parseInt(st.nextToken());
				check[c]++;
				q.add(c + (i + 1) * 1000);
				max = Math.max(max, c);
			}

			int result = 1;
			while (true) {
				int re = q.poll();
				if (re % 1000 == max) {
					if (re / 1000 == m) {
						break;
					} else {
						result++;
						if (check[max] >= 2) {
							check[max]--;
						} else {
							check[max]--;
							for (int i = 100; i > 0; i--) {
								if (check[i] != 0) {
									max = i;
									break;
								}
							}
						}
					}
				} else {
					q.add(re);
				}
			}

			bw.write(result + "\n");
			bw.flush();
		}
	}
}

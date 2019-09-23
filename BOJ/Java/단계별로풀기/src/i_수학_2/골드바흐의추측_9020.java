//baekjoon source = "https://www.acmicpc.net/problem/9020"
package i_ºˆ«–_2;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;

public class ∞ÒµÂπŸ»Â¿«√ﬂ√¯_9020 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

		int T = Integer.parseInt(br.readLine());
		for (int t = 0; t < T; t++) {
			int n = Integer.parseInt(br.readLine());
			int[] number = new int[n + 1];

			for (int i = 2; i <= n; i++) {
				if (number[i] == 0) {
					number[i] = 1;
					int index = 2;
					while (i * index < n + 1) {
						number[i * index] = 2;
						index++;
					}
				}
			}

			for (int i = n / 2; i >= 2; i--) {
				if (number[i] == 1) {
					if (number[n - i] == 1) {
						bw.write(i + " " + (n - i)+"\n");
						break;
					}
				}
			}
		}
		bw.flush();
	}
}

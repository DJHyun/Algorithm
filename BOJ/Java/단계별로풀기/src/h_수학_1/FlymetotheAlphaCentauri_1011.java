//baekjoon source = "https://www.acmicpc.net/problem/1011"
package h_¼öÇÐ_1;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class FlymetotheAlphaCentauri_1011 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

		int T = Integer.parseInt(br.readLine());
		for (int t = 1; t <= T; t++) {
			String[] st = br.readLine().split(" ");
			int x = Integer.parseInt(st[0]), y = Integer.parseInt(st[1]);
			int d = y - x;
			int idx = 1;

			for (;;) {
				if (Math.pow(idx, 2) >= d) {
					break;
				}
				idx++;
			}
			double f = (double) (d - Math.pow(idx, 2));
			f = Math.ceil(f / idx);
			int result = (int)f + 2 * idx - 1;

			bw.write(String.valueOf(result)+"\n");
			bw.flush();
		}
	}
}

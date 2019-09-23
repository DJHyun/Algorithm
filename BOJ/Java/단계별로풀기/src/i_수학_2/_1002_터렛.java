//baekjoon source = "https://www.acmicpc.net/problem/1002"
package i_¼öÇÐ_2;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class _1002_ÅÍ·¿ {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		int T = Integer.parseInt(br.readLine());

		for (int t = 0; t < T; t++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			int x = Integer.parseInt(st.nextToken()), y = Integer.parseInt(st.nextToken()),
					r = Integer.parseInt(st.nextToken()), a = Integer.parseInt(st.nextToken()),
					b = Integer.parseInt(st.nextToken()), c = Integer.parseInt(st.nextToken());
			double d = Math.sqrt(Math.pow(x - a, 2) + Math.pow(y - b, 2));
			int sum = r + c, sub = Math.abs(r - c);

			if (x == a && y == b && r == c) {
				bw.write(-1 + "\n");
			} else if (sum > d && sub < d) {
				bw.write(2 + "\n");
			} else if (sum == d || d == sub) {
				bw.write(1 + "\n");
			} else {
				bw.write(0 + "\n");
			}
			bw.flush();
		}
	}
}

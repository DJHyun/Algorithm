//baekjoon source = "https://www.acmicpc.net/problem/6064"
package h_수학_1;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class 카잉달력_6064 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		int t = Integer.parseInt(br.readLine());

		for (int T = 0; T < t; T++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			int m = Integer.parseInt(st.nextToken()), n = Integer.parseInt(st.nextToken()),
					x = Integer.parseInt(st.nextToken()), y = Integer.parseInt(st.nextToken());
			int result = -1;
			int d = Math.abs(m - n);

			if (m < n) {
				int check = x;
				int index = x;
				while (true) {
					if (check == y) {
						result = index;
						break;
					}
					check -= d;
					if(check == x) break;
					if(check <= 0) {
						check = n + check;
					}
					index += m;
				}
			} else {
				int check = y;
				int index = y;
				while (true) {
					if (check == x) {
						result = index;
						break;
					}
					check -= d;
					if(check == y) break;
					if(check <= 0) {
						check = m + check;
					}
					index += n;
				}
			}
			bw.write(result + "\n");
			bw.flush();
		}
	}
}

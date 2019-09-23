//baekjoon source = "https://www.acmicpc.net/problem/2884"
package b_if문;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class 알람시계_2884 {
	public static void main(String[] args) throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		String[] st = bf.readLine().split(" ");
		int h = Integer.parseInt(st[0]);
		int m = Integer.parseInt(st[1]);

		if (m > 45) {
			m -= 45;
		} else if (m == 45) {
			m = 0;
		} else {
			if (h == 0) {
				h = 23;
			} else {
				h -= 1;
			}
			m = 60 - (45 - m);
		}

		System.out.printf("%d %d", h, m);
	}
}

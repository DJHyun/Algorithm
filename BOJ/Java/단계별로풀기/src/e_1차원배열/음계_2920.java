//baekjoon source = "https://www.acmicpc.net/problem/2920"
package e_1차원배열;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class 음계_2920 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String[] st = br.readLine().split(" ");
		int result = -1;

		for (int i = 0; i < 7; i++) {
			if (Integer.parseInt(st[i]) > Integer.parseInt(st[i + 1])) {
				if (result == 0) {
					result = 2;
					break;
				} else {
					result = 1;
				}
			} else if (Integer.parseInt(st[i]) < Integer.parseInt(st[i + 1])) {
				if (result == 1) {
					result = 2;
					break;
				} else {
					result = 0;
				}
			}
		}
		switch (result) {
		case 0:
			System.out.println("ascending");
			break;
		case 1:
			System.out.println("descending");
			break;
		case 2:
			System.out.println("mixed");
			break;
		}
	}
}

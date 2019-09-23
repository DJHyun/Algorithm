//baekjoon source = "https://www.acmicpc.net/problem/8958"
package e_1차원배열;

import java.util.Scanner;

public class OX퀴즈_8958 {
	static Scanner sc = new Scanner(System.in);

	public static void main(String[] args) {
		int n = sc.nextInt();
		for (int t = 0; t < n; t++) {
			int result = 0;
			int check = 0;
			String st = sc.next();

			for (int i = 0; i < st.length(); i++) {
				if (st.charAt(i) == 'O') {
					check++;
					result += check;
				} else {
					check = 0;
				}
			}
			System.out.println(result);
		}
	}
}

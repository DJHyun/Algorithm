//baekjoon source = "https://www.acmicpc.net/problem/10872"
package f_함수;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class 팩토리얼_10872 {
	static int result = 1;

	static void fact(int a) {
		if (a <= 1) {
			return;
		}

		result *= a;
		fact(a - 1);
	}

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		fact(Integer.parseInt(br.readLine()));
		System.out.println(result);
	}
}

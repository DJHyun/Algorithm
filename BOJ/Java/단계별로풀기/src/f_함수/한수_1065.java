//baekjoon source = "https://www.acmicpc.net/problem/1065"
package f_함수;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class 한수_1065 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		int cnt = 0;
		if (n == 1000) {
			System.out.println(144);
		} else if (n > 99 && n < 1000) {
			for(int i = 100; i<=n; i++) {
				int a = i/100;
				int b = i%100/10;
				int c = i%100%10;
				
				if (a-b == b -c) {
					cnt ++;
				}
			}
			System.out.println(99+cnt);
		} else {
			System.out.println(n);
		}

	}
}

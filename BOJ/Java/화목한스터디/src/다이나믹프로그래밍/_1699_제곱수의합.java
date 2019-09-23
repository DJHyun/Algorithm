//baekjoon source = "https://www.acmicpc.net/problem/1699"
package 다이나믹프로그래밍;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class _1699_제곱수의합 {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

		int n = Integer.parseInt(br.readLine());
		int number = 2;
		int[] check = new int[n + 1];
		check[1] = 1;

		for (int i = 2; i <= n; i++) {
			if (number * number == i) {
				number++;
				check[i] = 1;
			} else {
				check[i] = check[i - 1] + 1; 
				for (int j = 2; j * j < i; j++) {
					int c = (int) i / (j * j) + check[i % (j * j)];
					check[i] = Math.min(c, check[i]);
				}
			}
		}

		bw.write(check[n] + "");
		bw.flush();
	}
}

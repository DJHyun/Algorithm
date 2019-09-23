//baekjoon source = "https://www.acmicpc.net/problem/2438"
package c_for¹®;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class º°Âï±â_1_2438 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());

		for (int i = 1; i <= n; i++) {
			for (int j = 0; j<i; j++) {
				System.out.print("*");
			}
			System.out.println();
		}
	}
}

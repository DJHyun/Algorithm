//baekjoon source = "https://www.acmicpc.net/problem/2439"
package c_for¹®;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class º°Âï±â_2_2439 {
	public static void main(String[] args) throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(bf.readLine());
		bf.close();
		
		for (int i = 1; i <= n; i++) {
			for (int j = n - 1 - i; j > -1; j--) {
				System.out.print(" ");
			}
			for (int j = 0; j < i; j++) {
				System.out.print("*");
			}
			System.out.println();
		}
	}
}

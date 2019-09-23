//baekjoon source = "https://www.acmicpc.net/problem/10951"
package d_while문;

import java.io.IOException;
import java.util.Scanner;

public class A더하기B_4_10951 {
	public static void main(String[] args) throws IOException {
		Scanner sc = new Scanner(System.in);
		while (sc.hasNextInt()) {
			int a = sc.nextInt();
			int b = sc.nextInt();

			System.out.println(a + b);
		}
	}
}

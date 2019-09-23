//baekjoon source = "https://www.acmicpc.net/problem/1330"
package b_if문;

import java.util.Scanner;

public class 두수비교하기_1330 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int a = sc.nextInt();
		int b = sc.nextInt();
		if (a > b) {
			System.out.println(">");
		}else if(a == b) {
			System.out.println("==");
		}else {
			System.out.println("<");
		}
	}
}

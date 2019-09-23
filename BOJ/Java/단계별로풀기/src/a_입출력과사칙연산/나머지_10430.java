//baekjoon source = "https://www.acmicpc.net/problem/10430"
package a_입출력과사칙연산;

import java.util.Scanner;

public class 나머지_10430 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		double a = sc.nextDouble();
		double b = sc.nextDouble();
		double c = sc.nextDouble();

		System.out.println((int) ((a + b) % c));
		System.out.println((int) ((a % c + b % c) % c));
		System.out.println((int) ((a * b) % c));
		System.out.println((int) ((a % c * b % c) % c));
	}
}

//baekjoon source = "https://www.acmicpc.net/problem/1546"
package e_1차원배열;

import java.util.Scanner;

public class 평균_1546 {
	static double max(double[] score) {
		double result = Integer.MIN_VALUE;
		for (int i = 0; i < score.length; i++) {
			if (result < score[i]) {
				result = score[i];
			}
		}
		return result;
	}

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		double[] score = new double[n];
		for (int i = 0; i < n; i++) {
			score[i] = sc.nextDouble();
		}
		double max_ = max(score);
		double result = 0;
		
		for (double i : score) {
			result += i/max_*100;
		}
		
		System.out.printf("%.2f",result/n);
	}
}

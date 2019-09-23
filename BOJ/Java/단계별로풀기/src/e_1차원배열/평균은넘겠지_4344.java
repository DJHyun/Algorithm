//baekjoon source = "https://www.acmicpc.net/problem/4344"
package e_1차원배열;

import java.util.Scanner;

public class 평균은넘겠지_4344 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int c = sc.nextInt();
		sc.nextLine();
		for (int t = 0; t < c; t++) {
			String[] st = sc.nextLine().split(" ");
			double avg = 0;
			for (int i = 1; i < Integer.parseInt(st[0])+1; i++) {
				avg += Integer.parseInt(st[i]);
			}
			avg /= Double.parseDouble(st[0]);
			double cnt = 0;
			for (int i = 1; i < Integer.parseInt(st[0])+1; i++) {
				if(Double.parseDouble(st[i]) > avg) {
					cnt ++;
				}
			}
			cnt /= Double.parseDouble(st[0]);
			System.out.printf("%.3f%%\n",cnt*100);
		}
	}
}

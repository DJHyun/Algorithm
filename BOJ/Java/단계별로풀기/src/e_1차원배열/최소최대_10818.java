//baekjoon source = "https://www.acmicpc.net/problem/10818"
package e_1차원배열;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class 최소최대_10818 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		String[] st = br.readLine().split(" ");
		int max = Integer.MIN_VALUE;
		int min = Integer.MAX_VALUE;
		
		for (int i = 0; i<n; i++) {
			if (max < Integer.parseInt(st[i])) {
				max = Integer.parseInt(st[i]);
			}
			if (min > Integer.parseInt(st[i])) {
				min = Integer.parseInt(st[i]);
			}
		}
		System.out.printf("%d %d",min,max);
	}
}

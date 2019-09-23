//baekjoon source = "https://www.acmicpc.net/problem/10950"
package c_for문;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class A더하기B_3_10950 {
	public static void main(String[] args) throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(bf.readLine());

		for (int t = 0; t < n; t++) {
			String[] st = bf.readLine().split(" ");
			int a = Integer.parseInt(st[0]);
			int b = Integer.parseInt(st[1]);
			
			System.out.println(a+b);
		}
	}
}

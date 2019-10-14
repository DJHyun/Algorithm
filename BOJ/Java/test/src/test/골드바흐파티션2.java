package test;

import java.io.BufferedWriter;
import java.io.IOException;
import java.io.OutputStreamWriter;
import java.util.Scanner;

public class ∞ÒµÂπŸ»Â∆ƒ∆ºº«2 {
	public static void main(String[] args) throws IOException {
//		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		Scanner sc = new Scanner(System.in);
		int[] arr = new int[1000001];
		for (int i = 2; i <= 1000000; i++) {
			if (arr[i] == -1)
				continue;
			arr[i] = 1;
			for (int j = 2;; ++j) {
				if (i * j >= 1000001)
					break;
				arr[i * j] = -1;
			}
		}
		
		int t = sc.nextInt();
		StringBuilder sb = new StringBuilder();
		
		for (int test_case = 0; test_case < t; ++test_case) {
			
			int number = sc.nextInt();
			int result = 0;
			int len = (int)(number/2);
			for (int i = 2; i <= len; i++) {
				if (arr[i] == 1 && arr[(number - i)] == 1) {
					result++;
				}
			}
			sb.append(result + "\n");
		}
		bw.write(sb + "");
		bw.flush();

		bw.close();
		sc.close();
	}
}

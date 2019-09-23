//baekjoon source = "https://www.acmicpc.net/problem/2839"
package h_수학_1;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class 설탕배달_2839 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

		int n = Integer.parseInt(br.readLine());
		int result = 0;
		int idx = 1;
		int check = n;

		if (n % 5 == 0) {
			result = n / 5;
		} else {
			while (true) {
				if (check < 5 * idx) {
					break;
				}
				if ((check - 5 * idx) % 3 == 0) {
					result = idx + (check - 5 * idx) / 3;
					idx++;
				}else {
					idx++;
				}
			}
			if (result == 0) {
				if (n%3 == 0) {
					result = n/3;
				}else {
					result = -1;
				}
			}
		}

		bw.write(String.valueOf(result));
		bw.flush();
	}
}

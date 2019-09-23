//baekjoon source = "https://www.acmicpc.net/problem/2292"
package h_¼öÇÐ_1;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;

public class ¹úÁý_2292 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		long arr = 0;
		long Narr = 2;
		long n = Long.parseLong(br.readLine());
		long idx = 1;

		if (n == 1) {
			idx = 1;
		} else {

			while (true) {
				if (arr > n) {
					break;
				} else if (arr == n) {
					idx++;
					break;
				}
				arr = Narr + 6 * idx;
				Narr = arr;
				idx++;
			}
		}
		bw.write(String.valueOf(idx));
		bw.flush();
	}
}

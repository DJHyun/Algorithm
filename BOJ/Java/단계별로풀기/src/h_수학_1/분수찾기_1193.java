//baekjoon source = "https://www.acmicpc.net/problem/1193"
package h_수학_1;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class 분수찾기_1193 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

		int x = Integer.parseInt(br.readLine());
		int idx = 0;
		int i = 1;
		int mom = 1;
		for (i = 1; idx < x; i++) {
			idx += i;
		}
		i--;
		if (i % 2 == 0) {
			mom = i;
			i = 1;
			while (idx != x) {
				idx--;
				mom--;
				i++;
			}
		} else {
			
			while (idx != x) {
				idx--;
				mom++;
				i--;
			}
		}
		bw.write(mom + "/" + i);
		bw.flush();
	}
}

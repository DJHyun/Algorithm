//baekjoon source = "https://www.acmicpc.net/problem/1929"
package i_수학_2;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class 소수구하기_1929 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

		StringTokenizer st = new StringTokenizer(br.readLine());
		int m = Integer.parseInt(st.nextToken()), n = Integer.parseInt(st.nextToken());

		int[] arr = new int[n + 1];
		for (int i = 2; i < n + 1; i++) {
			if (arr[i] == 0) {
				if (i >= m) {
					bw.write(i + "\n");
				}
				arr[i] = 1;
				int index = 2;
				while (i * index < n + 1) {
					arr[i * index] = 2;
					index++;
				}
			}
		}
		bw.flush();
	}
}

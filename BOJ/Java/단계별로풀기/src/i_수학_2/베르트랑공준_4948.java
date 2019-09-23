//baekjoon source = "https://www.acmicpc.net/problem/4948"
package i_수학_2;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class 베르트랑공준_4948 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

		while (true) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			int n = Integer.parseInt(st.nextToken());
			if (n == 0)
				break;

			int[] arr = new int[2 * n + 1];
			int result = 0;
			for (int i = 2; i < 2 * n + 1; i++) {
				if (arr[i] == 0) {
					if (i > n) {
						result++;
					}
					arr[i] = 1;
					int index = 2;
					while (i * index < 2 * n + 1) {
						arr[i * index] = 1;
						index++;
					}
				}
			}
			bw.write(result + "\n");
		}
		bw.flush();
	}
}

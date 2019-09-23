//baekjoon source = "https://www.acmicpc.net/problem/1978"
package i_수학_2;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class 소수찾기_1978 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

		int n = Integer.parseInt(br.readLine());
		StringTokenizer st = new StringTokenizer(br.readLine());
		int result = 0;
		int[] arr = new int[1001];
		for (int i = 2; i < 1001; i++) {
			if (arr[i] == 0) {
				arr[i] = 1;
				int idx = 2;
				while (i * idx < 1001) {
					arr[i * idx] = 2;
					idx++;
				}
			}
		}
		for (int i = 0; i < n; i++) {
			if (arr[Integer.parseInt(st.nextToken())] == 1) {
				result++;
			}
		}
		bw.write(result + "");
		bw.flush();
	}
}

//baekjoon source = "https://www.acmicpc.net/problem/2309"
package ºê·çÆ®Æ÷½º;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.StringTokenizer;

public class ÀÏ°ö³­ÀïÀÌ_2309 {
	static int[] number;
	static int[] visited = new int[9];
	static boolean flag = false;
	static int[] result = new int[7];

	static void solution(int depth, int index, int sum) {
		if (depth > 7 || result[0] != 0)
			return;

		if (depth == 7 && sum == 100) {
			int ind = 0;
			for (int j = 0; j < 9; j++) {
				if (visited[j] != 0) {
					result[ind] = number[j];
					ind++;
				}
			}
			return;
		}

		for (int i = index; i < 9; i++) {
			if (visited[i] == 0) {
				visited[i] = 1;
				solution(depth + 1, i, sum + number[i]);
				visited[i] = 0;
			}
		}
	}

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		number = new int[9];

		for (int i = 0; i < 9; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			number[i] = Integer.parseInt(st.nextToken());
		}

		solution(0, 0, 0);
		Arrays.sort(result);
		StringBuilder sb = new StringBuilder();
		for (int i = 0; i < 7; i++) {
			if (i != 6) {
				sb.append(result[i] + "\n");
			} else {
				sb.append(result[i]);
			}
		}
		bw.write(sb + "");
		bw.flush();
	}
}

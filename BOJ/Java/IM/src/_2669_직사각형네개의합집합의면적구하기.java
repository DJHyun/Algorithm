//baekjoon source = "https://www.acmicpc.net/problem/2669"

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.StringTokenizer;

public class _2669_직사각형네개의합집합의면적구하기 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

		int[][] arr = new int[101][101];
		int result = 0,r = 0;
		for (int t = 0; t < 4; t++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			r = 0;
			int a = Integer.parseInt(st.nextToken()), b = Integer.parseInt(st.nextToken()),
					c = Integer.parseInt(st.nextToken()), d = Integer.parseInt(st.nextToken());
			for (int i = a; i < c; i++) {
				for (int j = b; j < d; ++j) {
					if (arr[i][j] != 1) {
						result++;
						arr[i][j] = 1;
					}
				}
			}
		}

		bw.write(result+"");
		bw.flush();
	}
}

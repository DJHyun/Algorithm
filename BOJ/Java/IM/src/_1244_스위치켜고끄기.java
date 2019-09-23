//baekjoon source = "https://www.acmicpc.net/problem/1244"

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.StringTokenizer;

public class _1244_스위치켜고끄기 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

		int n = Integer.parseInt(br.readLine());
		int[] arr = new int[n];
		StringTokenizer st = new StringTokenizer(br.readLine());
		for (int i = 0; i < n; ++i) {
			arr[i] = Integer.parseInt(st.nextToken());
		}
		int h = Integer.parseInt(br.readLine());

		for (int i = 0; i < h; ++i) {
			st = new StringTokenizer(br.readLine());
			if (Integer.parseInt(st.nextToken()) == 1) {
				int check = Integer.parseInt(st.nextToken());
				for (int j = 1;; ++j) {
					if (check * j - 1 > n - 1)
						break;
					arr[check * j - 1] = arr[check * j - 1] == 1 ? 0 : 1;
				}
			} else {
				int check = Integer.parseInt(st.nextToken());
				arr[check - 1] = arr[check - 1] == 1 ? 0 : 1;
				for (int j = 1;; ++j) {
					if (check - j - 1 < 0 || check + j - 1 > n - 1)
						break;
					if (arr[check - j - 1] == arr[check + j - 1]) {
						arr[check + j - 1] = arr[check + j - 1] == 1 ? 0 : 1;
						arr[check - j - 1] = arr[check - j - 1] == 1 ? 0 : 1;
					} else {
						break;
					}
				}
			}
		}
		int index = 0;
		for (int i = 0; i < n; ++i) {
			if (i != n - 1) {
				bw.write(arr[i] + " ");
			} else {
				bw.write(arr[i] + "");
			}
			index++;
			if (index%20 == 0) {
				bw.newLine();
			}
		}
		bw.flush();
	}
}

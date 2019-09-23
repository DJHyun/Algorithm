//baekjoon source = "https://www.acmicpc.net/problem/2798"
package j_브루트포스;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.StringTokenizer;

public class 블랙잭_2798 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

		StringTokenizer st = new StringTokenizer(br.readLine());
		int n = Integer.parseInt(st.nextToken()), m = Integer.parseInt(st.nextToken());
		int[] arr = new int[n];
		st = new StringTokenizer(br.readLine());
		for (int i = 0; i < n; i++) {
			arr[i] = Integer.parseInt(st.nextToken());
		}
		int result = Integer.MIN_VALUE;
		boolean oneflag = false;
		boolean twoflag = false;
		for (int i = 0; i < n - 2; i++) {
			if (!oneflag) {
				for (int j = i + 1; j < n - 1; j++) {
					if (!twoflag) {
						for (int k = j + 1; k < n; k++) {
							int check = arr[i] + arr[j] + arr[k];
							if (check > m) {
								continue;
							} else if (check == m) {
								result = check;
								oneflag = true;
								twoflag = true;
								break;
							} else {
								result = Math.max(result, check);
							}
						}

					} else {
						break;
					}
				}
			} else {
				break;
			}
		}
		bw.write(result + "\n");
		bw.flush();
	}
}

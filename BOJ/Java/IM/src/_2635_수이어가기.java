
//baekjoon source = "https://www.acmicpc.net/problem/2635"

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class _2635_수이어가기 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

		int n = Integer.parseInt(br.readLine());
		int result = 0;
		int check = 0;
		for (int i = n/2; i <= n; i++) {
			int cnt = 1;
			int number = i;
			int nn = n;
			while (number >= 0) {
				cnt++;
				int tmp = number;
				number = nn - number;
				nn = tmp;
			}
			if (result < cnt) {
				result = cnt;
				check = i;
			}
		}
		StringBuilder sb = new StringBuilder();
		sb.append(result + "\n");
		int number = check;
		int nn = n;
		while (number >= 0) {
			sb.append(nn + " ");
			int tmp = number;
			number = nn - number;
			nn = tmp;
		}
		sb.append(nn);
		bw.write(sb + "");
		bw.flush();
	}
}

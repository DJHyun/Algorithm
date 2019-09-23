//baekjoon source = "https://www.acmicpc.net/problem/2231"
package 브루트포스;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class 분해합_2231 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

		int n = Integer.parseInt(br.readLine());
		String index = "1";
		boolean flag = true;
		while (Integer.parseInt(index) < n) {
			int newIndex = Integer.parseInt(index);
			for (int i = index.length() - 1; i > -1; i--) {
				newIndex += index.charAt(i) - '0';
			}
			if (newIndex == n) {
				bw.write(index + "");
				flag = false;
				break;
			} else {
				index = (Integer.parseInt(index) + 1) + "";
			}
		}
		if (flag)
			bw.write(0 + "");
		bw.flush();
	}
}
